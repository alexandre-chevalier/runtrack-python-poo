class Voiture:
    def __init__(self, marque, modele, annee, km):
        self.__marque = marque
        self.__modele = modele 
        self.__annee = annee
        self.__kilometrage = km
        self.__reservoir = 50
        self.__enMarche = False


    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee

    def get_km(self):
        return self.__kilometrage
    
    def get_etat(self):
        return self.__enMarche
    
    def _verifier_plein(self):
        return self.__reservoir

    def set_marque(self, marque):
        self.__marque = marque   

    def set_modele(self, modele):
        self.__modele = modele 
    
    def set_annee(self, annee):
        self.__annee = annee

    def set_km(self, km):
        self.__kilometrage = km

    def set_etat(self, etat):
        self.__enMarche = etat

    def demarrer(self):
        self.__enMarche = True
    
    def arreter(self):
        self.__enMarche = False
    

