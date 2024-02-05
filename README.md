# ProjetPA-API

## Architecture du projet

```
ProjetPA-API/
├─ apimongo/
│  ├─ server/
│  │  ├─ models/
│  │  │  ├─ article.py
│  │  ├─ routes/
│  │  │  ├─ article.py
│  │  ├─ app.py
│  │  ├─ database.py
│  ├─ main.py
├─ insert_mongo.py
├─ README.md
├─ requirements.txt
├─ scrap_carrefour.py
├─ streamlit_mongo.py

```

## Pré-requis

Le projet contient le scrapping des données du site Carrefour et l'insertion dans MongoDB, l'officiant en streamlit et la gestion de API

## Installation de bibliothèques
La commande de terminal:
`pip install -r requirements.txt`

## Scrapping 
La commande de terminal:
`py ./scrap_carrefour.py`

## MongoDB

### Start server et terminal de mongo, l'exécution d'insert de données récupérés
Les commandes de terminal:
`start mongod | mongosh | py ./insert_mongo.py`

## Streamlit 
La commande de terminal:
`py ./streamlit_mongo.py`

## API CRUD
La commande de terminal:
`py ./apimongo/main.py`
## Adresse serveur:
`localhost:8000:/docs`

