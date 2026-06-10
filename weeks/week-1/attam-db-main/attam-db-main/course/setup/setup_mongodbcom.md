

# Créer un cluster sur MongoDB.com


## Créer un compte [MongoDB.com](https://www.mongodb.com/fr-fr)

## Ensuite, après la vérification d'email : 

### Premier formulaire (préférences utilisateur)

**(pas très important, mais augmente les chances d'avoir les mêmes interfaces pendant le cours)**

![MongoDB](../images/mongodb_first_form.png)

### Second formulaire (création du cluster)

#### Choisir : 

- Deploy your database: **M0 Free**
- Provider : **AWS**
- Region : **Paris (EU West)**
- Name : **Cluster0**


![MongoDB](../images/mongodb_second_form.png)




### Troisième formulaire (sécurité)

#### Choisir : 

- Authentification avec username et password **Penser à sauvegarder le mot de passe**
    - Créer un fichier `.env` à la racine de votre dossier avec le contenu des variables `user` et `password` : 
    ```
    MONGO_DB_USER=<user>
    MONGO_DB_PASSWORD=<pass>
    ```

![MongoDB](../images/mongodb_third_form_1.png)


- Se connecter depuis sa machine : ajouter son IP à la whitelist


![MongoDB](../images/mongodb_third_form_2.png)

