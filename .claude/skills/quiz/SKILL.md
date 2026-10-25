---
name: quiz
description: Quiz de révision de 10 à 30 min (répétition espacée) sur les notions vues, pour les jours sans séance. Met à jour les niveaux de maîtrise.
disable-model-invocation: true
argument-hint: "[durée en minutes ou thème, optionnel]"
---

# Quiz de révision

Hadrien veut réviser hors séance. Durée ou thème éventuel : $ARGUMENTS (sinon, vise environ 15 min, soit 8 à 10 questions).

## 1. Choisir les questions

Lis `progression/notions.yaml` et les fiches associées dans `fiches/`. Ordre de priorité :
1. Les notions dont `prochaine_revision` est passée ou tombe aujourd'hui.
2. Les notions `fragile`.
3. Les notions `en_cours`.
4. Quelques notions `acquis`, pour vérifier qu'elles tiennent.

Si un thème est demandé, filtre dessus. S'il n'y a aucune notion, dis-le simplement et propose plutôt de relire une fiche.

## 2. Poser les questions

- **Une question à la fois.** Attends la réponse avant de passer à la suivante.
- Varie les formats : prédire ce qu'affiche un bout de code, trouver le bug, expliquer un « pourquoi », choisir entre deux approches, écrire une ligne de code ou de commande.
- Après chaque réponse : dis si c'est juste, corrige en une ou deux phrases et renvoie vers la fiche si besoin. Pas de cours : c'est un quiz.
- Annonce la progression (« question 3/8 »).

## 3. Clôturer

- Bilan court : ce qui est solide, ce qui reste fragile.
- Mets à jour `progression/notions.yaml` selon les règles de répétition espacée de `CLAUDE.md` : `maitrise` et `prochaine_revision`. Ajoute `derniere_revision` avec la date du jour.
- Propose de committer la mise à jour (`git add progression/notions.yaml && git commit -m "Quiz du AAAA-MM-JJ"`).
