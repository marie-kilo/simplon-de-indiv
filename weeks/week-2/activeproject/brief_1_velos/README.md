# Brief 1 : disponibilité des vélos en libre-service

> La collectivité veut un tableau de bord de la disponibilité des vélos. Avant le tableau de bord, il faut la base qui l'alimente.

Objectif : collecter les données Vélib' en temps réel, les structurer en deux tables liées, et répondre à une première question métier.

## La question métier

Quelles stations sont régulièrement saturées ou vides ?

## Les données

API GBFS de Vélib' Métropole, ouverte et sans clé. Dans chaque fichier, les stations sont dans `data["stations"]`.

- Informations stables des stations (🔴 obligatoire)
    - `https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json`
    - Champs utiles : `station_id`, `stationCode`, `name`, `lat`, `lon`, `capacity`.
- État temps réel (🔴 obligatoire)
    - `https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_status.json`
    - Champs utiles : `station_id`, `num_bikes_available`, `num_docks_available`.
    - Point clé : les deux fichiers se relient par `station_id`.

## Le modèle attendu

Deux tables liées par une clé étrangère :

- `station` : `station_id` (clé primaire), code, nom, latitude, longitude, capacité.
- `releve` : un id auto-incrémenté, `station_id` (clé étrangère vers `station`), vélos disponibles, bornes disponibles.

> Une station a plusieurs relevés dans le temps : c'est une relation un-à-plusieurs.

## Étapes (indicatives)

- Étape 1 : requête `GET` sur les deux endpoints, récupérer le JSON.
- Étape 2 : `CREATE TABLE` station et releve avec la clé étrangère.
- Étape 3 : insérer d'abord les stations, puis un relevé par station.
- Étape 4 : requêtes analytiques.

## Exemples de requêtes analytiques

1. Les stations les plus vides et les plus pleines (avec leur nom, donc avec une jointure).
2. Le taux de disponibilité moyen (vélos rapportés à la capacité).
3. Les stations de grande capacité.

## Pour aller plus loin (🟢 optionnel)

- Relancez la collecte plusieurs fois à quelques minutes d'intervalle pour empiler des relevés et observer l'évolution.
- Reprenez le découpage en classes du `smallproject` (un collecteur d'API, un chargeur de base).

## Pièges à anticiper

- Une station présente dans le statut peut manquer dans les informations (ou l'inverse) : filtrez sur les `station_id` connus.
- L'API est en temps réel : deux exécutions donnent des chiffres différents, c'est normal.
