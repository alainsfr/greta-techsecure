# 🔒 TechSecure Solutions - Portail de Gestion Centralisé

TechSecure Solutions est une application web dynamique développée avec le framework Flask (Python), connectée à une base de données MySQL et entièrement conteneurisée à l'aide de Docker et Docker Compose. 

Ce projet a été conçu dans le cadre d'un livrable technique, respectant les normes de sémantique HTML5, d'intégration CSS responsive (Media Queries) et de sécurité applicative (protection contre les injections SQL).

---

## 🚀 Fonctionnalités Majeures

- **Page d'Accueil & Services** : Vitrine de l'entreprise présentant les expertises métiers (Cybersécurité, Cloud, Infogérance) et les agences sous forme de cartes fluides et ergonomiques.
- **Gestion Dynamique des Filiales (CRUD)** :
  - **👁️ Visualisation (Read)** : Fiche technique détaillée de chaque agence (Effectifs, adresses, segments réseaux).
  - **➕ Ajout (Create)** : Formulaire d'enregistrement d'une nouvelle agence dans le SI.
  - **📝 Modification (Update)** : Formulaire dynamique pré-rempli pour la mise à jour des infrastructures.
  - **🗑️ Suppression (Delete)** : Retrait sécurisé d'une filiale avec boîte de dialogue de confirmation de sécurité.
- **Formulaire de Contact** : Enregistrement automatisé des demandes clients dans la base de données avec système de notifications d'alertes Flask (Flash Messages).
- **Design Responsive** : Adaptabilité complète du menu, des tableaux et des grilles pour les supports mobiles (smartphones et tablettes) via Media Queries.

---

## 🛠️ Stack Technique

- **Backend** : Python 3.10+ / Flask
- **Base de données** : MySQL 8.0 (Encodage natif utf8mb4 pour la gestion des accents)
- **Pilote de connexion** : mysql-connector-python
- **Frontend** : HTML5 sémantique / CSS3 (Grid & Flexbox avancés) / Architecture Jinja2 (Templates éditables et héritage via base.html)
- **Conteneurisation** : Docker / Docker Compose

---

## 🔒 Security & Bonnes Pratiques

- **Protection anti-injection SQL** : Toutes les requêtes en base de données (SELECT, INSERT, UPDATE, DELETE) utilisent l'encapsulation de requêtes paramétrées via le driver MySQL. Aucun paramètre utilisateur n'est directement concaténé dans les chaînes SQL.
- **Sécurisation Docker** : Les variables d'environnement sensibles (mots de passe root de la base de données, clés secrètes applicatives) sont isolées et configurées à travers le fichier d'orchestration Docker Compose.
- **Isolation réseau** : Le conteneur Flask (web) et le conteneur MySQL (db) communiquent au sein d'un sous-réseau privé isolé créé par Docker.

---

## 📦 Installation et Lancement

### Prérequis
Avoir installé Docker Desktop et Git sur votre machine.

### 1. Cloner le projet
```bash
git clone https://github.com/alainsfr/greta-techsecure.git
cd techsecure-solutions

### 2. Démarrer l'infrastructure (Docker)

Pour compiler les images et lancer l'application et la base de données en arrière-plan, exécutez la commande suivante dans votre terminal Git Bash ou PowerShell :
```bash
docker compose up -d --build

### 3. Accéder à l'application

Une fois les conteneurs démarrés, ouvrez votre navigateur internet et rendez-vous sur :
http://127.0.0.1:5000


Commandes Utiles pour l'Administration

Forcer la reconstruction et vider le cache en cours de développement :

   ```bash
docker compose up -d --build --force-recreate web

Arrêter proprement les services :
```bash
docker compose down

Consulter les journaux de logs en temps réel (Audit) :
```bash
docker compose logs -f web


Architecture des Fichiers

├── app.py                  # Script principal Flask (Routes, Sécurité, Logique métier)
├── docker-compose.yml      # Orchestrateur des conteneurs (web, db, volumes et réseaux)
├── Dockerfile              # Instructions de build de l'image Python/Flask
├── requirements.txt        # Dépendances Python requises
├── init.sql                # Script d'initialisation de la base MySQL (Tables et données de test)
├── static/
│   ├── style.css           # Feuille de style globale (Grid, Flexbox, Media Queries)
│   └── IMAGE/              # Ressources graphiques (logo, paris.jpg, lyon.jpg...)
└── templates/
    ├── base.html           # Squelette global du site (Navbar, Footer, En-tête)
    ├── accueil.html        # Page d'accueil (Bandeau Hero, Agences)
    ├── services.html       # Grille des prestations de l'entreprise
    ├── filiales.html       # Tableau de bord général des agences
    ├── voir.html           # Fiche technique détaillée d'une agence
    ├── ajouter.html        # Formulaire de création d'agence
    ├── modifier.html       # Formulaire d'édition d'agence
    └── contact.html        # Formulaire de contact client avec messages flash