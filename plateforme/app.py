"""La plateforme Tech me up : un petit site local pour suivre le parcours.

FastAPI reçoit les requêtes du navigateur (« donne-moi la page /fiches ») et appelle
la fonction correspondante. Chaque fonction lit les données via content.py, puis
remplit un template HTML (dossier templates/) avec Jinja2.
"""

import threading
import webbrowser
from collections import Counter
from datetime import date
from pathlib import Path

import yaml
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pygments.formatters import HtmlFormatter

from . import content

HERE = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 8000

app = FastAPI(title="Tech me up")
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")

# Libellés affichés pour les valeurs stockées dans les fichiers YAML
LABELS = {
    "a_faire": "À faire",
    "en_cours": "En cours",
    "fait": "Fait",
    "fragile": "Fragile",
    "acquis": "Acquis",
    "lecon": "Leçon",
    "exercice": "Exercice",
    "projet": "Projet",
    "test": "Test",
}
templates.env.globals["label"] = lambda value: LABELS.get(value, value)


def format_date(value: date | None) -> str:
    months = ["janv.", "févr.", "mars", "avr.", "mai", "juin",
              "juil.", "août", "sept.", "oct.", "nov.", "déc."]
    return f"{value.day} {months[value.month - 1]} {value.year}" if value else ""


templates.env.filters["date_fr"] = format_date


@app.exception_handler(yaml.YAMLError)
def yaml_error(request: Request, exc: yaml.YAMLError):
    """Un fichier YAML mal formé affiche une page claire plutôt qu'une erreur brute."""
    return templates.TemplateResponse(
        request, "error.html", {"message": str(exc)}, status_code=500
    )


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    modules = content.load_modules()
    notions = content.load_notions()
    steps = [s for m in modules for s in m.steps]
    done = sum(1 for s in steps if s.status == "fait")

    return templates.TemplateResponse(request, "dashboard.html", {
        "modules": modules,
        "next": content.next_step(modules),
        "done": done,
        "total": len(steps),
        "percent": round(100 * done / len(steps)) if steps else 0,
        "mastery_counts": Counter(n.mastery for n in notions),
        "mastery_levels": content.MASTERY_LEVELS,
        "due": [n for n in notions if n.is_due],
        "fragile": [n for n in notions if n.mastery == "fragile" and not n.is_due],
        "notions_total": len(notions),
        "journal": content.load_journal()[:5],
        "today": date.today(),
    })


@app.get("/fiches", response_class=HTMLResponse)
def fiches(request: Request, q: str = "", tag: str = "", theme: str = ""):
    # q, tag et theme viennent de l'URL : /fiches?q=git&tag=bases
    all_fiches = content.load_fiches()
    shown = [
        f for f in all_fiches
        if (not q or f.matches(q))
        and (not tag or tag in f.tags)
        and (not theme or f.theme == theme)
    ]
    return templates.TemplateResponse(request, "fiches.html", {
        "fiches": shown,
        "total": len(all_fiches),
        "themes": sorted({f.theme for f in all_fiches}),
        "tags": Counter(t for f in all_fiches for t in f.tags).most_common(),
        "q": q,
        "tag": tag,
        "theme": theme,
    })


@app.get("/fiches/{slug}", response_class=HTMLResponse)
def fiche(request: Request, slug: str):
    # On cherche le slug parmi les fiches existantes plutôt que d'ouvrir un chemin
    # construit depuis l'URL : impossible ainsi de lire un fichier hors de fiches/.
    found = next((f for f in content.load_fiches() if f.slug == slug), None)
    if found is None:
        raise HTTPException(status_code=404, detail="Fiche introuvable")
    return templates.TemplateResponse(request, "fiche.html", {"fiche": found})


@app.get("/journal/{slug}", response_class=HTMLResponse)
def journal_entry(request: Request, slug: str):
    found = next((e for e in content.load_journal() if e.slug == slug), None)
    if found is None:
        raise HTTPException(status_code=404, detail="Séance introuvable")
    return templates.TemplateResponse(request, "journal.html", {"entry": found})


@app.get("/pygments.css")
def pygments_css():
    """Couleurs de la coloration syntaxique, en version claire et sombre."""
    light = HtmlFormatter(style="friendly").get_style_defs(".codehilite")
    dark = HtmlFormatter(style="github-dark").get_style_defs(".codehilite")
    css = f"{light}\n@media (prefers-color-scheme: dark) {{\n{dark}\n}}"
    return Response(css, media_type="text/css")


def run():
    """Point d'entrée de `uv run plateforme`."""
    import uvicorn

    url = f"http://localhost:{PORT}"
    print(f"\n  Tech me up tourne sur {url}  (Ctrl+C pour arrêter)\n")
    # On ouvre le navigateur une seconde plus tard, le temps que le serveur démarre
    threading.Timer(1.0, webbrowser.open, args=[url]).start()
    uvicorn.run(app, host=HOST, port=PORT, log_level="warning")
