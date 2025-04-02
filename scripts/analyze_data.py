def run():
    """
    Ce script exécute des requêtes SQL sur la table 'sales' de la base de données SQLite,
    puis exporte les résultats sous forme de fichiers CSV dans le répertoire output/.

    """

    import sqlite3
    import pandas as pd

    # 1. Connexion à la base
    conn = sqlite3.connect("data/sales.db")


    # 2. Requête 1 : Top 5 produits par chiffre d'affaires
    
    query1 = """
    SELECT product, ROUND(SUM(total_price), 2) AS total_revenue
    FROM sales
    GROUP BY product
    ORDER BY total_revenue DESC
    LIMIT 5
    """
    top_products = pd.read_sql(query1, conn)  # Exécute la requête SQL 'query1' sur la base SQLite via la connexion 'conn' et charge le résultat dans un DataFrame pandas nommé 'top_products'
    
    top_products.to_csv("output/top_products.csv", index=False) # Exporte le DataFrame 'top_products' dans un fichier CSV situé dans le dossier 'output'


    # 3. Requête 2 : Ventes par ville
    query2 = """
    SELECT city, ROUND(SUM(total_price), 2) AS total_revenue 
    FROM sales
    GROUP BY city
    ORDER BY total_revenue DESC
    """
    sales_by_city = pd.read_sql(query2, conn)
    sales_by_city.to_csv("output/sales_by_city.csv", index=False)

    # 4. Requête 3 : Clients les plus actifs (nb de commandes)
    query3 = """
    SELECT customer_name, COUNT(order_id) AS nb_orders
    FROM sales
    GROUP BY customer_name
    ORDER BY nb_orders DESC
    LIMIT 5
    """
    top_customers = pd.read_sql(query3, conn)
    top_customers.to_csv("output/top_customers.csv", index=False)


    # 5 Panier moyen par client
    query4 = """
    SELECT 
        customer_name,
        ROUND(SUM(total_price), 2) AS total_spent,                          -- total d'argent dépensé par le client 

        COUNT(order_id) AS nb_orders,                                       -- nombre de commandes passées par le client

        ROUND(SUM(total_price) / COUNT(order_id), 2) AS avg_basket          -- panier moyen du client (total dépensé / nombre de commandes)

    FROM sales
    GROUP BY customer_name
    ORDER BY avg_basket DESC
    LIMIT 10
    """
    avg_basket = pd.read_sql(query4, conn)
    avg_basket.to_csv("output/avg_basket_per_customer.csv", index=False)


    #6 Produits les plus commandés
    query_top_quantity = """
    SELECT 
        product,
        SUM(quantity) AS total_quantity                                -- nombre total d'article vendus pour chaque produit
    FROM sales
    GROUP BY product
    ORDER BY total_quantity DESC
    """
    top_quantity = pd.read_sql(query_top_quantity, conn)
    top_quantity.to_csv("output/top_products_by_quantity.csv", index=False)


    #7 Évolution des ventes par jour

    query_daily_sales = """
    SELECT 
        order_date,
        ROUND(SUM(total_price), 2) AS daily_revenue                    -- chiffre d'affaires quotidien

    FROM sales
    GROUP BY order_date
    ORDER BY order_date
    """
    daily_sales = pd.read_sql(query_daily_sales, conn)
    daily_sales.to_csv("output/daily_sales.csv", index=False)

    #8. Fermer la connexion
    conn.close()

    print("✅ Analyses terminées. Résultats exportés dans le dossier output/.")



if __name__ == "__main__":
    run()
