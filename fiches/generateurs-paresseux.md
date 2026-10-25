---
titre: Les générateurs sont paresseux
theme: Python
tags: [python, generateurs, yield, iterateurs]
module: m1
date: 2026-10-22
---

## Le problème

Produire une longue suite de valeurs (les lignes d'un gros fichier, une suite infinie…) en construisant toute la liste d'un coup prend beaucoup de mémoire, voire est impossible.

## L'idée

Un générateur (une fonction avec `yield`) produit ses valeurs **une par une, seulement quand on les demande**.

- Appeler la fonction **n'exécute rien** : ça fabrique un générateur.
- Chaque `next()` exécute le corps jusqu'au `yield` suivant, puis met la fonction en pause.
- Un générateur ne se parcourt **qu'une fois**. Épuisé, il ne redonne rien.

## En pratique

```python
def countdown(n):
    print("start")
    while n > 0:
        yield n
        n -= 1

g = countdown(3)   # rien ne s'affiche encore
next(g)            # affiche "start", renvoie 3
list(g)            # [2, 1] : ce qui reste
list(g)            # [] : épuisé
```

## Pourquoi c'est comme ça

En ne calculant que le nécessaire, on garde en mémoire une seule valeur à la fois, quelle que soit la longueur de la suite.

## Pièges

- `for`, `list()`, `sum()`… interceptent eux-mêmes le `StopIteration` de fin : on ne le voit qu'avec `next()` sur un générateur épuisé.
- Vouloir parcourir deux fois le même générateur donne une seconde fois vide. Si on en a besoin plusieurs fois : `list(g)` une fois, puis on réutilise la liste.
