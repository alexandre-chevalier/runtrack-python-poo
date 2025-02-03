#creer une classe animal avec attribut age et prenom
#

class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age +=1
    
    def nommer(self):
       prenom =  input("veuillez entrez le nom de votre animal ")
       self.prenom = prenom


animal = Animal()

print(animal.age)

animal.vieillir()

print(f"votre animal a :{animal.age} ans")

animal.nommer()

print(f"votre animal s'appelle {animal.prenom} ")
    