#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculer le factoriel d'un nombre donné de manière récursive.

    Description de la fonction :
    Cette fonction calcule le factoriel d'un entier non négatif en utilisant la récursion. 
    Le factoriel de 0 est défini comme étant égal à 1. Pour tout entier positif n, 
    le factoriel est le produit de tous les entiers positifs inférieurs ou égaux à n.

    Paramètres :
    n (int) : Un entier non négatif dont le factoriel doit être calculé.

    Retourne :
    int : Le factoriel du nombre donné n.
    """
    if n == 0:
        return 1  # Cas de base : le factoriel de 0 est 1
    else:
        return n * factorial(n - 1)  # Appel récursif

# Programme principal
# Lire le premier argument de la ligne de commande, le convertir en entier, et calculer son factoriel
f = factorial(int(sys.argv[1]))
print(f)  # Afficher le résultat
