#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Réduction de n pour éviter une boucle infinie
    return result

# Gestion des erreurs pour les entrées non valides
try:
    n = int(sys.argv[1])
    if n < 0:
        print("Erreur : le factoriel d'un nombre négatif n'est pas défini.")
    else:
        f = factorial(n)
        print(f"Le factoriel de {n} est {f}.")
except (IndexError, ValueError):
    print("Usage : ./script.py <entier>")
