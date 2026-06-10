# Installer MongoDB sur Linux


## Installer MongoDB


```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

sudo apt-get update

sudo apt-get install -y mongodb-org
```

## Lancer MongoDB

```bash
sudo systemctl start mongod
```


## Vérifier l'état de MongoDB

```bash
sudo systemctl start mongod
```


# Installer MongoDB sur Mac

### Installer et mettre à jour Homebrew


```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

brew update
```


### Installer MongoDB
```bash
brew tap mongodb/brew
brew install mongodb-community@4.4
```


## Démarrer MongoDB
```bash
brew services start mongodb/brew/mongodb-community
```


# Installer MongoDB sur Windows (11/2023) 

Suivre le [tutoriel officiel](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/).


# Installer MongoDB sur Windows (< 04/2023) 

## Télécharger l'installateur
Visitez le site officiel de MongoDB et téléchargez l'installateur pour Windows.

## Exécuter l'installateur
Ouvrez l'installateur téléchargé et suivez les instructions.

## Configurer le chemin d'accès
Ajoutez le dossier `bin` de MongoDB à la variable d'environnement PATH.

## Créer le dossier de données
```bash
md \data\db
```



## Étape 5 : Démarrer MongoDB
Ouvrez une invite de commande et tapez `mongod` pour démarrer le serveur MongoDB.


# Vérifier la version de MongoDB

Pour afficher la version installée, tapez :

```bash
mongod --version
# Ou :
mongo --version
```




