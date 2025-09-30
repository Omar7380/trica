FROM python:3.11-slim

WORKDIR /app
COPY . /app
RUN pip install flask

# L'image sera utilisée pour les deux serveurs, on précisera le script au lancement
CMD ["python", "app1.py"]