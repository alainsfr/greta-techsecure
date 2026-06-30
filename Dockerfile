# 1. Utiliser une image de base Python légère
FROM python:3.10-slim

# 2. Définir le dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier d'abord le fichier des dépendances pour optimiser le cache Docker
COPY requirements.txt .

# 4. Installer les bibliothèques Python requises (Flask, mysql-connector, bcrypt)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier tout le reste du code source du projet dans le conteneur
COPY . .

# 6. Indiquer que le conteneur écoutera sur le port 5000
EXPOSE 5000

# 7. Commande pour démarrer l'application Flask
CMD ["python", "app.py"]