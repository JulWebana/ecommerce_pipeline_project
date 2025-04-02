def run():
    """
    Ce script charge les données de vente nettoyées dans une base de données SQLite nommée sales.db et les stocke dans une table nommée "sales".
    
    """

    import pandas as pd
    import sqlite3

    # 1. Lire les données nettoyées
    df = pd.read_csv("data/cleaned_sales_data.csv")

    # 2. Connexion (ou création) à la base SQLite
    conn = sqlite3.connect("data/sales.db")

    # 3. Charger les données dans une table "sales"
    df.to_sql("sales", conn, if_exists="replace", index=False)

    # 4. Fermer la connexion
    conn.close()

    print("✅ Données chargées dans la base SQLite (data/sales.db)")

    print(f"✅ {len(df)} lignes insérées dans la table 'sales'")


if __name__ == "__main__":
    run()
