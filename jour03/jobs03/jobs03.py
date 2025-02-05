class Tache:
    def __init__(self, titre, description, statut):
        self.__titre = titre 
        self.__description = description
        self.__statut = statut

    def get_titre(self):
        return self.__titre
    
    def get_description(self):
        return self.__description

    def get_statut(self):
        return self.__statut
    
    def set_statut(self, statut):
        self.__statut = statut
    
    
    def set_titre(self, titre):
        self.__titre = titre

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return f"Titre: {self.get_titre()}, Description: {self.get_description()}, Statut: {self.get_statut()}"   

    def __repr__(self):
        return self.__str__()

    
class ListeDeTache:
    def __init__(self):
        self.__liste = []

    def get_liste(self):
        return self.__liste
    
    def set_liste(self, liste):
        self.__liste = liste

    def ajouterTache(self, tache):
        liste = self.get_liste()
        liste.append(tache)
        self.set_liste(liste)   

    def suprimmerTache(self, tache):
        liste = self.get_liste()
        if tache in liste:
            liste.remove(tache)
        self.set_liste(liste)

    def marquerCommeFinie(self,tache):
        tache.set_statut("terminé")

    def afficherListe(self, liste):
        for i in liste.get_liste():
            print(i)

    def filterListe(self, liste):
       taches = liste.get_liste()
       for i in taches:
            if i.get_statut() == "a faire":
                print(i)








tache1 = Tache("faire la vaisselle", "nettoyer les fourchettes du repas", "a faire")
tache2 = Tache("voyager", "vister des pays", "a faire")
tache3 = Tache("faire du shopping", "acheter des jeans", "terminé")
tache4 = Tache("jouer aux jeux videos", "faire ff8", "a faire")
liste = ListeDeTache()


liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)
liste.ajouterTache(tache4)
liste.suprimmerTache(tache1)

liste.ajouterTache(tache1)
liste.marquerCommeFinie(tache1)
##liste.afficherListe(liste)
liste.filterListe(liste)




