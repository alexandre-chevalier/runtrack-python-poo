## creer une classe presentation qui a des attributs nom et prenom

class Presentation:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        print(f"vous etes : {self.nom} {self.prenom}")

pres1 = Presentation("chevalier", "alexandre")
pres2 = Presentation("Ponce", "emilie")
pres3 = Presentation("leca", "antoine")

pres1.sePresenter()
pres2.sePresenter()
pres3.sePresenter()