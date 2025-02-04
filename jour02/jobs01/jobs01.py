


class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, valeur):
        self.__longueur = valeur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, valeur):
        self.__largeur = valeur

    
rectangle = Rectangle(10, 5)

print("la longueur de votre rectangle est de ", rectangle.get_longueur())
print("la largeur de votre rectangle est de ", rectangle.get_largeur())

rectangle.set_longueur(20)
rectangle.set_largeur(10)

print("la longueur de votre rectangle est de ", rectangle.get_longueur())
print("la largeur de votre rectangle est de ", rectangle.get_largeur())