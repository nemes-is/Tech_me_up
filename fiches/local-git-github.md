---
titre: Local, Git et GitHub
theme: Outils
tags: [git, github, bases]
module: m0
date: 2026-10-19
---

## Le problème

Quand on code, on veut pouvoir revenir en arrière si on casse quelque chose, savoir ce qui a changé et quand, et ne pas perdre son travail si l'ordinateur meurt.

## L'idée : trois choses distinctes

| | C'est quoi | Où ça vit |
|---|---|---|
| **Local** | Tes fichiers, que tu modifies dans VS Code et que tu fais tourner sur ton Mac | Ton ordinateur |
| **Git** | Un outil qui enregistre l'**historique** de ton projet sous forme de *commits* (des points de sauvegarde avec un message) | Ton ordinateur aussi ! (dossier caché `.git`) |
| **GitHub** | Un site qui garde une **copie en ligne** de ton historique Git | Internet |

Git ne change rien à ta façon de travailler : tu continues à éditer dans VS Code et à lancer ton app en local.

## En pratique

```bash
git status                 # qu'est-ce qui a changé depuis le dernier commit ?
git add fichier.py         # « je veux inclure ce changement dans le prochain commit »
git commit -m "Ajoute la page de connexion"   # crée le point de sauvegarde
git push                   # envoie les nouveaux commits sur GitHub
git pull                   # récupère depuis GitHub les commits faits ailleurs
```

## Pourquoi c'est comme ça

- **Git est local** pour que tu puisses travailler hors ligne et que chaque commit soit instantané.
- **GitHub est séparé** pour servir de sauvegarde, de point de rencontre entre plusieurs ordinateurs ou plusieurs personnes et, plus tard, de point de départ pour **déployer** ton app (beaucoup d'hébergeurs la mettent en ligne directement depuis GitHub).

## Pièges

- Un commit n'est **pas** envoyé en ligne tant que tu n'as pas fait `git push`.
- Ne jamais committer de mot de passe ou de clé secrète : même effacé ensuite, il reste dans l'historique.
