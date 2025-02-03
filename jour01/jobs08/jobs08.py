import math

class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon
    
    def changerRayon(self, rayon):
        self.rayon = rayon

    def circonference(self, ):
        circ = 2 * math.pi * self.rayon
        print(circ)
        return circ
    
    def aire(self):
        aire = math.pi * (self.rayon * self.rayon)
        print(aire)
        return aire
    
    def diametre(self):
        diametre = self.rayon * 2
        print(diametre)
        return diametre
    
    def afficherInfos(self, circ, aire, diametre):
        print(f"votre cerlce a pour circonference : {circ}")
        print(f"une aire de : {aire}")
        print(f"et un diametre de : {diametre}")

cercle1 = Cercle(4)
cercle2 = Cercle(7)

aire = cercle1.aire()
circ = cercle1.circonference()
diam = cercle1.diametre()

cercle1.afficherInfos(circ, aire, diam)


aire2 = cercle2.aire()
circ2 = cercle2.circonference()
diam2 = cercle2.diametre()

cercle1.afficherInfos(circ2, aire2, diam2)