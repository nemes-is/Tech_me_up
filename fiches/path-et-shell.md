---
titre: Le PATH et les réglages du terminal
theme: Outils
tags: [terminal, shell, path, zsh]
module: m0
date: 2026-10-22
---

## Le problème

On vient d'installer un programme, et le terminal répond `command not found`.

## L'idée

Le terminal ne fouille pas tout le disque : il cherche les commandes dans une liste de dossiers, la variable **`PATH`**. Cette liste est définie dans les fichiers de réglages du shell (`~/.zshrc`, `~/.zshenv`).

Le shell lit ces fichiers **une seule fois, au démarrage**, et garde le résultat en mémoire. C'est comme un papier qu'on lit puis qu'on pose devant soi : si quelqu'un le modifie, on ne le sait pas tant qu'on ne l'a pas relu.

## En pratique

```bash
echo $PATH                 # voir la liste des dossiers
~/.local/bin/uv --version  # le chemin complet marche toujours
source ~/.zshrc            # relire les réglages sans fermer le terminal
```

## Pourquoi c'est comme ça

Relire les réglages à chaque commande serait lent, et un réglage pourrait changer en plein milieu de ton travail.

## Pièges

- Chaque fenêtre de terminal est une instance séparée, avec sa propre copie du `PATH`. Relire les réglages dans une fenêtre ne change rien pour les autres.
- `command not found` ne veut pas dire « pas installé » : souvent, le programme est bien là, mais pas dans un dossier du `PATH`.
- Une ligne qui finit par `\` veut dire « la commande continue à la ligne suivante » : le terminal attend la suite.
