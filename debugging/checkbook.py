class Checkbook:
    """
    Une classe simple pour gérer un chéquier : dépôts, retraits et consultation du solde.

    Attributs:
    balance (float): Le solde actuel dans le chéquier.
    """

    def __init__(self):
        """
        Initialise le chéquier avec un solde de 0,0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose le montant spécifié dans le chéquier.

        Paramètres:
        amount (float): Le montant à déposer.

        Retourne:
        None
        """
        self.balance += amount
        print("Montant déposé : ${:.2f}".format(amount))
        print("Solde actuel : ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire le montant spécifié du chéquier si le solde est suffisant.

        Paramètres:
        amount (float): Le montant à retirer.

        Retourne:
        None
        """
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.balance -= amount
            print("Montant retiré : ${:.2f}".format(amount))
            print("Solde actuel : ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel du chéquier.

        Retourne:
        None
        """
        print("Solde actuel : ${:.2f}".format(self.balance))

def main():
    """
    Fonction principale pour gérer les interactions avec l'utilisateur.

    Retourne:
    None
    """
    cb = Checkbook()
    while True:
        action = input("Que souhaitez-vous faire ? (deposit, withdraw, balance, exit) : ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Entrez le montant à déposer : $"))
                if amount < 0:
                    print("Le montant doit être un nombre positif.")
                    continue
                cb.deposit(amount)
            except ValueError:
                print("Entrée invalide. Veuillez entrer une valeur numérique.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Entrez le montant à retirer : $"))
                if amount < 0:
                    print("Le montant doit être un nombre positif.")
                    continue
                cb.withdraw(amount)
            except ValueError:
                print("Entrée invalide. Veuillez entrer une valeur numérique.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Commande invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
