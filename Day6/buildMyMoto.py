# BUILD MY MOTO

# L’objectif de ce challenge va être de créer un objet définissant une moto.
#
# 👉 Initialisez une classe Moto(), permettant d’instancier des objets compte à partir d’attributs 
# brand et color. L’objet disposera également d’attributs par défaut : 
# pilot à "" (chaîne de caractères vide) 
# et speed à 0 qui ne pourront pas être initialisés par l’utilisateur.
#
# 👉 Mettez en place trois méthodes :
#
# change_pilot(self, pilot) : modifie le pilote sur la Moto.
# set_speed(self, rate, duration) : définit la vitesse de la Moto (produit de rate et duration) 
# si celle-ci dispose bien d’un pilote.
# __repr__(self) : affiche les informations de la Moto.

class Moto:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.pilot = ""
        self.speed = 0

    def change_pilot(self, pilot):
        self.pilot = pilot

    def set_speed(self, rate, duration):
        if self.pilot:
            self.speed = rate * duration

    def __repr__(self):
        return f"Moto(brand={self.brand}, color={self.color}, pilot={self.pilot}, speed={self.speed})"

# Exemple d'utilisation
moto = Moto("Yamaha", "Red")
print(moto)

moto.change_pilot("Fred")
moto.set_speed(10, 15)
print(moto)