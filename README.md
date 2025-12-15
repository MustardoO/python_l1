# RobotIndexWeb.py

## Description
Ce script Python permet de **scraper récursivement les pages** à partir d'une URL source, en explorant les liens internes du site (indexation web basique).

## Métadonnées du projet

- **Nom du fichier** : `RobotIndexWeb.py`
- **Rôle** : Scraper récursivement les pages d'un site web
- **Auteur** : DIAGNE Moustapha
- **Version** : V0.3
- **Date** : 24/03/2022
- **Licence / Contexte** : Réalisé dans le cadre du cours de méthodologie en programmation
- **Note sur la compilation** : La mention "gcc (GNU COMPILER COLLECTION)" semble erronée ou résiduelle, car le script est en **Python 3** et ne nécessite pas de compilation C/C++.

## Prérequis
- Python 3.x
- Bibliothèques Python nécessaires (à installer via `pip` si besoin) :
  - Probablement `requests`, `beautifulsoup4` et éventuellement `urllib` (à vérifier dans le code source)

## Utilisation
Le script prend **un unique argument** en ligne de commande : l'URL source du site à indexer.

### Exemple de lancement :
```bash
python RobotIndexWeb.py "https://example.com"
