from gestion_hopital.service import GestionPatients

def afficher_menu():
    print("\n=== Gestion des patients ===")
    print("1. Ajouter un patient")
    print("2. Lister les patients")
    print("3. Rechercher un patient")
    print("4. Quitter")

def main():
    service = GestionPatients()

    while True:
        afficher_menu()
        choix = input("Choix : ")

        if choix == "1":
            nom = input("Nom du patient : ")
            age = int(input("Âge du patient : "))
            service.ajouter_patient(nom, age)
            print("Patient ajouté avec succès.")

        elif choix == "2":
            patients = service.lister_patients()
            if not patients:
                print("Aucun patient.")
            else:
                print("\nListe des patients :")
                for p in patients:
                    print(p)

        elif choix == "3":
            nom = input("Nom à rechercher : ")
            resultats = service.rechercher_patient(nom)

            if not resultats:
                print("Aucun patient trouvé.")
            else:
                print("\nRésultats :")
                for p in resultats:
                    print(p)

        elif choix == "4":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()