#creer classe point avec des attributs x et y avec
# des methodes afficherPoint, afficherX, afficherY
# changerX et changerY


class Point:
    def __init__(self, x, y ):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"voici les coordonnées ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Voici la coordonné de x :  {self.x}")

    def afficherY(self):
        print(f"ceci est la coordonnées y : {self.y}")

    def changerX(self):
        X = input("veuillez entrer votre nouveaux x : ")
        self.x = X

    def changerY(self):
        Y = input("veuillez entrer votre nouveaux x : ")
        self.y = Y


coordonnées = Point(10, 5)

coordonnées.afficherX()
coordonnées.afficherY()

coordonnées.changerX()
coordonnées.changerY()

coordonnées.afficherX()
coordonnées.afficherY()

