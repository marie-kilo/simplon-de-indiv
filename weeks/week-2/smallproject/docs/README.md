

# Smallproject : Volonté du D

Projet d'application qui mobilise trois TP de la week_02 en même temps : scraping, classes et SQL. À faire en fin de semaine Python, ou comme « one day project », une fois ces trois TP vus.

## Prérequis (TP de la même semaine, à faire avant)

- TP 6 : scraping avec BeautifulSoup
- TP 7 : classes et séparation des responsabilités (programmation orientée objet)
- TP 10 : SQL et clés étrangères

## Déroulé conseillé

1. Lire le code de base (`main.py` et les trois classes) comme modèle d'architecture propre : un module par rôle, un point d'entrée clair, des classes plutôt qu'un gros script.
2. Lancer le projet : `pip install -r requirements.txt` puis `python3 main.py`. Le scraping s'exécute en direct.
3. Faire les exercices ci-dessous, qui sont la vraie montée en compétence.
4. Le corrigé de l'exercice 1 est dans `corrige.ipynb`, et `data/bdd.db` contient les trois tables résultantes comme référence.

# Setup 

## Installer pyenv & créer un environnement virtuel
- Guide dans le fichier `setup_env.md`


## Exécuter le code 
```bash
# Activer l'environnement virtuel (linux)
source env/bin/activate 
python3 main.py
```

# Exercices 

## Exercice 1
- On ne récupère actuellement que la liste d'un équipage. Modifier le code pour que l'on récupère la liste de tous les pirates de la Nouvelle Vague : http://www.volonte-d.com/perso/pirates.php.


- Pour chaque personnage, rapatrier la liste des noms des techniques de combat. Créer le dictionnaire : 
    ```
    {personnage:["technique_1_nom", "technique_2_nom"...]}
    ```

- Créer une table `équipages` avec les colonnes suivantes : 
    - Id (entier positif unique par ligne)
    - Nom de l'équipage
    - Nombre de membres

- Créer une table `personnages` avec les colonnes suivantes : 
    - Id (entier positif unique par ligne)
    - Nom du personnage
    - Foreign Key sur l'équipage de la table `équipage` (donc l'id de l'équipage auquel appartient le personnage)

- Créer une table `techniques` avec les colonnes suivantes : 
    - Id (entier positif unique par ligne)
    - Nom de la technique
    - Foreign Key sur le personnage de la table `personnages` (donc l'id du personnage qui possède la technique)

- *Cette question est plus difficile et nécessite de faire des recherches.* Pour chaque technique de combat, récupérer la photo associée. Créer une nouvelle colonne dans la table technique, et stocker la photo (il faut trouver comment la stocker).



## Exercice 2
Avec le site de votre choix qui contient des données qui permettront de créer deux tables dont une table contient une Foreign Key pointant sur l'autre table, reproduire la démarche de ce projet.