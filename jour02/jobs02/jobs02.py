class Livre:
    def __init__(self, auteur, titre, nombre):
        self.__auteur = auteur
        self.__titre = titre 
        self.__nombrePages = nombre
    
    def get_auteur(self):
        return self.__auteur

    def get_titre(self):
        return self.__titre
    
    def get_nombrePages(self):
        return self.__nombrePages
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_titre(self, titre):
        self.__titre = titre
    
    def set_nombrePages(self, nombre):
            if nombre == int(nombre) and nombre > 0:
                self.__nombrePages = nombre
            else:
                print("vous n'avez pas rentrez un nombre entier positif")
        
        
    
livre = Livre("isaac asimov", "foundation", 400)

print(livre.get_auteur())
print(livre.get_titre())
print(livre.get_nombrePages())

livre.set_auteur("patrick rothfuss")
livre.set_nombrePages(10)
livre.set_titre("le nom du vent")

print(livre.get_auteur())
print(livre.get_titre())
print(livre.get_nombrePages())