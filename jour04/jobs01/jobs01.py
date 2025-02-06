class Personne:
    def __init__(self):
        self.age = 14
    
    def AfficherAge(self):
        return self.age

    def Bonjour(self):
        return print("Bonjour")

    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):

    def allerEnCours(self):
        print("je vais en cours")

    def AfficherAge(self):
        print(f"j'ai {super().AfficherAge()} ans")

    def bonjour(self):
        super().Bonjour()

class Professeur(Personne):
    def __init__(self):
        self.__matiereEnseignee = "anglais"

    def enseigner(self):
        print("Le cours va commencer")
    
    def bonjour(self):
        super().Bonjour()



eleve = Eleve()
prof = Professeur()


eleve.AfficherAge()




