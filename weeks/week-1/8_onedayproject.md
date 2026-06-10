# One day project

## Les données

> Les jeux DataNova sont plats mais reliés entre eux par des clés métier (code INSEE ↔ code postal ↔ commune).

Objectif : partir de CSV dénormalisés et reconstruire un schéma relationnel propre.

**Utilisez au moins deux jeux de données.**

- Base officielle des codes postaux (laposte_hexasmal) (🔴 obligatoire)
    - Colonnes type : Code_commune_INSEE, Nom_commune, Code_postal, Libelle_acheminement, coordonnees_gps.
    - Point clé : un code INSEE peut avoir plusieurs codes postaux et inversement, c'est une table de jonction naturelle N-N.
- Points de contact du réseau La Poste (bureaux, agences, relais) (🟡 au choix)
    - Colonnes type : nom, adresse, commune, lat/lon, et selon la version les services offerts.
    - Relations 1-N (horaires) et N-N (services).
- Un autre jeu de données (🟡 au choix) qui :
    - utilise le code INSEE ou le code postal (ou les coordonnées GPS) comme clé étrangère
    - permet idéalement de faire des requêtes analytiques intéressantes (🟢 non obligatoire)
- Optionnel, si vous avez le temps : un jeu INSEE externe (population par commune), à joindre sur le code INSEE.

## Étapes (indicatives, pas obligatoires)

Les étapes et temps indiqués sont seulement indicatifs.

- Étape 0 : profiling (~45 min). Téléchargement et exploration sous pandas : types, doublons, valeurs manquantes, repérage des clés candidates. Comprenez les données avant de modéliser.
- Étape 1 : modélisation (~1h) sur papier ou dbdiagram.io : entités, cardinalités, choix entre clés naturelles et clés de substitution. C'est là que se joue tout le raisonnement sur les clés étrangères.
- Étape 2 : DDL, Data Definition Language (~1h). Écrivez les CREATE TABLE avec leurs contraintes (PRIMARY KEY, FOREIGN KEY ... REFERENCES, NOT NULL, CHECK). C'est l'étape « recréer la base ».
- Étape 3 : ETL et chargement (~1h30 à 2h). Nettoyez sous pandas, dédupliquez les dimensions avant insertion, chargez dans Postgres en respectant l'ordre des FK.
- Étape 4 : requêtes analytiques (~1h30 à 2h). Voir la section ci-dessous.

## Exemples de requêtes analytiques

1. Communes ayant plusieurs codes postaux.
2. Bureaux situés dans des communes au-dessus de la population moyenne nationale.
3. Communes sans aucun bureau de poste.
4. Pour chaque département, le bureau offrant le plus de services.
5. Bureaux offrant tous les services d'une liste donnée.

### Pièges à anticiper

- Zéros initiaux : lus en entier, les codes INSEE et postaux perdent leur zéro de tête (01000 devient 1000). Forcez dtype=str au read_csv.
- Séparateur ; et encodage (souvent UTF-8, parfois latin-1) dans les CSV DataNova.
- coordonnees_gps est souvent dans une seule colonne "lat,lon" à découper.
- CEDEX : certains codes postaux cassent le modèle simple, bon sujet de discussion sur les limites d'un schéma.
- Pré-filtrez sur un ou deux départements pour garder des volumes raisonnables et des chargements rapides.


### Google Drive

- [Tableau d'avancement](https://docs.google.com/spreadsheets/d/1lBXXA_Rg8RtSsr4cNpcJRodVUR0zVJ-xHC5INXpgzEI/edit?gid=0#gid=0)
- [Rendus (intermédiaires au 30/05/2026)](https://drive.google.com/drive/folders/1rwxlyc5PywdaDnn44X6t9-poFYYFG20Z)
