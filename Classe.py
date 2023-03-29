# classe

class joueur ():
    def __init__ (self, pseudo, colour):
        self.pseudo = pseudo
        self.colour = colour
        self.character = None
        self.position = 1

        self.point = 0
        self.yen = 0

        self.panorama_mer = 0
        self.panorama_montagne = 0
        self.panorama_riziere = 0

    def Display_player (self):
        print(self.pseudo,self.colour,self.character,self.point,self.yen,self.panorama_mer,self.panorama_montagne,self.panorama_riziere)
