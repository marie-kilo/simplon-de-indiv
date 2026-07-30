"""Orchestration : les 4 collecteurs sur une liste de départements.

Usage :
    python3 run_all.py                # 101 départements, les 4 collecteurs
    python3 run_all.py 69 01          # une sélection de départements, les 4 collecteurs
    python3 run_all.py a              # worker A : reseau_eau.py + qualite_eau.py, 101 départements
    python3 run_all.py b              # worker B : geo_risque.py + dvf.py, 101 départements
    python3 run_all.py a 69 01        # worker A sur une sélection de départements
    python3 run_all.py b 69 01        # worker B sur une sélection de départements

Procfile (Scalingo) :
    workera: python run_all.py a
    workerb: python run_all.py b

Chaque script de collecte implémente sa propre reprise.
L'ordre des départements (celui passé en argument, sinon DEPARTEMENTS) et
l'ordre relatif des scripts (celui de SCRIPTS) sont toujours respectés,
quel que soit le scénario (complet, worker a, worker b) : les deux workers
ne font que filtrer la même liste SCRIPTS, il n'y a pas d'ordre "parallèle"
distinct à maintenir.
Code de sortie : 0 sans échec, 1 sinon.
"""

import subprocess
import sys

# 101 départements : 96 métropolitains (2A et 2B remplacent le 20) et
# 5 d'outre-mer (971 à 974 et 976).
DEPARTEMENTS = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "2A",
    "2B",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "70",
    "71",
    "72",
    "73",
    "74",
    "75",
    "76",
    "77",
    "78",
    "79",
    "80",
    "81",
    "82",
    "83",
    "84",
    "85",
    "86",
    "87",
    "88",
    "89",
    "90",
    "91",
    "92",
    "93",
    "94",
    "95",
    "971",
    "972",
    "973",
    "974",
    "976",
]

# Liste canonique : toute sélection (mode complet, worker a, worker b) est
# un sous-ensemble filtré de SCRIPTS, ce qui garantit un ordre relatif
# toujours identique d'un scénario à l'autre.
SCRIPTS = ["geo_risque.py", "reseau_eau.py", "qualite_eau.py", "dvf.py"]

# Répartition des scripts entre les deux workers Scalingo.
WORKER_SCRIPTS = {
    "a": {"reseau_eau.py", "qualite_eau.py"},
    "b": {"geo_risque.py", "dvf.py"},
}


def parse_args(argv):
    """Interprète les arguments de la ligne de commande.

    Retourne (worker, depts) où worker vaut "a", "b" ou None (mode complet).
    argv[0] est reconnu comme sélecteur de worker s'il vaut "a" ou "b"
    (insensible à la casse) ; tous les arguments restants sont traités
    comme des codes de départements, exactement comme avant.
    """
    worker = None
    rest = list(argv)
    if rest and rest[0].lower() in WORKER_SCRIPTS:
        worker = rest[0].lower()
        rest = rest[1:]

    depts = [d.upper().zfill(2) for d in rest] or DEPARTEMENTS
    return worker, depts


def main():
    worker, depts = parse_args(sys.argv[1:])
    scripts = [s for s in SCRIPTS if worker is None or s in WORKER_SCRIPTS[worker]]

    echecs = []
    for dept in depts:
        for script in scripts:
            res = subprocess.run([sys.executable, script, dept])
            if res.returncode != 0:
                echecs.append(f"{script} {dept}")

    label = f" (worker {worker})" if worker else ""
    if echecs:
        print(f"{len(echecs)} échec(s){label} : {', '.join(echecs)}", flush=True)
        sys.exit(1)
    print(f"{len(depts)} département(s) chargés sans échec{label}", flush=True)


if __name__ == "__main__":
    main()
