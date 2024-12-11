import csv

def ajout(productos):
    with open('productos.csv', 'a', newline='') as file :
      nouveau_produit = input("Entrez le produit de votre choix, sous le format du fichier")
      produits_separes = [x.strip() for x in nouveau_produit.split(',')]
      writer = csv.writer(file)
      writer.writerow(produits_separes)
    with open('productos.csv', 'r') as file :
      tout = file.read()
      print(tout)

ajout('productos.csv')

        