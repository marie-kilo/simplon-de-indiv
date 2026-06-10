# activeproject

> Projet de révision en situation : on repasse tout le SQL (week01) et tout le Python (week02), sur une vraie problématique métier et de l'open data.

Objectif : à partir de données ouvertes, construire des bases de données propres (avec clés étrangères) et répondre à des questions métier concrètes.

## Le contexte

Vous êtes alternant·e data engineer dans une agence qui accompagne les collectivités sur la mobilité durable. Deux missions indépendantes vous sont confiées.

## Les deux briefs

> Les deux briefs sont indépendants : le brief 2 ne réutilise rien du brief 1. Faites-les dans l'ordre ou en parallèle.

- `brief_1_velos/` (🔴 obligatoire) : suivre la disponibilité des vélos en libre-service, à partir d'une API temps réel.
- `brief_2_bornes/` (🔴 obligatoire) : repérer les départements sous-équipés en bornes de recharge, en croisant un fichier open data et une page web.

Chaque brief a son énoncé dans son `README.md`.

## Ce que vous révisez

- Requêtes HTTP et API JSON (TP5), lecture de fichiers (TP4), scraping (TP6), classes (TP7, smallproject)
- Modélisation SQL, clés étrangères, jointures et requêtes analytiques (week01, TP10)
- SQL depuis Python (TP10)

> Pas besoin de pandas : `requests`, `csv` et `sqlite3` suffisent.

## Étapes (indicatives, pas obligatoires)

- Étape 0 : exploration (~30 min). Regardez les champs de la source avant de modéliser.
- Étape 1 : modélisation (~45 min) sur papier ou sur dbdiagram.io : deux tables, leurs colonnes, la clé étrangère.
- Étape 2 : DDL (~30 min). Écrivez les `CREATE TABLE` avec leurs contraintes (`PRIMARY KEY`, `FOREIGN KEY`).
- Étape 3 : collecte et chargement (~1h30). Récupérez les données en Python et insérez-les (la table référencée d'abord).
- Étape 4 : requêtes analytiques (~1h). Répondez à la question métier du brief.

## Livrables

- Le code de collecte et de chargement.
- La base de données (SQLite suffit, PostgreSQL local si vous voulez).
- Les requêtes analytiques et leurs résultats.
- Un court texte qui répond à la question métier.

> Les corrigés sont dans `corriges/`, dossier non versionné. Demandez-les au formateur.
