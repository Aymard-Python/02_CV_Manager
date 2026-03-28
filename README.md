# CV Manager – Application Console en Python

## Présentation du projet

**CV Manager** est le deuxième projet de mon challenge personnel **"60 Days of Python Projects"**.

L'objectif de cette phase est de développer une **application en ligne de commande (console)** permettant de **gérer une base de CV stockée au format JSON**.

Ce projet introduit plusieurs concepts importants en programmation Python :

🟢 Programmation Orientée Objet (POO)
🟢 Persistance des données avec JSON
🟢 Validation des entrées utilisateur
🟢 Interaction avec l’utilisateur via une interface console
🟢 Organisation et architecture d’un projet Python

Ce projet est la suite logique de **la Phase 1 – CV Data Analyzer**, qui consistait à analyser des données de CV.
Dans cette deuxième phase, l'objectif est de **gérer et manipuler ces données dynamiquement**.

---

# How to Run the Project

Clone the repository :

```
git clone https://github.com/Aymard-Python/02_cv_Manager.git
```

Navigate to the project folder :

```
cd 02_CV_Manager
```

Run the program :

```
python src/main.py
```

---

# Fonctionnalités prévues

Au cours des prochaines semaines, l'application intégrera progressivement les fonctionnalités suivantes :

✅ Ajouter un nouveau CV
✅ Modifier un CV existant
✅ Supprimer un CV
✅ Rechercher des CV par top compétence
✅ Afficher la liste des CV enregistrés
✅ Valider les entrées utilisateur
✅ Sauvegarder automatiquement les données au format JSON
✅ Structurer le projet avec la **Programmation Orientée Objet (POO)**

---

# Structure du projet

```
02_CV_Manager/
│
├── data/
│   └── cvs.json
│
├── src/
│   ├── models/
│   │   └── cv.py
│   │
│   ├── services/
│   │   └── cv_manager.py
│   │
│   ├── utils/
│   │   └── json_storage.py
│   │
│   └── main.py
│
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Explication de l’architecture

### models

Contient les **modèles de données** utilisés dans l'application.

🟢 `cv.py` définira la **structure d'un CV** sous forme de classe Python.

### services

Contient la **logique métier** de l'application.

🟢 `cv_manager.py` gérera les opérations sur les CV : ajout, modification, suppression et recherche.

### utils

Contient les **modules utilitaires**.

🟢 `json_storage.py` sera responsable du **chargement et de la sauvegarde des données JSON**.

### main.py

Point d’entrée de l’application.

Il sera responsable de :

* afficher le menu de l'application
* gérer les interactions avec l’utilisateur
* appeler les services nécessaires.

---

# Feuille de route du développement

Le projet sera développé progressivement selon les étapes suivantes :

### 🏁 Étape 1 – Modèle de données

Création de la **classe CV** avec la Programmation Orientée Objet.

### 🏁 Étape 2 – Gestion du stockage JSON

Implémentation du chargement et de la sauvegarde des CV.

### 🏁 Étape 3 – Gestionnaire de CV

Création des fonctionnalités pour gérer les CV.

### 🏁 Étape 4 – Interface Console

Création d’un menu interactif pour utiliser l'application.

### 🏁 Étape 5 – Validation des entrées

Ajout de contrôles pour sécuriser les entrées utilisateur.

---

# Objectifs pédagogiques

Ce projet a pour but de renforcer les compétences suivantes :

* architecture de projet Python
* programmation orientée objet
* manipulation et gestion de données JSON
* développement d'applications console interactives

---

# Évolution du projet

Cette application constitue une étape vers la construction d'une **future plateforme de gestion et de publication de CV**.

Les prochaines phases du challenge incluront :

* la visualisation de données
* la création d’un tableau de bord
* le développement d’une plateforme web complète.

---

# Auteur

Projet réalisé dans le cadre d'un **challenge d'apprentissage Python sur 60 jours**.

🚀 Fin du projet CV Manager.
