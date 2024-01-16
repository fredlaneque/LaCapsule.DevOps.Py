# BANK ACCOUNT
#
# L’objectif de ce challenge est de créer un objet permettant de définir simplement le compte bancaire d’un utilisateur.
#
# 👉 Initialisez une classe CompteBancaire(), permettant d’instancier des objets à partir des attributs nom (string) et solde (int).
#
# 👉 Mettez en place trois méthodes :
#    depot(self, somme) : ajoute la somme indiquée au solde.
#    retrait(self, somme) : retire la somme indiquée au solde.
#    __repr__(self) : affiche le nom du titulaire et du solde du compte. 
#
# Par exemple : 
# print(CompteBancaire("Vanessa", 2000)) affichera dans la console : 
# "Compte bancaire de Vanessa : 2000 euros."


class CompteBancaire:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        self.solde += somme

    def retrait(self, somme):
        self.solde -= somme

    def __repr__(self):
        return f"Compte bancaire de {self.nom} : {self.solde} euros."

# Exemple d'utilisation
compte = CompteBancaire("Vanessa", 2000)
print(compte)

compte.depot(500)
compte.retrait(300)
print(compte)