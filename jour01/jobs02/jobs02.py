# avec la classe precedente print la valeur des attributs n1 et n2

class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2


ope = Operation(10,5)

print("ceci est le nombre1 : ", ope.nombre1)
print("ceci est le nombre2 : ",  ope.nombre2)