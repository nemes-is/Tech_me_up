---
name: fin-seance
description: Clôture une séance d'apprentissage - écrit le journal, crée les fiches mémo et la leçon, met à jour la progression, puis propose le commit et le push.
disable-model-invocation: true
---

# Fin de séance

Récapitule la séance qui vient d'avoir lieu dans cette conversation, puis mets à jour les fichiers du parcours. Les formats sont décrits dans `CLAUDE.md`.

## 1. Journal

Crée `progression/journal/AAAA-MM-JJ.md` avec la date du jour. Si le fichier existe déjà (deux séances le même jour), ajoute un suffixe : `AAAA-MM-JJ-2.md`. Contenu : en-tête YAML (`date`, `titre`, `duree`, `module`), puis les sections *Fait*, *Ce qui a coincé*, *Pour la prochaine fois*. Sois honnête sur ce qui a coincé : c'est ce qui guidera la prochaine séance.

## 2. Leçon écrite

Si une notion a été enseignée, écris ou complète la leçon dans `modules/NN-nom/lecons/` : une version propre et relisible de l'explication donnée en séance, avec les exemples. Pas besoin de tout retranscrire.

## 3. Fiches mémo

Pour chaque concept important de la séance, crée ou mets à jour une fiche dans `fiches/<slug>.md`. Elle doit être courte, centrée sur le pourquoi, et suivre la structure *Le problème / L'idée / En pratique / Pourquoi c'est comme ça / Pièges*. Inutile de faire une fiche pour un détail.

## 4. Progression

- `parcours.yaml` : passe les étapes terminées à `fait` et l'étape commencée à `en_cours`.
- `progression/notions.yaml` : ajoute les nouvelles notions (`maitrise: fragile` en général, `prochaine_revision` = demain) et mets à jour celles révisées à l'échauffement selon les règles de `CLAUDE.md`.

## 5. Sauvegarde

Montre un résumé des fichiers modifiés, puis guide Hadrien pour le commit et le push. **C'est lui qui tape les commandes Git** tant qu'elles ne sont pas acquises :

```bash
git status
git add .
git commit -m "Séance du AAAA-MM-JJ : <sujet>"
git push
```

Termine par une phrase sur ce qui l'attend à la prochaine séance, et rappelle que `/quiz` est disponible les jours off.
