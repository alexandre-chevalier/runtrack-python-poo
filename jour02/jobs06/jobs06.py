class Commande:
    def __init__(self, commande, statut, tva):
        self.__commande_num = commande
        self.__liste_commande = {}
        self.__statut = statut
        self.__tva = tva

    def get_num_commande(self):
        return self.__commande_num

    def get_plat_commande(self):
        return self.__liste_commande
    
    def get_status(self):
        return self.__statut
    
    def get_num_commande(self):
        return self.__commande_num

    def get_tva(self):
        return self.__tva

    def ajout_plat(self, numero, nom, prix, status):
        plat = self.get_plat_commande()
        if numero not in plat:
            plat[numero] = []
        
        plat[numero].append({
            "nom": nom,
            "prix": prix,
            "status": status
        })
    
    def _total_commande(self,liste):
        liste = self.get_plat_commande()
        total= 0
        for i in liste:
            for j, char in enumerate(liste[i]):
                total += liste[i][j]["prix"]
        
        return total
    
    def calcul_tva(self):
        totalHt = self._total_commande(self.get_plat_commande)
        tva = totalHt * (self.get_tva()/100)
        totalTTC = totalHt + tva
        return totalTTC
               
        
commande= Commande(1,"en cours",20)   
commande.ajout_plat(commande.get_num_commande(),"lasagne",10, "en cours")
commande.ajout_plat(commande.get_num_commande(),"bolognaise",50, "en cours")
commande.ajout_plat(commande.get_num_commande(),"pate a la carbonara",150, "en cours")
print(f"votre commande coute : {commande.calcul_tva()}")






"""plat = {}

def ajout_plats(plat, numero, nom, prix, status):
    if numero not in plat:
        plat[numero] = []
    
    plat[numero].append({
        "nom": nom,
        "prix": prix,
        "status": status
    })
    return plat

ajout_plats(plat, 1, "lasagne",10, "en cours" )
list_plats = ajout_plats(plat, 1, "bolognaise",20, "en cours" )

def changer_valeur(plats):
    for i in plats:
        for j, char in enumerate(plats[i]):
            print(plats[i][j]["prix"])

changer_valeur(list_plats)
"""


