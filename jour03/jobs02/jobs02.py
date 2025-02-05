class CompteBancaire:
    def __init__(self,numeroDeCompte, nom, prenom, solde, decouvert ):
        self.__numeroDeCompte = numeroDeCompte
        self.__nom = nom
        self.__prenom =prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def get_numero_compte(self):
        return self.__numeroDeCompte
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde

    def get_decouvert(self):
        return self.__decouvert
    
    def set_numero_compte(self, compte):
        self.__numeroDeCompte =  compte

    def set_nom(self, nom):
        self.__nom = nom

    def set_prenom(self, prenom):
        self.__prenom = prenom
    
    def set_solde(self, solde):
        self.__solde = solde

    def afficher(self):
        print(f"ceci est le compte n° : {self.get_numero_compte()} de mr/mme : {self.get_nom()} {self.get_prenom()}")

    def afficherSolde(self):
        print(f"votre compte contient : {self.get_solde()}")

    def versement(self, versement):
        solde = self.get_solde()
        solde += versement
        self.set_solde(solde)
        print(self.get_solde())

    def retrait(self, retrait):
        solde = self.get_solde()
        decouvert = self.get_decouvert()
        if decouvert == False and retrait > solde:
            print("vous ne pouvez pas retirer d'argent")
            print(solde)
        else:
            solde -= retrait
            self.set_solde(solde)
            print(self.get_solde())

    def agios(self):
        solde  = self.get_solde ()
        agios = 20
        if solde < 0 :
            solde -= agios
            self.set_solde(solde)
            print(f"nous vous avons pris les agios pour un montant de : {agios}")
            print(f"votre solde est de {solde}")

    def virement(self, compte, montant):
        solde = self.get_solde()
        solde2 = compte.get_solde()

        if montant > solde and self.get_decouvert() == False:
            print("vous n'avez pas les ressources necessaire pour effectuer ce virement")
        else:
            print(solde)
            solde -= montant
            self.set_solde = solde
            print(solde)
            print(solde2)
            solde2 += montant
            compte.set_solde = solde2
            print(solde2)
            
        


    


compte = CompteBancaire(1,"chevalier", "alexandre", 75000, False)
compte.afficher()
compte.afficherSolde()
compte.versement(15000)
compte.retrait(30000)

compte2 = CompteBancaire(2,"leca", "antoine", -15000, True)
compte2.afficher()
compte2.afficherSolde()
compte2.agios()

compte.virement(compte2, 15020)
