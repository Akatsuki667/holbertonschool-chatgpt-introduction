#!/usr/bin/python3
import sys

print("Liste des arguments passés au script :")
for i in range(len(sys.argv)):
    print(f"Argument {i} : {sys.argv[i]}")
