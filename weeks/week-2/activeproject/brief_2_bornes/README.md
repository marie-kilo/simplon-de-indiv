# Brief 2 : maillage des bornes de recharge électrique

> Une collectivité veut cibler ses prochaines installations de bornes, là où le réseau est trop faible.

Objectif : croiser le nombre de bornes avec la population et pointer les départements sous-équipés.

## La question métier

Quels départements comptent le moins de bornes par habitant ? Quel opérateur domine sur un territoire ?

## Les données

Deux sources à croiser.

- Bornes de recharge, open data IRVE (🔴 obligatoire, fichier CSV)
    - Dataset : `https://www.data.gouv.fr/fr/datasets/5448d3e0c751df01f85d0572/`
    - Récupérez l'URL du CSV consolidé le plus récent via l'API : `https://www.data.gouv.fr/api/1/datasets/5448d3e0c751df01f85d0572/`, champ `resources`.
    - Champs utiles : `nom_operateur`, `code_insee_commune`, `consolidated_commune`, `puissance_nominale`.
    - Point clé : le code du département, c'est les deux premiers caractères du code INSEE de la commune.
- Population par département, à scraper (🔴 obligatoire, page web)
    - `https://fr.wikipedia.org/wiki/Liste_des_départements_français_classés_par_population_et_superficie`
    - C'est une table de classe `wikitable`. Point clé : les deux premières lignes sont des entêtes, ensuite chaque ligne donne le code, le nom, puis la population par année.

## Le modèle attendu

Deux tables liées par une clé étrangère :

- `departement` : code (clé primaire), nom, population.
- `borne` : un id auto-incrémenté, opérateur, code du département (clé étrangère vers `departement`), commune, puissance.

## Étapes (indicatives)

- Étape 1 : scraper la population (BeautifulSoup), lire le CSV des bornes (module `csv`). Filtrez sur quelques départements pour des volumes raisonnables.
- Étape 2 : `CREATE TABLE` departement et borne avec la clé étrangère.
- Étape 3 : insérer d'abord les départements, puis les bornes.
- Étape 4 : requêtes analytiques.

## Exemples de requêtes analytiques

1. Le nombre de bornes pour 100 000 habitants, par département, du mieux au moins équipé.
2. Les départements les plus sous-équipés.
3. L'opérateur dominant dans un département donné.

## Pièges à anticiper

- Zéros initiaux : un code de département se lit en texte, pas en entier (sinon `01` devient `1`).
- Les nombres de population sur Wikipedia contiennent des espaces insécables (`\xa0`) à retirer avant de convertir en entier.
- Encodage et séparateur du CSV : vérifiez-les avant de parser.
- Choisissez la bonne colonne de population (l'année la plus récente).
- Respectez l'ordre d'insertion imposé par la clé étrangère.
