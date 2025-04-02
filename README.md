# 🛍️ E-commerce Sales Pipeline Project

Ce projet met en place un **pipeline de traitement de données e-commerce** complet : de l’ingestion des données brutes jusqu’à l’analyse et la visualisation des ventes.

---

## Objectifs

- Nettoyer des données brutes de ventes
- Charger les données dans une base **SQLite**
- Exécuter des **requêtes analytiques SQL**
- Générer des **exports CSV**
- Créer des **visualisations interactives** via Jupyter

---

## Stack utilisée

- Python 
- pandas, matplotlib, seaborn
- SQLite
- Jupyter Notebook
- VS Code

---

## Structure du projet


```
ecommerce_pipeline_project/
├── data/                       # Données brutes, nettoyées et base SQLite
│   ├── raw_sales_data.csv
│   ├── cleaned_sales_data.csv
│   └── sales.db
│
├── notebooks/                 # Visualisations (Jupyter)
│   └── visualisations.ipynb
│
├── output/                    # Résultats CSV générés par les analyses
│   ├── top_products.csv
│   ├── top_customers.csv
│   └── ...
│
├── scripts/                   # Scripts Python (nettoyage, chargement, analyse)
│   ├── clean_data.py
│   ├── load_to_sqlite.py
│   └── analyze_data.py
│
├── main.py                    # Script principal du pipeline
├── requirements.txt           # Dépendances Python
├── .gitignore                 # Fichiers/dossiers ignorés par Git
└── README.md                  # Ce fichier 
```

---


## Exécution du pipeline

### 1. Cloner le projet

```bash
git clone https://github.com/TON_UTILISATEUR/ecommerce_pipeline_project.git

cd ecommerce_pipeline_project
```

### 2. Créer un environnement virtuel :

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

### 4. Lancer le pipeline :
```bash
python main.py
```

Les résultats seront générés dans le dossier output/.

---

## Visualisations

Le notebook notebooks/visualisations.ipynb contient :

- Top 5 produits par chiffre d’affaires

- Ventes par ville

- Évolution des ventes quotidiennes

- Panier moyen par client

- Produits les plus commandés

Les graphiques sont interprétés + commentés pour donner une vraie perspective business.

---

## Résultats générés

- top_products.csv : Produits les plus rentables 

- sales_by_city.csv : Analyse géographique 

- daily_sales.csv : Courbe de CA quotidien 

- avg_basket_per_customer.csv : Valeur client 

- top_products_by_quantity.csv : Produits les plus vendus 

- top_customers.csv : Clients les plus actifs 

---

## Auteur

Projet réalisé par Julien T.W AGA dans le cadre de ma montée en compétence en Data Engineering & Data Analytics.

---

## Licence

Ce projet est open source et libre de réutilisation.