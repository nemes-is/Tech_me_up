# Tech me up

Mon parcours pour apprendre à programmer, de zéro jusqu'au lancement d'un produit web, avec Claude comme professeur.

## Le parcours

| # | Module | Projet fil rouge |
|---|--------|------------------|
| 0 | Environnement | Premier dépôt GitHub |
| 1 | Python : consolidation | Jeu textuel ou art génératif |
| 2 | HTML et CSS | La micro-encyclopédie |
| 3 | Données | Outil n°1 en ligne de commande |
| 4 | Comment marche le web | L'encyclopédie en ligne |
| 5 | Backend web | Outil n°2 : app web perso |
| 6 | Interactivité | Outil n°2 enrichi |
| 7 | Mise en production | Outil n°2 en ligne |
| 8 | Mini-SaaS | Le mini-SaaS |

Le détail est dans [parcours.yaml](parcours.yaml).

## La plateforme

Un petit site local pour suivre ma progression et relire mes fiches mémo.

```bash
uv run plateforme
```

Puis ouvrir http://localhost:8000.

## Organisation

- `fiches/` : fiches mémo
- `progression/` : journal des séances et maîtrise des notions
- `modules/` : leçons et exercices
- `projets/` : projets fil rouge
- `plateforme/` : le code de la plateforme
- `claude/` : documents de référence de Claude (plan du parcours, décisions)
