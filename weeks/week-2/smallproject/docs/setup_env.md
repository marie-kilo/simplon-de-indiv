# Environnement de développement : smallproject

## pyenv

Il existe de nombreuses versions de Python, et il est important de contrôler celle utilisée dans un projet. `pyenv` installe plusieurs versions de Python dans un dossier dédié, et permet de créer un environnement virtuel à partir de la version choisie. C'est l'approche la plus simple et la plus sûre : utilise-la par défaut, sauf si tu es déjà à l'aise avec un autre outil.

### Installer pyenv

Sur macOS, avec Homebrew :

```bash
brew update
brew install pyenv
```

Sur Linux : suivre la procédure d'installation de [pyenv](https://github.com/pyenv/pyenv#installation).

Sur Windows : utiliser [pyenv-win](https://github.com/pyenv-win/pyenv-win) (lancer PowerShell en tant qu'administrateur).

### Installer Python

On utilise une version récente de Python :

```bash
pyenv install 3.13.1
```

## Créer l'environnement virtuel

```bash
# Créer un dossier pour le projet
mkdir smallproject
cd smallproject

# Créer un environnement virtuel appelé "env" à partir de la version installée
~/.pyenv/versions/3.13.1/bin/python -m venv env

# Activer l'environnement (Linux / macOS)
source env/bin/activate
# Sur Windows : source env/Scripts/activate

# Pour le désactiver plus tard : deactivate
```

## Installer les dépendances

Les librairies sont listées dans `requirements.txt`, sans numéro de version (on prend les versions récentes) :

```
requests
bs4
```

Installation :

```bash
source env/bin/activate
pip3 install -r requirements.txt
```

## Black, formatage du code

Black est un formateur de code « opinionated » : il uniformise le style quand plusieurs personnes travaillent sur la même base. Avec VS Code, il permet le « Format On Save ».

- [Black sur GitHub](https://github.com/psf/black)
- [Extension VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

## Versionner avec Git

```bash
git init
echo "env" > .gitignore         # on ne versionne pas l'environnement virtuel
echo ".DS_Store" >> .gitignore   # déchet macOS

git add .
git commit -m "first commit"
git remote add origin <url-de-ton-remote>
git push --set-upstream origin main
```

## Lancer le projet

```bash
source env/bin/activate
python3 main.py
```

## Structure du projet

```
smallproject
├── main.py            point d'entrée
├── retriever.py       classe Retriever (requête HTTP)
├── processor.py       classe Processor (parsing BeautifulSoup)
├── alerter.py         classe Alerter (alerte)
├── time_exec.py       mesure du temps d'exécution
├── requirements.txt   librairies (sans version épinglée)
├── runtime.txt        version de Python cible (python-3.13.1)
├── corrige.ipynb      corrigé
├── data/bdd.db        base SQLite
└── docs/              documentation
```
