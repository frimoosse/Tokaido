# classe

class joueur ():
    def __init__ (self, pseudo, colour):
        self.pseudo = pseudo
        self.colour = colour
        self.character = None
        self.position = 1

        self.inventaire = []
        self.point = 0
        self.yen = 0
        self.offrande = 0

        self.panorama_mer = 0
        self.panorama_montagne = 0
        self.panorama_riziere = 0

    def Display_player (self):
        print("pseudo : ",self.pseudo,"\ncouleur : ",self.colour,"\npersonnage : ",self.character,"\npoint : ",self.point,"\npiece : ",self.yen,"\nnb panorama mer : ",self.panorama_mer,"\npanorama montagne : ",self.panorama_montagne,"\nnb panorama riziere : ",self.panorama_riziere)

class Repas():
    def __init__ (self):
        self.actuel = []
        self.precedent = []

class item():
    def __init__(self):
        self.allcard = []


        
    
