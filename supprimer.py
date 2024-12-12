import csv

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
            print(f"Erreur : La colonnes 'Nom_Produit' n'existe pas dans ce fichier")

supprimer_produit('productos.csv' , supprimer_colonne = supprimer_colonne)