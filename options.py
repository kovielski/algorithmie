import csv


def menu_affichage():
    print("\nMenu Interactif :")
    print("1 : Voir seulement les produits")
    print("2 : Ajouter un nouveau produit")
    print("3 : Effacer un produit")
    print("4 : Chercher un produit spécifique")
    print("5 : Fermer le fichier")
    option = int(input("Entrez le chiffre de votre choix :"))
    return option 

def voir_nom():
    with open('productos.csv', 'r') as file :
        reader = csv.DictReader(file)
    print("Liste des produits : ")
    for row in reader :
        print(row['nom_prod'])

def new_produit(produits):
    nouvelle_colonne = input("Ajoutez une nouvelle colonne dans le format : ID, Nom_produit, Prix, Quantitées")
    with open('productos.csv', 'a', newline ='') as file :
        writer = csv.writer(file)
        writer.writerow(nouvelle_colonne)
        print("Article ajouté avec succès !")
        with open('productos.csv', 'r', newline ='') as file :
            content = file.read()
            print(content)

def supprimer_produit(produits, supprimer_colonne):
    supprimer_colonne = input("Choisissez le colonne à supprimer")
    try :
        with open('productos.csv', 'r') as file :
            reader = csv.DictReader(file)
            rows = [row for row in reader if row["Nom_produit"] != supprimer_colonne]
        if len(rows) == 0 or (len(rows) == sum(1 for _ in open(produits)) - 1) : 
            print(f"Aucune colonne avec le nom= '{supprimer_colonne} n'a été trouvée")
            return 
        with open('productos.csv', 'w', newline ='') as file :
            fieldnames = reader.fieldnames 
            writer = writerheader()
            writer.writerows(rows)
        print(f"Le produit : {supprimer_colonne} a bien été supprimé")

        except FileNotFoundError:
            print(f"Erreur : Le fichier '{produits}' n'existe pas")
        except KeyError:
            print(f"Erreur : La colonne '{Nom_Produit}' n'existe pas dans ce fichier")


def binary_search(produits) : 
    nom_prod = input("Entrez le nom du produit pour la recherche : ")
    try :
        with open('productos.csv', 'r') as file :
            reader =cvs.DictReader(file)
            rows = sorted(reader, key=lambda row: row['Nom_Produit'].lower())
        low, high = 0, len(rows) - 1 
        while low <= high :
            mid = (low + high) // 2 
            mid_name = rows[mid]['Nom_Produit'].lower()
            if mid_name == nom_prod.lower():
                return rows[mid]
            elif mid_name < nom_prod.lower():
                low = mid + 1 
            else : 
                high = mid - 1 
        return None 
    except FileNotFoundError :
        print(f"Erreur : {produits} n'a pas été trouvé")
        return None 
    except KeyError :
        print(f"Erreur : la colonne Nom_Produit n'a pas été trouvée")

