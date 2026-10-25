# Le terminal, le PATH et l'environnement Python

*Séance du 2026-10-22, née d'un dépannage : « le serveur ne répond plus ».*

## 1. Un serveur vit avec son terminal

Un serveur, c'est un programme qui tourne en continu et attend des requêtes. Quand on le lance dans un terminal, il **appartient** à ce terminal : si on ferme le terminal (ou VS Code, qui contient le terminal), macOS arrête le programme. Rien n'est cassé, il suffit de le relancer.

- `Ctrl + C` dans le terminal : arrête le serveur proprement.
- Deux serveurs ne peuvent pas écouter sur le même port. Si le port 8000 est déjà pris, le second échoue avec `address already in use`.

## 2. Le code se copie, l'environnement se recrée

Un projet, c'est du code **et** un environnement pour le faire tourner : la bonne version de Python et les bibliothèques (FastAPI, uvicorn…).

- Les bibliothèques sont listées dans `pyproject.toml` (et figées précisément dans `uv.lock`).
- `uv` les installe dans un dossier isolé propre au projet, `.venv`. Comme ça, elles ne se mélangent ni avec le Python du système ni avec les autres projets.
- `.venv` est **jetable** : il contient des chemins absolus propres à une machine, donc on ne le copie pas et on ne le met pas dans Git (voir `.gitignore`). Chaque machine le recrée avec `uv run …` ou `uv sync`.

C'est pour ça que la plateforme avait tourné le 19 (sur la machine distante de Claude, où `uv` existait) mais pas sur le Mac : les fichiers étaient arrivés, pas l'environnement.

## 3. Le PATH : où le terminal cherche les commandes

Quand on tape `uv`, le terminal ne fouille pas tout le disque : il cherche dans une liste de dossiers, la variable `PATH`. Si le programme est ailleurs, on obtient `command not found`, alors qu'on peut toujours le lancer avec son chemin complet (`~/.local/bin/uv`).

Le `PATH` est défini dans les fichiers de réglages du shell (`~/.zshrc`, `~/.zshenv`). Le point clé :

> Le shell lit ces fichiers **une seule fois, au démarrage**, et garde le résultat en mémoire.

Hadrien l'a résumé ainsi : c'est comme un papier qu'on lit puis qu'on pose devant soi. Si quelqu'un modifie le papier, on ne le sait pas tant qu'on ne l'a pas relu.

- Chaque fenêtre de terminal est une **instance séparée**, avec sa propre copie en mémoire. Modifier le réglage et le relire dans le terminal A ne change rien pour le terminal B.
- Pour relire sans fermer : `source ~/.zshrc`.

## 4. Piège : un projet de code dans un dossier synchronisé

`Documents` était synchronisé avec iCloud, et le disque était plein. Résultat :
- iCloud supprimait les copies locales des fichiers (ils n'existaient plus qu'en ligne) ;
- iCloud marquait comme « cachés » certains fichiers de `.venv`, que Python 3.12 ignore par sécurité, d'où `No module named 'plateforme'`.

La bonne pratique : le code vit dans un dossier **non synchronisé** (par exemple `~/Code`), et c'est **Git + GitHub** qui le sauvegarde.
