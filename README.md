# 🤖 RobotIndexWeb

## 📋 Description

RobotIndexWeb est un robot d'indexation web qui explore récursivement les pages d'un site web et extrait les mots-clés pertinents. Ce projet a été développé dans le cadre d'un cours de méthodologie en programmation.

## 👤 Informations du projet

- **Auteur** : Moustapha DIAGNE
- **Version** : v0.3
- **Date** : 24 mars 2022
- **Contexte** : Projet académique - Cours de méthodologie en programmation

## 🎯 Fonctionnalités

- **Extraction de liens** : Parcourt récursivement les liens HTTP d'une page web
- **Nettoyage HTML** : Supprime les balises HTML et extrait le contenu textuel
- **Indexation intelligente** : 
  - Filtre les mots vides (stopwords) en français
  - Vérifie la validité des mots via un dictionnaire français
  - Supprime les doublons
- **Limitation de profondeur** : Contrôle du nombre de récursions (par défaut : 30 niveaux)
- **Gestion d'erreurs** : Gestion robuste des erreurs de récursion et de connexion

## 🛠️ Prérequis

- Python 3.x
- Bibliothèques requises :
  - `requests`
  - `re` (module standard)
  - `sys` (module standard)

## 📦 Installation

```bash
# Cloner le repository
git clone [URL_DU_REPO]

# Installer les dépendances
pip install requests
```

## 🚀 Usage

### Script Python

```bash
python3 RobotIndexWeb.py "https://www.example.com"
```

### Jupyter Notebook

Le projet inclut également un notebook Jupyter (`Moustapha_Diagne_Devoir3.ipynb`) qui contient :
- Le développement progressif des fonctions
- Des exemples d'utilisation
- Des tests et validations

## 📝 Structure du projet

```
.
├── RobotIndexWeb.py              # Script principal
├── Moustapha_Diagne_Devoir3.ipynb # Notebook de développement
└── README.md                      # Ce fichier
```

## 🔧 Configuration

Le script utilise plusieurs listes de mots vides (stopwords) en français :
- Articles
- Prépositions
- Pronoms
- Adverbes
- Conjonctions de coordination

Le dictionnaire français système (`/usr/share/dict/french`) est utilisé pour valider les mots.

## ⚙️ Limitations

- Limite de récursion : 30 niveaux par défaut
- Ne supporte pas `localStorage` ou `sessionStorage` dans les artefacts
- Dépend de la disponibilité du dictionnaire français système

## 📄 Licence

Projet réalisé dans le cadre académique - Tous droits réservés

## 🤝 Contributions

Ce projet a été développé dans un contexte académique. Les contributions ne sont pas acceptées.

## 📧 Contact

Pour toute question concernant ce projet, veuillez contacter l'auteur via les canaux universitaires appropriés.

---

*Projet développé avec Python 3 - Mars 2022*
