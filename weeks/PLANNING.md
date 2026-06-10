# Planification et compétences 

> Promo : Data Engineer Simplon Lyon 2026


> ⚠️ Planning indicatif au 31/05/2026


- Titre RNCP-37638 niveau 7, « expert en infrastructures de données massives ».
- 805h en centre (35h/semaine) + plus 5 mois de stage.  
- 10 phases comptées en heures. 

> Le cumul d'heures est un bon repère  (une semaine étudiant équivaut à 35h).


> Si vous avez la moindre question à la lecture de ce document, n'hésitez pas à nous les poser ! *Signé les formateurs*

## Tableau

| Semaine | Heures cumulées | Phase officielle | Contenu | Compétences techniques | Transverses |
|---|---|---|---|---|---|
| week_00 ✅ | 0 → 35h | Phase 0, prairie (0-49h) | EDA pandas | C8, C10 (n1), préfig. C2 | CT1, CT4 (n1) |
| week_01 ✅ | 35 → 70h | fin prairie (49h) puis Phase 1 | SQL : sqlite, PostgreSQL, psycopg2, pgAdmin | C8, C9, C11 (n1) | CT1, CT3, CT4 (n1) |
| week_02 🟡 | 70 → 105h | Phase 1, ETL (49-119h) | Python : syntaxe → fichiers, HTTP/API, scraping, classes, SQL | C8, C9, C10 (n1-2) | CT1, CT3, CT4 (n1-2) |
| week_03 | 105 → 140h | fin Phase 1 (119h) puis Phase 2 | Git, MERISE, nettoyage/harmonisation, RGPD (4h), numérique responsable (14h) | C4, C11 (n1) | CT2, CT5 |
| week_04 → 06 | 140 → 245h | Phase 2, data warehouse (119-217h) | modélisation étoile/flocon, ETL/ELT, OLAP/OLTP, normalisation, laïcité (4h), relation usager / ITIL (4h) | C13 à C17 (n1-2) | CT6, CT8 |
| week_07 → 10 | 245 → 350h | Phase 3, data lake (217-350h) | batch/streaming, catalogue, gouvernance, montée en capacité | C5, C6, C18 à C21 (n1) | CT5, CT9 |
| au-delà | 350h+ | Phases 4 à 7 | conception ETL/BDD/DWH/data lake, API REST, DataOps, missions d'étude | C1, C2, C3, C12 puis montée au niveau 3 | CT1 à CT9 |
| stage | Phase 8 (665h) | entreprise | missions réelles, rapport de stage | techniques selon les missions | CT1 à CT9 (n3) |
| examen | Phase 9 (70h) | certification | revue du projet, examen blanc, jour J | toutes | toutes |


- Modules réglementaires et transverses obligatoires pour la certification. 
- RGPD (4h) et numérique responsable / IA frugale (14h) en phase 1.
- Atelier technique de retour à l'emploi (21h) en phase 5.
- Laïcité et valeurs de la République (4h) et relation usager / ITIL (4h) en phase 2, cybersécurité et sécurité des données (14h) en phase 6.

## Notes

### Niveaux de maîtrise

Le référentiel gradue chaque compétence de 1 à 3. 

- niveau 1 : imiter, reproduire un exemple sur un cas guidé, avec accompagnement.
- niveau 2 : adapter, ajuster une solution connue à un contexte proche, en autonomie.
- niveau 3 : transposer, mobiliser la compétence dans un contexte nouveau ou complexe, en autonomie et en le justifiant.

> Une même compétence revient dans plusieurs phases en montant de niveau, jusqu'au niveau 3 en phase 7 et au stage.

### Compétences techniques (référentiel RNCP-37638)

- C1 : analyser l'expression d'un besoin de projet data (phase 4+).
- C2 : cartographier les données disponibles, sources, usages, métadonnées (préfigurée en EDA, formalisée phase 4+).
- C3 : concevoir un cadre technique d'exploitation des données (phase 4+).
- C4 : réaliser une veille technique et réglementaire (toutes phases, base de la routine de veille).
- C5 : planifier la réalisation d'un projet data (phase 3+).
- C6 : superviser la réalisation d'un projet data (phase 3+).
- C7 : communiquer tout au long de la réalisation du projet data (toutes phases).
- C8 : automatiser l'extraction de données depuis un service web, une page web (scraping), un fichier, une BDD, un système big data.
- C9 : développer des requêtes de type SQL d'extraction des données.
- C10 : développer des règles d'agrégation de données issues de différentes sources.
- C11 : créer une base de données dans le respect du RGPD.
- C12 : partager le jeu de données via des interfaces logicielles et programmables, API REST (phase 4+).
- C13 : modéliser la structure des données d'un entrepôt (faits et dimensions).
- C14 : créer un entrepôt de données.
- C15 : intégrer les ETL en entrée et en sortie d'un entrepôt de données.
- C16 : gérer l'entrepôt de données.
- C17 : implémenter des variations dans les dimensions de l'entrepôt (historisation).
- C18 : concevoir l'architecture du data lake.
- C19 : intégrer les composants d'infrastructure du data lake.
- C20 : gérer le catalogue des données.
- C21 : implémenter les règles de gouvernance des données.

### Compétences transverses

- CT1 : planifier le travail à effectuer, individuellement et en équipe.
- CT2 : contribuer au pilotage de l'organisation du travail individuel et collectif.
- CT3 : définir le périmètre d'un problème rencontré (démarche inductive).
- CT4 : rechercher de façon méthodique des pistes de résolution.
- CT5 : partager la solution adoptée (documentation, partage de connaissance).
- CT6 : présenter un travail réalisé en synthétisant ses résultats et sa démarche.
- CT7 : se familiariser avec les codes et la culture de son environnement professionnel.
- CT8 : interagir dans un contexte professionnel de façon respectueuse et constructive.
- CT9 : faciliter un temps de travail collectif.

> Note indicative : CT1 à CT4 sont visées dès la phase 0 (niveau 1) et la phase 1 (niveau 1-2). CT5 à CT9 ne sont cadrées avec un niveau qu'au stage (phase 8, niveau 3), mais se travaillent en continu via les projets, les restitutions et les rituels agiles.

### Sigles et abréviations

- RNCP : répertoire national des certifications professionnelles.
- FOAD : formation ouverte et à distance.
- EDA : exploratory data analysis, analyse exploratoire des données.
- SGBD : système de gestion de base de données.
- ETL : extract, transform, load. ELT : variante où la transformation se fait après le chargement.
- DWH : data warehouse, entrepôt de données.
- MERISE : méthode française de modélisation des données (conceptuel, logique, physique).
- OLTP : online transaction processing, bases orientées transactions. OLAP : online analytical processing, bases orientées analyse.
- RGPD : règlement général sur la protection des données.
- REST : style d'architecture pour les API web.
- IoT : internet of things, objets connectés.
- ITIL : référentiel de bonnes pratiques pour la gestion des services informatiques.
- SLA : service level agreement, engagement de niveau de service.
- DataOps : pratiques d'automatisation et de collaboration sur les flux de données.
- TRE : technique de recherche d'emploi.
