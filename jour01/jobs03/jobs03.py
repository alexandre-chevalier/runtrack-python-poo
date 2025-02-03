#ajouter la methode addition a la classe operation

class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        return print("le resultat est : ",  resultat)

ope = Operation(10,5)

ope.addition()