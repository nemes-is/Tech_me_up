# Git et GitHub : premier commit, premier push

*Séance du 2026-10-25.*

## 1. Pourquoi maintenant

Avant cette séance, le projet n'avait ni historique ni vraie sauvegarde. Il vivait dans un dossier iCloud qui l'avait déjà abîmé. Or iCloud n'est pas une sauvegarde mais une **synchronisation** : si un fichier est supprimé ou cassé, la version cassée part aussi dans le cloud.

Ce que protège chaque outil :

| | Protège de… | Ne protège pas de… |
|---|---|---|
| **Git (local)** | tes erreurs : revenir à hier, voir ce qui a changé | la panne du disque (`.git` est sur le même disque) |
| **GitHub** | la panne, le vol, le changement d'ordi | rien de tout ça, tant que tu fais `git push` |

## 2. Créer le dépôt : `git init`

```bash
cd ~/Code/Tech_me_up
git init        # crée le dossier caché .git (la boîte à photos), vide
git status      # « où en suis-je ? » : la commande la plus utile
```

`git init` ne prend aucune photo et ne touche à aucun fichier.

**Le `.gitignore`** liste ce que Git doit faire semblant de ne pas voir. C'est pour ça que `.venv` n'apparaissait pas dans `git status` : il se recrée avec `uv`, il est lourd et il est propre à chaque machine. On y a aussi ajouté `.claude/settings.local.json` : le mot `local` signale un réglage propre à une machine, qui ne se partage pas.

## 3. Prendre une photo : `git add`, puis `git commit`

```
fichiers modifiés  --git add-->  zone de préparation  --git commit-->  historique
```

**Pourquoi deux temps ?** Pour choisir ce qui entre dans la photo. Si tu as corrigé un bug **et** commencé une nouvelle page, tu fais deux commits séparés, avec deux messages clairs.

```bash
git add .                       # tout le dossier (sauf ce qui est ignoré)
git rm --cached <fichier>       # retire un fichier de la préparation, SANS l'effacer du disque
git commit -m "Message"         # prend la photo
git log                         # l'historique (q pour sortir)
```

### Les trois états d'un fichier

| État | Sens | Dans `git status` |
|---|---|---|
| **untracked** | jamais photographié | `Untracked files:` |
| **modified** | déjà dans une photo, mais changé depuis | `Changes not staged for commit:` |
| **staged** | prêt pour la prochaine photo | `Changes to be committed:` |

### Le hash

`edd766cfc980c601d3f9f8b4cdc28fd4d84ad9b2` est l'empreinte du commit. Git la calcule à partir du contenu, du message, de l'auteur, de la date et du commit parent. Changer une virgule donne une empreinte totalement différente. Les 7 premiers caractères (`edd766c`) suffisent pour désigner un commit.

- `(root-commit)` : le premier commit, le seul sans parent.
- `HEAD -> main` : le « vous êtes ici » de Git.

### Un bon message de commit

Il dit **ce que fait** le commit, pas l'état du projet, puisque l'état se lit dans les fichiers. Il tient en **une ligne courte** (environ 50 caractères), écrite comme un titre :

- ✅ `Premier commit : parcours, fiches et plateforme`
- ❌ `Créé toute l'infrastructure du projet et du repo. Conçu le framework…` (deux phrases, trop long)

## 4. Envoyer sur GitHub

1. Sur github.com, créer un dépôt **privé** et **vide** : ne pas cocher de README. Sinon, le dépôt distant a son propre premier commit, et les deux historiques n'ont pas d'ancêtre commun.
2. Vérifier que le Mac peut parler à GitHub :
   ```bash
   ssh -T git@github.com     # « Hi nemes-is! You've successfully authenticated… »
   ```
   **Une clé SSH**, c'est une paire de clés. La clé publique est déposée sur GitHub, c'est la serrure. La clé privée ne quitte jamais le Mac, c'est la clé qui l'ouvre. Depuis 2021, GitHub refuse les mots de passe pour `git push`.
3. Relier, puis pousser :
   ```bash
   git remote add origin git@github.com:nemes-is/Tech_me_up.git
   git push -u origin main   # -u : les fois suivantes, « git push » suffira
   ```

`origin` est le surnom conventionnel du dépôt distant. GitHub affiche la date du **commit**, pas celle du push : ce sont deux gestes séparés.

## 5. Le scénario « nouvel ordi » : `git clone`

```bash
git clone git@github.com:nemes-is/Tech_me_up.git
cd Tech_me_up
uv run plateforme      # uv recrée .venv tout seul, à partir de pyproject.toml et uv.lock
```

Le clone récupère les fichiers **et** l'historique (`.git`), mais pas `.venv`. Et c'est très bien comme ça.

## 6. En passant : qui occupe le port 8000 ?

Un seul programme à la fois peut écouter un port donné.

```bash
lsof -i :8000              # liste ce qui utilise le port ; LISTEN = le serveur
lsof -a -p <PID> -d cwd    # le dossier d'où ce programme a été lancé
kill <PID>                 # lui demande poliment de s'arrêter (comme Ctrl + C)
```

Le terminal de VS Code et celui du bureau font tourner le même shell (zsh). Il y a deux différences : celui de VS Code démarre dans le dossier du projet, et il s'arrête quand on ferme VS Code.
