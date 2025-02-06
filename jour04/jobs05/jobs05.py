import math


class Forme:
    def aire():
        return 0

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

    def aire(self):
        return self.get_longueur() * self.get_largeur()

class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius

    def aire(self):
        return math.pi * (self.get_radius()*self.get_radius())





rectangle = Rectangle(20,30)
cercle = Cercle(50)
print(rectangle.aire())
print(cercle.aire())