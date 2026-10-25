"""Lecture des fichiers du parcours.

La plateforme ne stocke rien elle-même : tout vient des fichiers texte du dépôt
(parcours.yaml, progression/, fiches/). Ce module les lit à chaque requête et les
transforme en objets Python simples que les pages peuvent afficher. Comme on relit
les fichiers à chaque fois, une modification se voit dès qu'on rafraîchit la page.
"""

import unicodedata
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import markdown
import yaml

# Racine du dépôt : le dossier parent de plateforme/
ROOT = Path(__file__).resolve().parent.parent

STEP_STATUSES = ("a_faire", "en_cours", "fait")
MASTERY_LEVELS = ("fragile", "en_cours", "acquis")


# --- Outils génériques -------------------------------------------------------

def read_yaml(path: Path) -> dict:
    """Lit un fichier YAML. Un fichier absent ou vide donne un dictionnaire vide."""
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def read_front_matter(path: Path) -> tuple[dict, str]:
    """Sépare l'en-tête YAML (entre deux lignes ---) du corps Markdown."""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        # maxsplit=2 : on ne coupe qu'aux deux premiers ---, le corps peut en contenir
        _, header, body = text.split("---", 2)
        return yaml.safe_load(header) or {}, body.strip()
    return {}, text.strip()


def render_markdown(text: str) -> str:
    """Convertit du Markdown en HTML, avec tableaux et coloration du code."""
    return markdown.markdown(
        text,
        extensions=["fenced_code", "codehilite", "tables"],
        extension_configs={"codehilite": {"guess_lang": False}},
    )


def to_date(value) -> date | None:
    """YAML convertit déjà 2026-10-19 en date ; on accepte aussi une chaîne."""
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None


def normalize(text: str) -> str:
    """Minuscules sans accents, pour qu'une recherche « debut » trouve « début »."""
    decomposed = unicodedata.normalize("NFD", text.lower())
    return "".join(c for c in decomposed if unicodedata.category(c) != "Mn")


# --- Le parcours -------------------------------------------------------------

@dataclass
class Step:
    id: str
    title: str
    kind: str
    status: str


@dataclass
class Module:
    id: str
    number: int
    title: str
    goal: str
    steps: list[Step]

    @property
    def done(self) -> int:
        return sum(1 for s in self.steps if s.status == "fait")

    @property
    def total(self) -> int:
        return len(self.steps)

    @property
    def percent(self) -> int:
        return round(100 * self.done / self.total) if self.total else 0

    @property
    def status(self) -> str:
        if self.total and self.done == self.total:
            return "fait"
        if any(s.status != "a_faire" for s in self.steps):
            return "en_cours"
        return "a_faire"


def load_modules() -> list[Module]:
    data = read_yaml(ROOT / "parcours.yaml")
    modules = []
    for m in data.get("modules", []):
        steps = [
            Step(
                id=s["id"],
                title=s.get("titre", s["id"]),
                kind=s.get("type", "lecon"),
                status=s.get("statut", "a_faire"),
            )
            for s in m.get("etapes", [])
        ]
        modules.append(Module(
            id=m["id"],
            number=m.get("numero", len(modules)),
            title=m.get("titre", m["id"]),
            goal=m.get("objectif", ""),
            steps=steps,
        ))
    return modules


def next_step(modules: list[Module]) -> tuple[Module, Step] | None:
    """L'étape en cours s'il y en a une, sinon la première étape à faire."""
    for wanted in ("en_cours", "a_faire"):
        for module in modules:
            for step in module.steps:
                if step.status == wanted:
                    return module, step
    return None


# --- Les notions -------------------------------------------------------------

@dataclass
class Notion:
    id: str
    title: str
    module: str
    mastery: str
    fiche: str | None
    seen_on: date | None
    next_review: date | None

    @property
    def is_due(self) -> bool:
        return self.next_review is not None and self.next_review <= date.today()


def load_notions() -> list[Notion]:
    data = read_yaml(ROOT / "progression" / "notions.yaml")
    return [
        Notion(
            id=n["id"],
            title=n.get("titre", n["id"]),
            module=n.get("module", ""),
            mastery=n.get("maitrise", "fragile"),
            fiche=n.get("fiche"),
            seen_on=to_date(n.get("vue_le")),
            next_review=to_date(n.get("prochaine_revision")),
        )
        for n in data.get("notions") or []
    ]


# --- Les fiches --------------------------------------------------------------

@dataclass
class Fiche:
    slug: str
    title: str
    theme: str
    tags: list[str]
    module: str
    date: date | None
    body: str

    @property
    def html(self) -> str:
        return render_markdown(self.body)

    @property
    def excerpt(self) -> str:
        """Première ligne de texte « normal » du corps, pour l'aperçu dans la liste."""
        for line in self.body.splitlines():
            line = line.strip()
            if line and not line.startswith(("#", "|", "`", "-", ">")):
                text = line.replace("**", "").replace("`", "")
                return text if len(text) <= 160 else text[:157].rstrip() + "…"
        return ""

    def matches(self, query: str) -> bool:
        haystack = normalize(" ".join([self.title, self.theme, *self.tags, self.body]))
        return all(word in haystack for word in normalize(query).split())


def load_fiches() -> list[Fiche]:
    fiches = []
    for path in sorted((ROOT / "fiches").glob("*.md")):
        meta, body = read_front_matter(path)
        fiches.append(Fiche(
            slug=path.stem,
            title=meta.get("titre", path.stem),
            theme=meta.get("theme", "Divers"),
            tags=[str(t) for t in meta.get("tags", [])],
            module=meta.get("module", ""),
            date=to_date(meta.get("date")),
            body=body,
        ))
    # Les plus récentes d'abord ; date.min place les fiches sans date à la fin
    fiches.sort(key=lambda f: f.date or date.min, reverse=True)
    return fiches


# --- Le journal --------------------------------------------------------------

@dataclass
class JournalEntry:
    slug: str
    title: str
    date: date | None
    duration: str
    module: str
    body: str

    @property
    def html(self) -> str:
        return render_markdown(self.body)


def load_journal() -> list[JournalEntry]:
    entries = []
    for path in (ROOT / "progression" / "journal").glob("*.md"):
        meta, body = read_front_matter(path)
        entries.append(JournalEntry(
            slug=path.stem,
            title=meta.get("titre", path.stem),
            date=to_date(meta.get("date")) or to_date(path.stem[:10]),
            duration=str(meta.get("duree", "")),
            module=meta.get("module", ""),
            body=body,
        ))
    entries.sort(key=lambda e: (e.date or date.min, e.slug), reverse=True)
    return entries
