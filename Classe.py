# classe
import Card_effect_rencontre as cer
import fonction as f

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
    def __init__ (self, nom, type, prix):
        self.nom = nom
        self.type = type
        self.prix = prix

class defausse ():
    def __init__(self):
        self.allcard = []


        
class station():
    def __init__(self, nom, place):
        self.nom = nom
        self.place = place
        self.chara = []     # nombre de personne sur la case <= self.place

class temple (station):
    def effect (player):
        offrande = int(input("nombre de piece a offrir"))
        while offrande > player.yen:
            offrande = int(input("nombre de piece a offrir"))
        if player.character == "hirotada":
            choix = int(input(" +1 piece ? (0 ou 1, 1 = oui)"))
            offrande += choix
        player.yen -= offrande
        player.offrande += offrande
        player.point += offrande

class rencontre (station):
    def effect (player) :
        if player.character == "Yoshiyasu":
            p=[]
            pioche = f.pioche(2,station,p)[0]
            print(pioche)
            choix =int(input("quel carte ?"))
            cer.effet(pioche[choix],player)
        else : 
            p=[]
            pioche = f.pioche(1,station,p)[0]
            print(pioche)
            cer.effet(pioche[0],player)

        if player.character == "Umegae":
            player.yen += 1
            player.point += 1