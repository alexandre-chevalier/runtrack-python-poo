## on doit creer une classe operation, l'instancier et la print sur l'ecran

class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2


ope = Operation(10,5)

print(ope)