import csv
from ajout import * 

def principale():
    produits = 'productos.csv'
    while True :
        input = menu_affichage()
        if input == "1" :
            voir_nom(produits)
        elif input == "2" :
            new_produit(produits)
        elif input == "3" :
            supprimer_produit(produits, supprimer_colonne)
        elif input == "4" : 
            binary_search(produits)
        elif input == "5" :
            print("Fermeture du programme")