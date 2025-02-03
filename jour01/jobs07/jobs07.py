class Personnage:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def gauche(self):
        self.x -=1

    def droite(self):
        self.x +=1

    def haut(self):
        self.y +=1

    def bas(self):
        self.y -=1

    def position(self):
        return (self.x, self.y)
    

perso_dep = Personnage()

print(perso_dep.position())

perso_dep.bas()
perso_dep.droite()

print(perso_dep.position())

perso_dep.haut()
perso_dep.gauche()

print(perso_dep.position())

perso_dep.haut()
perso_dep.gauche()

print(perso_dep.position())

