# Test de positionnement Python, partie 1 : correction

*Séance du 2026-10-22. Six questions de prédiction, sans exécuter le code.*

## 1. Deux noms, une seule liste

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)        # [1, 2, 3, 4]
```

En Python, une variable n'est pas une boîte qui contient une valeur, c'est une **étiquette collée sur un objet**. `b = a` ne copie rien : ça colle une deuxième étiquette sur la même liste. Pour une vraie copie : `b = a.copy()`.

*Pourquoi :* copier un objet entier à chaque `=` serait coûteux. Python ne copie que si on le demande.

## 2. L'argument par défaut mutable

```python
def add(item, bag=[]):
    bag.append(item)
    return bag

print(add(1))   # [1]
print(add(2))   # [1, 2]
```

La valeur par défaut `[]` est créée **une seule fois**, quand Python lit le `def`, et non à chaque appel. Tous les appels partagent la même liste. La parade classique :

```python
def add(item, bag=None):
    if bag is None:
        bag = []
    bag.append(item)
    return bag
```

## 3. Compréhension de dictionnaire

```python
words = ["chat", "chien", "cheval", "ane"]
print({w: len(w) for w in words if w.startswith("ch")})
# {'chat': 4, 'chien': 5, 'cheval': 6}
```

`{clé: valeur for …}` construit un **dictionnaire**. Sans les deux-points, `{len(w) for …}`, on obtiendrait un **set** : `{4, 5, 6}`.

## 4. Un générateur est paresseux

```python
def countdown(n):
    print("start")
    while n > 0:
        yield n
        n -= 1

g = countdown(3)
print("avant")      # avant
print(next(g))      # start, puis 3
print(list(g))      # [2, 1]
print(list(g))      # []
```

- Appeler `countdown(3)` **n'exécute rien** : ça fabrique le générateur. Le corps démarre au premier `next()`.
- Chaque `next()` avance jusqu'au `yield` suivant.
- `list(g)` consomme **ce qui reste**. Une fois épuisé, le générateur ne redonne rien.
- `list()` intercepte lui-même le `StopIteration` : pas d'erreur visible.

## 5. Attribut de classe et attribut d'instance (juste)

```python
class Counter:
    total = 0
    def __init__(self):
        Counter.total += 1
        self.id = Counter.total

a = Counter()
b = Counter()
print(a.id, b.id, Counter.total)   # 1 2 2
```

`total` appartient à la classe, il est partagé par toutes les instances. `id` appartient à chaque instance.

## 6. Décorateur (presque juste)

```python
def shout(func):
    def wrapper(name):
        return func(name).upper() + "!"
    return wrapper

@shout
def greet(name):
    return f"salut {name}"

print(greet("hadrien"))   # SALUT HADRIEN!
```

`@shout` remplace `greet` par `wrapper`. `.upper()` s'applique à toute la chaîne renvoyée par `func(name)`.

## Pour aller plus loin : muable ou immuable

```python
x = 5
y = x
y += 1
print(x)        # 5
```

Un entier est **immuable** : on ne peut pas le modifier sur place. `y += 1` crée un nouvel objet `6` et y déplace l'étiquette `y`. Avec la formule d'Hadrien : « on ne transforme pas un 5 en 6, on va chercher celui d'à côté ».

- Immuables : `int`, `float`, `str`, `tuple`.
- Muables : `list`, `dict`, `set`, et la plupart des objets qu'on crée soi-même.

La différence entre « boîte » et « étiquette » n'apparaît que lorsqu'on **modifie** un objet muable qui porte plusieurs noms.

## Bilan

| Thème | Résultat |
|---|---|
| Variables et références | à travailler (questions 1 et 2) |
| Compréhensions | à consolider (question 3) |
| Générateurs | à travailler (question 4) |
| POO, attributs de classe | acquis (question 5) |
| Décorateurs | bon (question 6) |
