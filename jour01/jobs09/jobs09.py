class Produit:
    def __init__(self, nom, prixHt, tva):
        self.nom = nom
        self.prixHt = prixHt
        self.tva = tva
        self.prixTTC = self.CalculPrixTTC()
    
    def CalculPrixTTC(self):
        taxe = self.prixHt * (self.tva/100)
        prixTTC = self.prixHt + taxe
        return prixTTC
    
    def ret_tva(self):
        return self.tva
    
    def ret_prixHt(self):
        return self.prixHt 
    
    def ret_nom(self):
        return self.nom 
    
    def modif_nom(self,nom):

        self.nom = nom
        
    def modif_prix(self, prix):
        self.prix = prix



prod1 = Produit("alan wake", 79.99, 20)
prod2 = Produit("assassin's creed shadows", 15, 15)
prod3 = Produit("candy crush", 3, 100)
prod4 = Produit("angry birds", 5,30)

prod1.CalculPrixTTC()


print(prod1.CalculPrixTTC())

prod1.modif_nom("alan wake 2")
prod1.modif_prix(89.99)


print(prod1.nom)
print(prod1.prix)
print(prod1.prixTTC)






