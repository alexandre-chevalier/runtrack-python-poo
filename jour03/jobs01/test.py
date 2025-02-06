class ClasseA:
    def __init__(self, message):
        self.message = message

    def afficher_message(self):
        print(self.message)


class ClasseB:
    def __init__(self):
        self.obj_a = None  # Initialisation à None

    def creer_instance_de_A(self, message):
        self.obj_a = ClasseA(message)  # Instanciation de ClasseA
        self.obj_a.afficher_message()  # Appel d'une méthode de ClasseA


# Utilisation
b = ClasseB()
b.creer_instance_de_A("Hello depuis ClasseA !")