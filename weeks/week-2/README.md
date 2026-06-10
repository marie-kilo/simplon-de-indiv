# Semaine 02 : Python

Cette semaine, on apprend Python depuis le début, jusqu'à aller chercher des données sur le web et dans une base SQL. C'est la brique qui sert à automatiser la collecte de données, au cœur du métier de data engineer.

## Comment ça marche

Chaque TP est un notebook unique qui contient le cours et les énoncés des exercices. Les cellules de code marquées `# À toi de jouer` sont à compléter par vous. Les corrigés sont rangés à part dans le dossier `corrections/`, un notebook par exercice. Essayez d'abord, regardez le corrigé ensuite.

## Les TP et leurs objectifs

| TP | Notebook | Objectif | Importance |
|---|---|---|---|
| 1 | `tp_01_syntaxe_variables_et_types.ipynb` | Écrire ses premières lignes : variables, types, listes, dictionnaires | Important |
| 2 | `tp_02_tests_boucles_fonctions.ipynb` | Contrôler le programme : conditions, boucles, fonctions | Important |
| 3 | `tp_03_algorithmie.ipynb` | Résoudre des problèmes : chaînes, statistiques, dates, dictionnaires | Important |
| 4 | `tp_04_fichiers.ipynb` | Lire et écrire des fichiers sur le disque | Important |
| 5 | `tp_05_http_api.ipynb` | Récupérer des données depuis le web avec des requêtes HTTP et des API | Important |
| 6 | `tp_06_webscraping_bs.ipynb` | Extraire des données d'une page web avec BeautifulSoup | Important |
| 7 | `tp_07_classes.ipynb` | Structurer son code avec des classes (programmation orientée objet) | Facultatif |
| 8 | `tp_08_wrap_up_monty_hall.ipynb` | Mettre tout en pratique sur un problème complet | Facultatif |
| 9 | `tp_09_algorithmie_avancee.ipynb` | Aller plus loin : efficacité et complexité d'un algorithme | Facultatif |
| 10 | `tp_10_sql.ipynb` | Faire dialoguer Python et une base de données SQL | Important |

À l'intérieur d'un TP, certains exercices peuvent eux aussi être marqués « facultatif » (par exemple le Seigneur des Anneaux au TP 5, qui demande une clé d'API gratuite).

## À savoir avant de lancer le TP 10

Le TP 10 se connecte à deux bases de données.

- SQLite (locale, rien à installer) : les exercices écrivent dans `data/tp_10/tp_10_exo_1.db`, déjà présente.
- PostgreSQL (local, déjà installé sur vos postes) : la connexion utilisée est `postgresql://postgres:postgres@localhost:5432/postgres`. Adaptez l'utilisateur, le mot de passe et la base selon votre installation.

## Clé d'API pour les exercices Le Seigneur des Anneaux

Les exercices qui utilisent l'API the-one-api (TP 5 facultatif et TP 10 exercice 1) demandent votre propre clé. Créez un compte gratuit sur [the-one-api.dev](https://the-one-api.dev/sign-up), puis remplacez `TA_CLE_API` par votre clé dans le code.

## Les projets

Deux projets d'application, à faire une fois les TP vus.

- `smallproject/` : un projet guidé qui combine scraping, classes et SQL (récupérer des données sur le web et les stocker en base avec des clés étrangères). Énoncé dans `smallproject/docs/README.md`.
- `activeproject/` : un projet de révision de la week01 (SQL) et de la week02 (Python), en deux briefs indépendants sur de l'open data de mobilité. Énoncé dans `activeproject/README.md`.
