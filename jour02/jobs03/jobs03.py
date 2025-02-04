class Livre:
    def __init__(self, auteur, titre, nombre):
        self.__auteur = auteur
        self.__titre = titre 
        self.__nombrePages = nombre
        self.__disponible = True
    
    def get_auteur(self):
        return self.__auteur

    def get_titre(self):
        return self.__titre
    
    def get_nombrePages(self):
        return self.__nombrePages
    
    def verif_disp(self):
        if self.__disponible == True:
            return True
        else: 
            return False
    
    def emprunt(self,dispo):
        if dispo == True:
            print("votre livre est disponible")
            self.__disponible = False
    
    def rendre(self,dispo):
        if dispo == False:
            print("votre livre n'est pas disponible")
            self.__disponible = True

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_titre(self, titre):
        self.__titre = titre
    
    def set_nombrePages(self, nombre):
            if nombre == int(nombre) and nombre > 0:
                self.__nombrePages = nombre
            else:
                print("vous n'avez pas rentrez un nombre entier positif")
        

livre = Livre("alex","blabla", 1)

livre.emprunt(livre.verif_disp())
print(livre.verif_disp())
livre.rendre(livre.verif_disp())
print(livre.verif_disp())

