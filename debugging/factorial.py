#!/usr/bin/python3 # Shebang -> Utilisation interpréteur Python 3
import sys # Accès arguments passés au script via sys.argv

def factorial(n): # Déclaration fonction 
    result = 1 # Initialisation variable
    while n > 1:
        result *= n
        n -= 1  # Réduction de n pour éviter une boucle infinie
    return result

# Gestion des erreurs pour les entrées non valides
try: # Débute bloc d'essai gestion exceptions
    n = int(sys.argv[1]) # Lecture premier argument ligne et conversion de ce dernier
    if n < 0: # Condition de vérification
        print("Erreur : le factoriel d'un nombre négatif n'est pas défini.")
    else:
        f = factorial(n) # Appel fonction pour calcul
        print(f"Le factoriel de {n} est {f}.") # Affichage résultat
except (IndexError, ValueError): # Gestion exceptions capture deux types d'erreurs
    print("Usage : ./script.py <entier>") # Affichage message d'usage
