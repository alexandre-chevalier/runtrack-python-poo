class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.__marque = marque
        self.__modele = modele 
        self.__annee  = annee
        self.__prix    = prix

    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_prix(self):
        return self.__prix
    
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_prix(self, prix):
        self.__prix = prix

    def demarrer(self):
        return f"attention je roule"

    def informationsVehicule(self):
       return f"""
            marque : {self.get_marque()}
            modele : {self.get_modele()}
            annee  : {self.get_annee()}
            prix   : {self.get_prix()}
            """
        

class Voiture(Vehicule):
    def __init__(self):
        self.__porte = 4

    def get_porte(self):
        return self.__porte
    
    def set_porte(self, porte):
        self.__porte = porte

    def demarrer(self):
        return super().demarrer() + "en voiture"

    def informationsVehicule(self):
        return super().informationsVehicule()+ f"nombre de porte : {self.get_porte()}"
    
class Moto(Vehicule):
    def __init__(self):
        self.__roue = 2

    def get_roue(self):
        return self.__roue

    def set_roue(self, roue):
        self.__roue = roue

    def demarrer(self):
       return super().demarrer() +" en moto"

    def informationsVehicule(self):
        return super().informationsVehicule() + f"nombre de roue : {self.get_roue()}"
    

voiture = Voiture()
moto = Moto()

voiture.set_marque("toyota")
voiture.set_modele("yaris")
voiture.set_annee(2015)
voiture.set_prix(30000)

moto.set_marque("Yamaha")
moto.set_modele("XSR900GP")
moto.set_annee(2024)
moto.set_prix(13199)


print(voiture.informationsVehicule())
print(moto.informationsVehicule())

print(voiture.demarrer())
print(moto.demarrer())
