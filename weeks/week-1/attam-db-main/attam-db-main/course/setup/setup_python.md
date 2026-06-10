

# Environnement virtuel Python 3.11.2 avec pyenv


## Création
Dans le dossier contenant le code du cours (par exemple le dossier de ce repository) : 
```bash
<votre-chemin>/.pyenv/versions/3.11.2/bin/python3 -m venv env
```

## Activation

```bash
source env/bin/activate
```

## Vérification

```bash
# tout en ayant l'environnement virtuel activé
which pip
# Doit afficher un chemin vers le dossier env qui a été créé 
```


## Installer les dépendances

(Contient  `jupyter` et `ipykernel`)

```bash
# tout en ayant l'environnement virtuel activé
pip3 install -r requirements.txt
```


## Enregistrer l'environnement virtuel

```
# tout en ayant l'environnement virtuel activé
python -m ipykernel install --name ENV_DBA --display-name ENV_DBA --user
```



## Exécuter jupyter-lab

```bash
# tout en ayant l'environnement virtuel activé
# rajouter le chemin complet pour être sûr de bien exécuter Jupyter depuis l'environnement virtuel
env/bin/jupyter-lab
```



