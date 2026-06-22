# Mini brief : implémenter le droit à l'effacement

> Suite du brief RGPD. Vous y aviez conçu le schéma et décrit, sur le papier, la procédure de suppression. Ici vous la **codez** : base réelle, données d'exemple, script Python qui efface.

L'article 17 du RGPD donne à toute personne le droit d'obtenir l'effacement de ses données. Techniquement, c'est une suite de `DELETE` (ou d'anonymisations via `UPDATE` ou autre) à mener dans le bon ordre sans casser l'intégrité de la base.

> Compétence visée (RNCP-37638) : **C11, niveau 1-2** : « créer une base de données dans le respect du RGPD [...] en programmant leur import ». 


## Situation professionnelle emblématique

- Le DPO du client vous transmet une demande d'effacement reçue par mail : « le client n° 42 souhaite que vous supprimiez ses données ».
- Vous devez exécuter cette demande de façon **fiable et reproductible** : un script (et pas pas dix `DELETE` tapés à la main en production 🙃). 
- Piège métier : certaines données ne peuvent pas être supprimées (une facture doit être conservée pour l'obligation comptable). Dans ce cas, on **anonymise** au lieu de supprimer.

**⚠️ Un effacement mal ordonné viole les clés étrangères ou laisse des données orphelines. L'ordre des suppressions fait partie du travail.**

## Ce qu'on attend

### 1. Créer la base

- Reprenez le **schéma de votre brief RGPD** (par exemple `client`, `commande`, `ligne_commande`, `produit`).
- Écrivez les `CREATE TABLE` avec leurs clés primaires et **clés étrangères** : c'est ce qui rend l'ordre de suppression contraignant.

### 2. Injecter quelques lignes d'exemple

- Quelques clients, quelques commandes rattachées, de quoi avoir un cas réaliste : un client qui a passé des commandes, un autre non.
- Quelques dizaines de lignes suffisent. Le but est de pouvoir vérifier l'avant / après, pas de faire du volume.

### 3. Coder la procédure d'effacement en Python

- Une fonction `effacer_client(conn, client_id)` qui supprime (ou anonymise) toutes les données personnelles rattachées à ce client.
- Respect des clés étrangères : supprimez **du côté `n` vers le côté `1`** (les `ligne_commande` avant les `commande`, les `commande` avant le `client`), ou bien posez vos clés étrangères en `ON DELETE CASCADE` et assumez ce choix.
- Tout dans **une seule transaction** : soit tout s'efface, soit rien (un `commit` final, un `rollback` en cas d'erreur).
- 🟠 Traitez au moins un cas d'**anonymisation** plutôt que de suppression (par exemple : on garde la commande pour la comptabilité, mais on remplace le nom et l'email du client par une valeur neutre).

### 4. Vérifier

- Un `SELECT count(*)` avant et après sur chaque table concernée.
- Une vérification qu'**aucune donnée orpheline** ne subsiste (pas de commande pointant vers un client supprimé).
- Un message clair en sortie : ce qui a été supprimé, ce qui a été anonymisé.

## Livrables

| Livrable | Forme |
|---|---|
| Le schéma SQL (`CREATE TABLE` avec FK) | `.sql` ou dans le script |
| Le jeu de lignes d'exemple | script d'insertion |
| La procédure `effacer_client` | fonction Python (psycopg2) |
| La vérification avant / après | sortie du script ou notebook |

Un script Python exécutable, versionné dans le dépôt.

## Indicateurs de performance

- la base est créée avec des clés étrangères réelles, et les lignes d'exemple sont cohérentes ;
- la procédure efface **toutes** les données personnelles du client visé, et **seulement** les siennes ;
- l'ordre de suppression respecte l'intégrité référentielle (ou le `CASCADE` est assumé et expliqué) ;
- l'opération est transactionnelle : pas d'état intermédiaire incohérent en cas d'erreur ;
- au moins un cas d'anonymisation est traité et justifié (donnée à conservation obligatoire) ;
- la vérification avant / après prouve l'absence de donnée orpheline.

## Modalités pédagogiques

- TP technique court, en prolongement direct du brief RGPD et du module RGPD.
- Travail individuel ou en groupe, en autonomie accompagnée.
- Prérequis : `psycopg2`, `CREATE TABLE` et clés étrangères, le schéma de votre brief RGPD.
- Durée indicative : une journée max.
- 🔴 Aucun usage de LLM pour produire le code de la procédure.

## Modalités d'évaluation

- Rendu sous forme de commits git dans vos repos `simplon-de-indiv`.
- Barème sur les indicateurs ci-dessus : justesse de l'effacement, respect de l'intégrité, transaction, traitement de l'anonymisation, vérification.
