---
titre: Variables, références et mutabilité
theme: Python
tags: [python, variables, listes, pieges]
module: m1
date: 2026-10-22
---

## Le problème

On modifie une liste via un nom, et une autre variable « change toute seule ». Ou une fonction garde en mémoire des valeurs d'un appel à l'autre. Ces bugs semblent magiques tant qu'on pense qu'une variable est une boîte.

## L'idée

Une variable est une **étiquette collée sur un objet**, pas une boîte qui contient une valeur.

- `b = a` colle une deuxième étiquette sur **le même** objet.
- **Muable** (`list`, `dict`, `set`) : l'objet peut être modifié sur place, et toutes ses étiquettes voient le changement.
- **Immuable** (`int`, `str`, `tuple`) : impossible de le modifier. Toute « modification » crée un nouvel objet et y déplace l'étiquette. On ne transforme pas un 5 en 6, on va chercher celui d'à côté.

## En pratique

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)          # [1, 2, 3, 4] : même liste

c = a.copy()      # une vraie copie, indépendante

x = 5
y = x
y += 1
print(x)          # 5 : y pointe maintenant vers un autre objet
```

## Pourquoi c'est comme ça

Copier un objet entier à chaque `=` serait lent et gourmand en mémoire. Python ne copie donc que si on le demande explicitement.

## Pièges

- **Argument par défaut mutable** : `def f(bag=[])` crée la liste une seule fois, au moment du `def`. Elle est partagée par tous les appels. Écrire `bag=None` puis `if bag is None: bag = []`.
- Passer une liste à une fonction, c'est lui donner une étiquette vers **ta** liste : si elle la modifie, tu le vois.
