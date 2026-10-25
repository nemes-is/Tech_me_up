---
titre: "Serveur local : localhost"
theme: Web
tags: [web, serveur, bases]
module: m0
date: 2026-10-19
---

## Le problème

Une app web a besoin d'un **serveur** : un programme qui attend des demandes (« donne-moi la page des fiches ») et y répond. En développement, on ne veut pas mettre l'app en ligne à chaque modification pour la tester.

## L'idée

On fait tourner le serveur **sur son propre ordinateur**. Le navigateur lui parle comme à n'importe quel site, mais sans passer par internet.

- `localhost` est un nom spécial qui veut dire « cet ordinateur-ci ».
- Le nombre après les deux-points (`:8000`) est le **port** : un numéro de « porte » qui permet de faire tourner plusieurs serveurs en même temps sur la même machine.

## En pratique

```bash
uv run plateforme          # démarre le serveur de la plateforme
# puis ouvrir http://localhost:8000 dans le navigateur
# Ctrl+C dans le terminal pour l'arrêter
```

## Pourquoi c'est comme ça

Le navigateur et le serveur sont deux programmes séparés qui communiquent selon les mêmes règles (le protocole HTTP), qu'ils soient sur la même machine ou à l'autre bout du monde. Une app qui marche en local marchera donc en ligne de la même façon, ou presque.

## Pièges

- Le serveur vit tant que le terminal qui l'a lancé reste ouvert. Fermer le terminal (ou VS Code, qui le contient) arrête le serveur : il suffit de relancer la commande.
- Deux serveurs ne peuvent pas écouter sur le même port : le second échoue avec `address already in use`.
- `localhost` sur ton Mac n'est accessible que depuis ton Mac : personne d'autre ne peut voir ton app.
