
import csv

def creation():
    open('produits.txt', 'w').close()

donnees = [
    [1, "Louboutin", "9999.99", "25"],
    [2, "Pommes", "1.20", "65"],
    [3, "Porte-avions", "1000000", "3"],
    [4, "Ampoules", "5.99", "39"]
]

with open('productos.csv', 'w', newline='') as file : 
    writer = csv.writer(file)
    field = ["ID", "Nom_produit", "Prix", "Quantitées"]
    writer.writerow(field)
    writer.writerows(donnees)

with open('productos.csv', 'r') as file : 
    tout = file.read()
    print(tout)
