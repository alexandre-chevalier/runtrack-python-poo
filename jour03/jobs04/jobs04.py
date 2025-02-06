class joueur:
    def __init__(self, nom, prenom, position ):
        self.__nom      = nom 
        self.__prenom   = prenom
        self.__position = position
        self.__nombre_but = 0 
        self.__passes_dec = 0
        self.__carton_jaune = 0
        self.__carton_rouge = 0

    def get_nom(self):
        return self.__nom
        
    def get_prenom(self):
        return self.__prenom
        
    def get_position(self):
        return self.__position
        
    def get_but(self):
        return self.__nombre_but
        
    def get_passes_dec(self):
        return self.__passes_dec

    def get_carton_jaune(self):
        return self.__carton_jaune

    def get_carton_rouge(self):
        return  self.__carton_rouge
    
    def set_nom(self, nom):
        self.__nom = nom
        
    def set_prenom(self, prenom):
        self.__prenom = prenom
        
    def set_position(self,position):
        self.__position = position
        
    def set_but(self,but):
        self.__nombre_but = but
        
    def set_passes_dec(self, passeDec):
        self.__passes_dec = passeDec

    def set_carton_jaune(self, jaune):
        self.__carton_jaune = jaune

    def set_carton_rouge(self, rouge):
        self.__carton_rouge = rouge

    def marquerUnBut(self):
        buts = self.get_but()
        buts += 1
        self.set_but(buts)

    def passeDecisiveEffectué(self):
        passeD = self.get_passes_dec()
        passeD += 1
        self.set_passes_dec(passeD)
    
    def avoirCartonJaune(self):
        carton = self.get_carton_jaune()
        carton +=1
        self.set_carton_jaune(carton)

    def avoirCartonRouge(self):
        nombreCarton= self.get_carton_rouge()
        nombreCarton += 1
        self.set_carton_Rouge(nombreCarton)

    def afficherStatistique(self):
        print(f"""
                nom: {self.get_nom()}
                prenom: {self.get_prenom()}
                position: {self.get_position()}
                but: {self.get_but()}
                passe decisive: {self.get_passes_dec()}
                nombre de carton jaune: {self.get_carton_jaune()}
                nombre de carton rouge: {self.get_carton_rouge()}
                """)
        
    def __str__(self):
        return f"""nom: {self.get_nom()}, prenom: {self.get_prenom()}, position: {self.get_position()}
                nombre de but: {self.get_but()}, passe decisive: {self.get_passes_dec()},
                carton jaune:{self.get_carton_jaune()}, carton rouge:{self.get_carton_rouge()}"""   

    def __repr__(self):
        return self.__str__()



class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__liste_equipe = []

    def get_nom(self):
        return self.__nom
    
    def get_liste_equipe(self):
        return self.__liste_equipe

    def set_nom(self, nom):
        self.__nom = nom

    def set_equip(self, equipe):
        self.__liste_equipe = equipe


    def ajouterJoueur(self, joueur):
        liste = self.get_liste_equipe()
        liste.append(joueur)
        self.set_equip(liste)

    def afficherStatJoueur(self):
        listeJoueur= self.get_liste_equipe()
        for i in listeJoueur:
            print(f"""
                nomEquipe: {self.get_nom()}
                nom: {i.get_nom()}
                prenom: {i.get_prenom()}
                position: {i.get_position()}
                but: {i.get_but()}
                passe decisive: {i.get_passes_dec()}
                nombre de carton jaune: {i.get_carton_jaune()}
                nombre de carton rouge: {i.get_carton_rouge()}
                """)
            
    def mettreAJourStat(self, joueur):
        liste = self.get_liste_equipe()
        if joueur in liste
                self.

        

        


equipe  = Equipe("OM")
equipe2 = Equipe("Psg")

joueur1 = joueur("mbappe","kylian","ailier droit")
joueur2 = joueur("griezmann","antoine","attaquant")
joueur3 = joueur("rabiot","adrien","ailier gauche")
joueur4 = joueur("benzema","karim","attaquant")

equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)

equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)

equipe.afficherStatJoueur()
equipe2.afficherStatJoueur()

equipe.afficherStatJoueur()
equipe2.afficherStatJoueur()


joueur1.marquerUnBut()

joueur2.avoirCartonJaune()
joueur2.avoirCartonJaune()
joueur2.avoirCartonJaune()
joueur2.avoirCartonJaune()
joueur2.avoirCartonJaune()

equipe.mettreAJourStat(joueur2)
