#!/usr/bin/python3
def print_board(board):
    """
    Affiche la grille de jeu.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print()  # Ajout d'un espacement après l'affichage de la grille

def check_winner(board):
    """
    Vérifie si un joueur a gagné.
    """
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Lance la partie de Tic-Tac-Toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        
        # Entrée sécurisée pour la ligne
        try:
            row = int(input(f"Entrez la ligne (0, 1, ou 2) pour le joueur {player}: "))
            if row not in [0, 1, 2]:
                print("Numéro de ligne invalide, veuillez entrer un nombre entre 0 et 2.")
                continue
        except ValueError:
            print("Entrée invalide, veuillez entrer un entier.")
            continue
        
        # Entrée sécurisée pour la colonne
        try:
            col = int(input(f"Entrez la colonne (0, 1, ou 2) pour le joueur {player}: "))
            if col not in [0, 1, 2]:
                print("Numéro de colonne invalide, veuillez entrer un nombre entre 0 et 2.")
                continue
        except ValueError:
            print("Entrée invalide, veuillez entrer un entier.")
            continue

        # Vérification si l'emplacement est déjà occupé
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("Cette case est déjà occupée ! Essayez une autre.")
            continue

        # Vérification du gagnant
        if check_winner(board):
            print_board(board)
            print(f"Le joueur {player} a gagné!")
            break
        
        # Changer de joueur
        player = "O" if player == "X" else "X"

tic_tac_toe()
