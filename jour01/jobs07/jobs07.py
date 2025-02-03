class Personnage:
    def __init__(self):
        self.x = 2
        self.y = 2
        self.tab = [
            ["-","","","","","",""],
            ["-","","","","","",""],
            ["-","","","","","",""],
            ["-","","","","","",""],
            ["-","","","","","",""]
        ]
    
    def gauche(self):
        self.tab[self.x][self.y] ="-"
        self.x -=1

    def droite(self):
        self.tab[self.x][self.y] ="-"
        self.x +=1

    def haut(self):
        self.tab[self.x][self.y] ="-"
        self.y +=1

    def bas(self):
        self.tab[self.x][self.y] ="-"
        self.y -=1

    def position(self):
        self.tab[self.x][self.y] ="-"
        self.tab[self.x][self.y] ="P"
        print(self.tab, end="")

perso_dep = Personnage()

print(perso_dep.position())

perso_dep.bas()
perso_dep.droite()

print(perso_dep.position())

perso_dep.haut()
perso_dep.gauche()

