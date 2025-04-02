def run() :

    """
    Ce script nettoie les données de vente en supprimant les doublons, en traitant les valeurs manquantes, en normalisant les noms des clients et en calculant le prix total.
    
    """

    import pandas as pd


    df=pd.read_csv("data/raw_sales_data.csv")

    df.drop_duplicates(inplace=True)

    df["customer_name"] = df["customer_name"].str.strip().str.title()  # Normaliser la casse (customer_name)

    #print(df.isnull().sum())  # Afficher le nombre de valeurs manquantes par colonne

    df= df.dropna(subset=["unit_price"])  # Supprimer les lignes avec unit_price manquant

    df["email"] = df["email"].fillna("no_email@example.com")  # Remplacer les valeurs manquantes par une valeur par défaut

    df["city"] = df["city"].fillna("Unknown")        # Remplacer les valeurs manquantes par unknown

    df["unit_price"]=df["unit_price"].round(2)  # Arrondir les prix à deux décimales

    df["total_price"] = df["quantity"] * df["unit_price"] # Calculer le prix total

    df["total_price"] = df["total_price"].round(2)  # Arrondir les prix à deux décimales


    df.to_csv("data/cleaned_sales_data.csv", index=False)  # Enregistrer le DataFrame nettoyé dans un nouveau fichier CSV

    print("✅ Données nettoyées et enregistrées dans data/cleaned_sales_data.csv")


if __name__ == "__main__":
    run()   