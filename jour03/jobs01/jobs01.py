class Ville:
    def __init__(self, nom, nombre_habitant):
        self.__nom = nom
        self.__nombre_habitant = nombre_habitant
    
    def get_nom_ville(self):
        return self.__nom
    
    def get_nombre_habitant(self):
        return self.__nombre_habitant
    
    def set_habitant(self,habitant ):
        self.__nombre_habitant = habitant
    

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville
    
    def ajouter_population(self, habitant):
        habitant +=1

        return habitant
    

ville = Ville("paris", 1000000)
ville2 = Ville("Marseille", 861635)
print(f"la population de la ville de {ville.get_nom_ville()} est de : {ville.get_nombre_habitant()}")
print(f"la population de la ville de {ville2.get_nom_ville()} est de : {ville2.get_nombre_habitant()}")


perso1 = Personne("john", 45, ville)
perso2 = Personne("Myrtille",4, ville)
perso3 = Personne("Chloé",45, ville2)

print(ville.set_habitant(perso1.ajouter_population(perso1.get_ville().get_nombre_habitant())))
print(ville.set_habitant(perso2.ajouter_population(perso2.get_ville().get_nombre_habitant())))
print(ville2.set_habitant(perso3.ajouter_population(perso3.get_ville().get_nombre_habitant())))


print(f"la population de la ville de {ville.get_nom_ville()} est de : {ville.get_nombre_habitant()}")
print(f"la population de la ville de {ville2.get_nom_ville()} est de : {ville2.get_nombre_habitant()}")