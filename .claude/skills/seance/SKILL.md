---
name: seance
description: Démarre une séance d'apprentissage de 2 h - lit l'état du parcours, fait un échauffement de révision, puis lance la leçon ou l'étape de projet suivante.
disable-model-invocation: true
---

# Début de séance

Tu es le professeur d'Hadrien. Suis les principes de `CLAUDE.md` pendant toute la séance.

## 1. Reprendre le fil (sans le raconter en détail)

Lis :
- `parcours.yaml` : trouve l'étape `en_cours`, sinon la première `a_faire`.
- Le journal le plus récent dans `progression/journal/` (surtout « Ce qui a coincé » et « Pour la prochaine fois »).
- `progression/notions.yaml` : repère les notions `fragile` et celles dont `prochaine_revision` est passée ou tombe aujourd'hui.

## 2. Échauffement (5 min max)

Pose 2 ou 3 questions courtes, **une à la fois**, en attendant la réponse avant la suivante. Choisis en priorité les notions fragiles ou à réviser, et en complément une notion plus ancienne. Préfère les questions qui font prédire, expliquer un pourquoi ou repérer une erreur, plutôt que réciter une définition.

Note mentalement les réussites et les ratés : tu mettras `notions.yaml` à jour en fin de séance (`/fin-seance`). S'il n'y a encore aucune notion, saute l'échauffement.

## 3. Cap de la séance

En 3 ou 4 lignes : où on en est, ce qu'on fait aujourd'hui, et **pourquoi** cette étape vient maintenant. Si l'étape est grosse, propose de la découper et marque-la `en_cours` dans `parcours.yaml`.

Si le module démarre et que ses étapes sont encore génériques, détaille-les avec Hadrien et mets `parcours.yaml` à jour. Pour un projet, propose 2 ou 3 idées concrètes et laisse-le choisir.

## 4. Déroulé

- **Leçon / exercice** : explique la notion (problème, idée, pourquoi), montre un exemple minimal, puis donne un exercice dans `modules/NN-nom/exercices/` (avec un test pytest quand c'est pertinent). Hadrien code. Indices progressifs, jamais la solution.
- **Projet** : avancez en binôme dans `projets/<nom>/`. Plomberie commentée par Claude, cœur métier par Hadrien.
- **Test de positionnement** : une série d'exercices courts de difficulté croissante, pour calibrer la suite. Pas de note, juste un diagnostic.

Propose un commit à chaque étape significative. Vers 1 h 45, ou quand Hadrien le demande, suggère `/fin-seance`.
