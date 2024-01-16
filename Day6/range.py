# RANGE
#
# L’objectif de ce challenge est de recréer simplement l’objet range natif à Python.
#
# 👉 Initialisez une classe Range, pouvant prendre 3 arguments : une borne inférieure, 
# une borne supérieure et un pas (facultatif, par défaut, fixé à 1) permettant de générer 
# une liste de nombres compris entre la borne inférieure (incluse) et la borne supérieure (exclue) 
# avec le pas indiqué par l’utilisateur. L’affichage de la classe Range (print(Range(0,6)) 
# devra retourner la liste générée. 
#
# Note : tout comme la fonction range en Python, l’utilisateur doit pouvoir indiquer comme paramètres 
# une borne inférieure qui soit plus grande que la borne supérieure, avec un pas négatif, 
# et l’objet sera renvoyé au bon format : Range(6, 0, -1) renverra [6, 5, 4, 3, 2, 1].
#
# 👉 Mettez en place une méthode reverse() permettant d’inverser l’ordre des éléments de l’objet Range. 
# Par exemple : Range(0,4) renverra [0, 1, 2, 3] et Range(0, 4).reverse() renverra [3, 2, 1, 0].

class Range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.range_list = self.generate_range()

    def generate_range(self):
        range_list = []
        if self.step == 0:
            raise ValueError("step cannot be zero")

        if self.step > 0 and self.start < self.end:
            number = self.start
            while number < self.end:
                range_list.append(number)
                number += self.step
        elif self.step < 0 and self.start > self.end:
            number = self.start
            while number > self.end:
                range_list.append(number)
                number += self.step

        return range_list

    def reverse(self):
        return self.range_list[::-1]

    def __repr__(self):
        return str(self.range_list)

# Exemples d'utilisation:
print(Range(0, 6))  # [0, 1, 2, 3, 4, 5]
print(Range(6, 0, -1))  # [6, 5, 4, 3, 2, 1]
print(Range(0, 4).reverse())  # [3, 2, 1, 0]