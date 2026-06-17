# Brief RGPD : modéliser une fonctionnalité et rédiger ses mentions légales

> Module réglementaire obligatoire (compétence C11, niveau 1 : créer une base de données dans le respect du RGPD).

En partant d'un site marchand français, vous reconstituerez le travail de conception derrière une de ses fonctionnalités : 
- le schéma de données
- l'analyse des données personnelles
- les mentions légales associées

> Compétence visée (RNCP-37638) : **C11, niveau 1-2** : « créer une base de données dans le respect du RGPD en élaborant les modèles conceptuels et physiques des données à partir des données préparées et en programmant leur import afin de stocker le jeu de données du projet ». Niveau 1 : cas guidé, avec accompagnement.

## Situation professionnelle emblématique

- Vous êtes data engineer dans une agence qui réalise des sites marchands.
- Un client vous confie la conception de la base d'une fonctionnalité de son futur site marchand. 
- Avant d'écrire la moindre ligne de SQL, on attend deux choses de vous : un modèle de données qui tient la fonctionnalité, et une analyse RGPD qui dit ce qui relève de la donnée personnelle et comment le site doit informer ses utilisateurs.

Le délégué à la protection des données (DPO) du client vous demande de documenter vos choix : ce dossier servira au registre des traitements et aux mentions légales publiées sur le site. 

**⚠️ La conformité se construit à la modélisation et se justifie par écrit.**

## 1. Choisir un site

Un site qui valide les deux conditions :

- **français** : éditeur établi en France, soumis au droit français et au RGPD ;
- **marchand** : il vend un produit ou un service en ligne (e-commerce, réservation, abonnement, place de marché…).

## 2. Choisir une fonctionnalité et la modéliser

Prenez **une** fonctionnalité précise, pas le site entier. Quelques exemples : la création de compte, le panier et la commande, l'avis client, la liste de souhaits, la réservation d'un créneau, le programme de fidélité, l'abonnement à la newsletter etc...

Pour cette fonctionnalité :

- imaginez le **schéma SQL** représentant les données nécessaires à son bon fonctionnement, et rien de plus. Vous appliquer principe de minimisation : une colonne qu'on ne sait pas justifier ne se crée pas.
- livrez-le en MCD (Mermaid `erDiagram` ou crow's foot) **et** en `CREATE TABLE` PostgreSQL, avec clés primaires, clés étrangères et contraintes (`NOT NULL`, `UNIQUE`, au moins un `CHECK`).

- [Crow's foot](https://www.drawio.com/docs/tutorials/crows-foot-notation/)
- [Entity Relationships](https://www.drawio.com/docs/diagram-types/entity-relationship-tables/)

Trois ou quatre tables liées suffisent. Par exemple pour un site de e-commerce : `client`, `commande`, `ligne_commande`, `produit`.

## 3. Identifier les données personnelles

- Reprenez votre schéma colonne par colonne : pour chaque donnée, dites si elle est personnelle et pourquoi. 
- Rappel de l'article 4 du RGPD : est personnelle toute information se rapportant à une personne physique **identifiable**, directement ou indirectement.

*⚠️ Le coeur de l'exercice, c'est l'**indirect** : listez les données et surtout les **combinaisons de données** qui, croisées, permettent de remonter à une personne, même sans son nom.*

- une donnée seule : email, téléphone, adresse de livraison, numéro client ;
- une combinaison : code postal + date de naissance + sexe suffit à ré-identifier une part importante de la population ; historique d'achats + horaires de connexion + ville ; adresse IP + horodatage etc...

Présentez ça en tableau : `donnée | personnelle ? | directe / indirecte | justification (base légale)`. Et une ligne par combinaison ré-identifiante repérée.

> Piège à ne pas rater : une donnée « anonyme » en apparence (un identifiant interne, un code postal) cesse de l'être dès qu'on peut la recouper. 

## 4. Rédiger une ébauche de mentions légales

Rédigez les mentions légales du site, en veillant à n'**oublier aucune mention obligatoire**. Le cas d'un site marchand français cumule trois sources : la LCEN (article 6), le Code de commerce, et le RGPD. La checklist de contrôle :

**Identification de l'éditeur**
- raison sociale et forme juridique (SARL, SAS…), montant du capital social ;
- adresse du siège social ;
- numéro RCS et ville d'immatriculation, numéro SIRET ;
- numéro de TVA intracommunautaire ;
- coordonnées de contact (email, téléphone) ;
- nom du directeur de la publication.

**Hébergeur**
- nom (ou raison sociale), adresse et téléphone de l'hébergeur du site.

**Activité commerciale (B2C)**
- renvoi aux conditions générales de vente ;
- information sur le médiateur de la consommation (obligatoire pour la vente aux particuliers).
- tout autre médiateur ou mention obligatoire pour les professions réglementées.

**Protection des données (RGPD)**
- identité du responsable de traitement, et du DPO s'il existe ;
- finalités et base légale du traitement ;
- durée de conservation des données ;
- droits des personnes : accès, rectification, effacement, opposition, portabilité, limitation ;
- droit d'introduire une réclamation auprès de la CNIL ;
- information sur les cookies et le recueil du consentement.

🟠 Vous veillerez à bien indiquer quels sont les délais de conservation des données, qui peut être variable.

**Propriété intellectuelle**
- mention sur les droits relatifs aux contenus du site.

Une ébauche réaliste : remplissez avec des valeurs plausibles (ou les vraies, si le site les publie) plutôt que des `[à compléter]` partout. **Le but est de montrer que vous savez quelles mentions sont dues et pourquoi.**


## 5. Concevoir le process de suppression en cas d'invocation du droit à l'effacement


Rédiger la liste des instructions à suivre dans le cas où un utilisateur ferait valoir son droit à l'effacement. 


## Livrables

| Livrable | Forme |
|---|---|
| Le site choisi et la fonctionnalité, en deux lignes | dans le `.md` |
| Le schéma de la fonctionnalité | MCD (Mermaid) + `CREATE TABLE` |
| L'analyse des données personnelles | tableau données + tableau combinaisons ré-identifiantes |
| L'ébauche de mentions légales | section rédigée, checklist couverte |

Un seul fichier Markdown versionné dans le dépôt + éventuelles images ou fichiers pour le schéma SQL.

## Indicateurs de performance

Ce qui sera regardé pour valider la compétence :

- le MCD et les `CREATE TABLE` sont cohérents entre eux et couvrent la fonctionnalité choisie, sans table ni colonne superflue ;
- les contraintes d'intégrité sont posées et pertinentes (clés primaires, clés étrangères, `NOT NULL`, `UNIQUE`, au moins un `CHECK` justifié) ;
- la minimisation est appliquée : chaque colonne se rattache à la finalité, et les colonnes écartées sont justifiées ;
- l'analyse des données personnelles distingue identification directe et indirecte, et repère au moins une combinaison ré-identifiante propre au schéma ;
- les mentions légales couvrent l'intégralité de la checklist (éditeur, hébergeur, activité commerciale, RGPD, propriété intellectuelle), sans mention obligatoire manquante ;
- le volet RGPD est complet et exact : finalité, base légale, durée de conservation, droits des personnes, réclamation CNIL, cookies.


## Modalités pédagogiques

- Module réglementaire en présentiel, intégré aux 4h RGPD de la phase 1. 
- Travail en binôme, en autonomie accompagnée : le formateur passe valider le choix du site et de la fonctionnalité avant la modélisation. 
- Durée indicative : une demi-journée.
- 🔴 Aucun usage de LLM ne sera toléré pour ce brief.
- 🟠 Il est préférable de ne pas s'inspirer des mentions légales du site que vous choisirez.

## Modalités d'évaluation

Le travail est rendu sous forme de commit git. Un barème simple suit les indicateurs de performance ci-dessus : modèle (cohérence et minimisation), analyse des données personnelles (justesse et combinaisons), mentions légales (exhaustivité). Une courte restitution orale (5 minutes) peut être demandée pour défendre les arbitrages RGPD. 




