class Rectangle:
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

    def perimetre(self):
        perimetre = (self.get_longueur() + self.get_largeur())*2
        return perimetre
    
    def surface(self):
        surface = self.get_longueur() * self.get_largeur()
        return surface
    

class parallelepipede(Rectangle):
    def __init__(self, hauteur):

        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        volume = self.get_longueur() * self.get_largeur()*self.get_hauteur()
        return print(f"votre para a un volume de : {volume}")

    
rectangle = Rectangle(10,15)
print(rectangle.get_longueur())
print(rectangle.get_largeur())
print(rectangle.perimetre())
print(rectangle.surface())







