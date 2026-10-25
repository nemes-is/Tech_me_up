# Tech me up — Plan du parcours

Document de référence. Il décrit le cadre du parcours et garde l'historique de ses évolutions (en bas). L'état d'avancement, lui, est dans `parcours.yaml` et `progression/`.

## Contexte

Hadrien veut apprendre à programmer sans passer par une école en ligne, avec Claude comme professeur.
- **Objectif principal** : savoir lancer un produit web de A à Z (80 %). Objectifs secondaires : parler d'égal à égal avec des devs, créer de petits outils.
- **Niveau** : débutant avancé. En Python, dit connaître les bases jusqu'aux itérateurs et générateurs, la POO et les décorateurs (à vérifier par le test de positionnement). A fait du vibe coding. A appris les bases de HTML/CSS enfant et veut les retrouver.
- **Temps** : 4 à 8 h par semaine, en 2 ou 3 séances de 2 h, plus des quiz de 10 à 30 min les jours off, sur ordinateur.
- **Stack** : Python côté serveur et données, HTML/CSS/JS côté navigateur. Cible finale : une application web, puis un mini-SaaS.
- **Pédagogie demandée** : de l'académique sur ce qui s'y prête (la grammaire des langages), puis des projets. **À chaque étape, un court « pourquoi »**, pas seulement un « comment ».
- **Rôle de Claude** : il dépend du thème. Sur les leçons et exercices fondamentaux, Hadrien code seul et Claude explique, donne des indices et corrige. Sur la « plomberie » (config, déploiement, gros volumes), Claude guide davantage et va plus vite.

## 1. Principes pédagogiques

Détaillés dans `CLAUDE.md` : le pourquoi d'abord ; fondamentaux = Hadrien code ; projets = binôme ; rien de magique ; Git au quotidien ; vérifier la compréhension ; doser ; mémoire dans le dépôt.

## 2. Organisation

- **Dépôt** : `parcours.yaml` (programme), `progression/` (journal, notions), `fiches/`, `modules/`, `projets/`, `plateforme/`, `claude/` (documents de référence de Claude).
- **Rituels** : `/seance` (début de séance, échauffement), `/quiz` (révision espacée, jours off), `/fin-seance` (journal, fiches, progression, commit).
- **Plateforme V1** : app locale FastAPI + Jinja2, en lecture seule. Tableau de bord (avancement, notions, séances) et bibliothèque de fiches (recherche, filtres). Extensions prévues : quiz à répétition espacée, lecture des leçons.
- **Mémoire** : pas de mémoire locale de Claude. Tout vit dans le dépôt.

## 3. Programme

Chaque module mêle des leçons « grammaire » (Hadrien fait les exercices seul) et un projet. Projets fil rouge : ludiques ou créatifs au début, puis des outils de plus en plus complexes, et enfin le mini-SaaS.

| # | Module | Contenu clé | Projet fil rouge |
|---|--------|-------------|------------------|
| 0 | Environnement | **Test de positionnement Python** (en premier), terminal, VS Code, uv, Git et GitHub | Premier dépôt GitHub |
| 1 | Python : consolidation | Révision ciblée selon le test, modules et packages, annotations de type, pytest, débogage | 🎲 Jeu textuel ou art génératif |
| 2 | HTML et CSS | Balises sémantiques, liens et navigation, sélecteurs, modèle de boîte, flexbox et grid, responsive | 📚 La micro-encyclopédie (plusieurs pages liées, faites à la main) |
| 3 | Données | Fichiers, JSON, CSV, APIs externes, SQL et SQLite | 🔧 Outil n°1 en ligne de commande |
| 4 | Comment marche le web | HTTP, client/serveur, DNS, bases de JS, le DOM | 🌐 L'encyclopédie publiée en ligne, avec des touches de JS |
| 5 | Backend web | FastAPI, templates, SQLModel, formulaires, authentification. Option : lire le code de la plateforme | 🔧 Outil n°2 : app web perso |
| 6 | Interactivité | Événements, fetch, htmx ou mini-framework | 🔧 Outil n°2 enrichi |
| 7 | Mise en production | Déploiement, variables d'environnement, sécurité de base, domaine | 🔧 Outil n°2 en ligne |
| 8 | Mini-SaaS | Idée et validation, MVP, comptes multi-utilisateurs, paiement, lancement | 🚀 Le mini-SaaS |

Sujets transversaux : Git, débogage, lecture de doc, utiliser l'IA intelligemment sans retomber dans le vibe coding aveugle.

### Test de positionnement (première séance)

Une série d'exercices courts de difficulté croissante, à faire dans `modules/00-environnement/exercices/` : un survol rapide des bases, puis les compréhensions, les fonctions avancées (`*args`, `**kwargs`, closures), les itérateurs et générateurs, la POO (héritage, méthodes spéciales), les décorateurs, les gestionnaires de contexte, les exceptions, et un peu de lecture de code. Pas de note : le but est de détailler le module 1 en fonction des trous.

## Historique

- **2026-10-19** : plan initial (cadrage en mode plan). Module 1 = grammaire Python complète ; HTML/CSS au module 4.
- **2026-10-20** : après retour d'Hadrien.
  - Le module 1 devient une **consolidation** Python, calibrée par le test, car les bases sont acquises.
  - Création d'un module 2 **HTML et CSS**, avec pour projet la micro-encyclopédie. L'ancien module 2 (structurer) est fusionné dans le module 1.
  - Le module 4 se concentre sur HTTP et JavaScript, et son projet devient la mise en ligne de l'encyclopédie.
  - Le test de positionnement ouvre la première séance.
  - Le plan est déplacé dans `claude/`, et la mémoire locale de Claude n'est plus utilisée.
