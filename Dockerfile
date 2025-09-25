# Utilise une image Python légère
FROM python:3.12-slim-bookworm

# Créer le dossier de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY app.py .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Variables d’environnement Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Exposer le port
EXPOSE 5000

# Commande de lancement
CMD ["flask", "run"]
