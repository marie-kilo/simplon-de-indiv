# Proposition de programme : week03 à week07

État au 31/05/2026. La promo a vu pandas (week00), le SQL (week01) et Python (week02). On est à 105h cumulées. La phase 1 du référentiel (ETL) se termine vers 119h, la phase 2 (data warehouse) court jusqu'à 217h, la phase 3 (data lake) démarre ensuite.

## Principes directeurs

- Pédagogie active. Chaque semaine est portée par une situation professionnelle, sur le modèle des exemples du référentiel. Peu de cours descendant, on apprend en produisant un livrable.
- Outils open source d'abord. PostgreSQL, pandas, dbt, Spark, MongoDB, Docker, Airflow couvrent tout le référentiel sans coût. Talend, Databricks et la stack Azure sont payants, on les montre en survol pour la culture et parce que la certification les cite, sans construire les briefs dessus.
- Modules réglementaires placés là où le référentiel les rattache, en format atelier plus veille plutôt qu'en cours bloc.
- Différenciation. Le niveau de la promo est hétérogène, chaque brief a un socle commun et des extensions pour les plus rapides.

## Week 03 : pandas pour le nettoyage, clôture de la phase 1

Situation : on confie à l'apprenant des extractions sales issues de plusieurs SI métier. Il doit les harmoniser en un jeu de données propre, documenté, et le charger en base.

Retour à pandas, orienté ETL et non EDA :

- lecture multi-sources (CSV, Excel, JSON, SQL), gestion des types, parsing des dates et des unités
- valeurs manquantes, doublons, entrées corrompues, homogénéisation des formats (C10)
- `merge`, `concat`, `groupby`, `pivot` et `melt`, puis export propre avec `to_sql`
- modélisation relationnelle MERISE (MCD, MLD, cardinalités) pour préparer l'entrepôt

Modules de la phase 1 : RGPD (4h) et numérique responsable, IA frugale (14h).

Compétences visées : C10 niveau 2, C11 niveau 1 à 2, C4.

## Week 04 : Git intensif, démarrage de l'entrepôt

Situation : une équipe doit collaborer sur un même dépôt pour construire un premier datamart des ventes.

- Git avec `git_step_by_step`, qui couvre tout le socle : créer un dépôt distant et local, la routine status, add, commit, push, créer une branche, fusionner dans `master`. C'est le bon niveau pour la promo, et c'est aussi du CT1 et du CT2, et le versionnement attendu en phase 1.
- Démarrage de la phase 2 : OLTP contre OLAP, l'intérêt d'un entrepôt, modélisation dimensionnelle (faits et dimensions), schéma en étoile contre flocon.

Compétences visées : C13 niveau 1, CT1 et CT2 niveau 1 à 2, C7.

## Week 05 : Git suite, ETL et ELT vers l'entrepôt, dbt

Situation : intégrer un nouveau jeu de données, ou un nouveau pays, au datamart existant. C'est un exemple direct du référentiel de la phase 2.

- Git en collaboration, au-delà du tutoriel : cloner un dépôt partagé, `fetch` et `pull`, gérer un conflit de merge, les pull requests et la revue de code, le `.gitignore`. Le `rebase` en bonus pour les plus à l'aise. Consolidation par la pratique sur le projet de la semaine.
- ETL et ELT : alimenter l'entrepôt, charger les dimensions puis les faits dans le bon ordre, historiser les dimensions (SCD type 1 et 2, C17).
- dbt en introduction : transformations versionnées, models, tests. pandas reste le moteur de transformation en amont.

Modules de la phase 2 : laïcité et valeurs de la République (4h), relation usager et client, ITIL (4h).

Compétences visées : C14 niveau 1 à 2, C15 niveau 1 à 2, C17 niveau 1.

## Week 06 : entrepôt complet, orchestration, projet de synthèse phase 2

Situation : concevoir et alimenter un data warehouse pour un client, et répondre à ses besoins analytiques. Gros livrable de la phase 2, sur plusieurs jours.

- normalisation et formes normales, OLAP, notions de cubes et d'hypercubes
- orchestration légère : cron, puis introduction d'Airflow ou Dagster pour automatiser le pipeline
- qualité et maintenance : tests dbt, monitoring simple, notion de SLA en lien avec ITIL

Compétences visées : C13 à C16 niveau 2, C17 niveau 1 à 2, C5 niveau 1.

## Week 07 : démarrage data lake, big data, Docker

Situation : ingérer des données massives et non structurées (logs, capteurs IoT) dans un data lake. Exemple direct du référentiel de la phase 3.

- phase 3 : l'intérêt d'un data lake face à un entrepôt, architecture, batch contre streaming, catalogue de données, gouvernance et RGPD appliqué
- outils big data en prise en main : PySpark (traitement distribué), MongoDB (non structuré), Docker (reproduire l'environnement)

Compétences visées : C18 niveau 1, C19 niveau 1, C20 niveau 1.

## Le retour à pandas

pandas n'est pas cantonné à la week03. Il reste le moteur de transformation des semaines 04 à 06, en amont du chargement et de dbt, donc la promo le pratique en continu.

## Git

Git est concentré sur les semaines 04 et 05. La week04 suit `git_step_by_step` pour le socle (dépôt, commits, branches, merge), la week05 va au-delà avec la collaboration (conflits, pull, pull requests). Ensuite Git reste un réflexe imposé sur tous les projets : chaque rendu passe par une pull request.

## Couverture de la certification

Sur ces cinq semaines, on termine la phase 1 (C8 à C11 au niveau 2), on couvre l'essentiel de la phase 2 (C13 à C17 niveau 1 à 2), on amorce la phase 3 (C18 à C21 niveau 1), et on traite tous les modules réglementaires des phases 1 et 2. Les transverses CT1, CT2, CT5 et CT6 montent via le travail Git en équipe et les restitutions de projet.
