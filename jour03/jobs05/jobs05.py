import random

class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie

    def get_nom(self):
        return self.__nom
    
    def get_vie(self):
        return self.__vie
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_vie(self, vie):
        self.__vie = vie

    def attaquer(self,joueur):
        j = joueur.get_vie() 
        j -= 10
        joueur.set_vie(j)
    
    def __str__(self):
        return f"""Le nom du joueur est {self.get_nom()} et ses points de vie {self.get_vie()}"""   

    def __repr__(self):
        return self.__str__()


class Jeu:
    def __init__(self):
        self.__joueur = None
        self.__ennemie = None


    def get_joueur(self):
        return self.__joueur
    
    def set_joueur(self, joueur):
        self.__joueur = joueur
    
    def get_ennemie(self):
        return self.__ennemie
    
    def set_ennemie(self, ennemie):
        self.__ennemie = ennemie
    
    

    def ChoisirNiveaux(self):
        print("""              
                1 : facile
                2 : normal 
                3 : difficile
                """)
        choix = int(input("veuillez choisir un niveaux de difficulté : "))
        
        vieJoueur = None
        vieEnnemie = None
        if choix == 1:
            vieJoueur = 100
            vieEnnemie = 80
        elif choix == 2:
            vieJoueur = 95
            vieEnnemie = 100
        elif choix == 3:
            vieJoueur = 90
            vieEnnemie = 150

        return vieJoueur, vieEnnemie
    
    def lancerJeu(self, PdV):
        print(PdV)
        joueur = Personnage("squall", PdV[0])
        ennemie = Personnage("ultimecia",PdV[1])

        self.set_joueur(joueur)
        self.set_ennemie(ennemie)

    def fin_de_Partie(self, PdVj, pdvE):
        if PdVj <=0 and pdvE > 0:
            print("joueur, vous avez perdu")
        if pdvE <=0 and PdVj > 0:
            print("joueur, vous avez perdu")


        

jeu = Jeu()

PdV = jeu.ChoisirNiveaux()

jeu.lancerJeu(PdV)

joueur = jeu.get_joueur()

ennemie = jeu.get_ennemie()
print(ennemie)
print(joueur)
ennemie.attaquer(joueur)
joueur.attaquer(ennemie)
ennemie.attaquer(joueur)
ennemie.attaquer(joueur)
ennemie.attaquer(joueur)
ennemie.attaquer(joueur)
ennemie.attaquer(joueur)
ennemie.attaquer(joueur)
ennemie.attaquer(joueur)
ennemie.attaquer(joueur)
ennemie.attaquer(joueur)

pdvEnnemie = ennemie.get_vie()
PdvJoueur = joueur.get_vie()

jeu.fin_de_Partie(PdvJoueur, pdvEnnemie)






