from scripts import clean_data, load_to_sqlite, analyze_data


def main():
    print("🧼 Étape 1 : Nettoyage des données...")
    clean_data.run()

    print("💾 Étape 2 : Chargement dans la base SQLite...")
    load_to_sqlite.run()

    print("📊 Étape 3 : Analyse des données...")
    analyze_data.run()

    print("✅ Pipeline exécuté avec succès !")

if __name__ == "__main__":
    main()
