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

rectangle = Rectangle(20,30)

print(rectangle.aire())