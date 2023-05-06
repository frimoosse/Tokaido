# classe
import Card_effect_rencontre as cer
import fonction as f
import random as r
import csv
#import Main  il ne faut pas import main n'y voyage initiatique
import pygame
import sys

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
        return [self.yen,self.panorama_mer,self.panorama_montagne,self.panorama_riziere,self.offrande]

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
    def update (self):
        self.rect.center = pygame.mouse.get_pos()

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
    def __init__(self, num_case, nom, place, pos_x, pos_y,board):
        # pour le jeu
        self.num_case = num_case
        self.nom = nom
        self.place = place
        self.chara = []     # nombre de personne sur la case <= self.place
        # pour l'interface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos = (pos_x,pos_y)
        self.board = board
        self.enable = True 
        
    def draw(self):
        station_hitbox = pygame.surface.Surface((100,100))
        self.board.blit(station_hitbox,self.pos)

    def hit (self, a, moving):
        cursor_position = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        station_hitbox = pygame.rect.Rect((a + self.pos_x,self.pos_y),(100,100))
        if left_click and station_hitbox.collidepoint(cursor_position) and self.enable and not moving:
            print(self.nom)
            return self.nom
        else:
            return False


# test
class temple(station):
    def effect (player, repas,items,nb_joueur):
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
    def effect (self, player, repas, items, nb_joueur) :
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

class source (station):
    def effect (self, player, repas, items, nb_joueur):
        pt = r.randint(2,3)
        player.point += pt
        if player.character == "Mitsukuni":
            player.point += 1

class riziere (station):
    def effect (self, player, repas, items, nb_joueur):
        rencontre = 'Annaibito Rizière'
        cer.effet(rencontre,player)

class montagne (station):
    def effect (self, player, repas, items, nb_joueur):
        rencontre = 'Annaibito Montagne'
        cer.effet( rencontre ,player)

class mer (station):
    def effect (self, player, repas, items, nb_joueur):
        rencontre = 'Annaibito Mer'
        cer.effet(rencontre,player)

class ferme (station):
    def effect (self, player, repas, items, nb_joueur):
        player.yen += 3

class relais (station):
    def effect (self, player, repas, items, nb_joueur):
        if player.character == "Chuubei":
            p=[]
            pioche = f.pioche(1,"rencontre",p)[0]
            print(pioche)
            cer.effet(pioche[0],player)
        if player.character == "Hiroshige":
            ask = int(input("which panorama choice ? "))
            if ask == 1:
                rencontre = 'Annaibito Mer'
                cer.effet(rencontre,player)
            elif ask == 2:
                rencontre = 'Annaibito Montagne'
                cer.effet( rencontre ,player)
            elif ask == 3:
                rencontre = 'Annaibito Rizière'
                cer.effet(rencontre,player)


        if Main.gastronomie and relais == 0:                                            # 
            repas.actuel,poi = (f.pioche(nb_joueur,"repas",repas.precedent))            # Si Gastronomie ###############
            for a in range (len(repas.actuel)):                                         #
                repas.precedent.append(poi[a])  

        elif relais == 0:
            repas.actuel,poi = (f.pioche(nb_joueur+1,"repas",repas.precedent))
            for a in range (len(repas.actuel)):
                repas.precedent.append(poi[a])

        
        
        choix = 0
        while choix != -2:
            print(repas.actuel)
            
            choix = int(input("repas choisi"))

            if choix == -1:
                return

            with open('repas.csv') as repas2:                      
                csv_reader = csv.reader(repas2, delimiter = ',')
                nom_repas = repas.actuel[choix]
                for row in csv_reader:
                    if str(nom_repas) == row[0]:
                        prix = row[1]

            if player.character == "Kinko":
                if (int(prix)-1) <= player.yen:
                    del(repas.actuel[choix])
                    player.point += 6
                    player.yen -= (int(prix)-1)
                    choix = -2
                    
            else:
                if int(prix) < player.yen:
                    del(repas.actuel[choix])
                    player.point += 6
                    player.yen -= int(prix)
                    choix = -2

class echoppe (station):
    def effect (self, player, repas, items, nb_joueur):
        achat = []
        pioche_memory =[]
        pioche,memoire = f.pioche(3,station,items.allcard)
        for it in pioche:
            pioche_memory.append(it)
        items.allcard.append(memoire)
        print(pioche)
        choix = int(input("quel item? " ))
        if choix != -1:
            achat.append(pioche[choix])
            del(pioche[choix])
            print(pioche)
            choix = int(input("autre item ? "))
            if choix != -1:
                achat.append(pioche[choix])
                del(pioche[choix])
                print(pioche)
                choix = int(input("un dernire item ? "))
                if choix != -1:
                    achat.append(pioche[choix])
        prix = 0
        with open('List_souvenirs.csv') as souvenir:                      
            csv_reader = csv.reader(souvenir, delimiter = ',')
            for row in csv_reader:
                for count in achat:
                    nom_souvenir = str(count)
                    if str(nom_souvenir) == row[1]:
                        prix += int(row[2])
        if prix > player.yen:
            achat = -2
            pioche = []
            for it in pioche_memory:
                pioche.append(it)
        while achat == -2:
            achat = []
            print("voux n'avez pas assez d'argent")
            print(pioche)
            choix = int(input("quel item? " ))
            if choix != -1:
                achat.append(pioche[choix])
                del(pioche[choix])
                print(pioche)
                choix = int(input("autre item ? "))
                if choix != -1:
                    achat.append(pioche[choix])
                    del(pioche[choix])
                    print(pioche)
                    choix = int(input("un dernire item ? "))
                    if choix != -1:
                        achat.append(pioche[choix])
            
            prix = 0
            with open('List_souvenirs.csv') as souvenir:                      
                csv_reader = csv.reader(souvenir, delimiter = ',')
                for row in csv_reader:
                    for count in achat:
                        nom_souvenir = str(count)
                        if str(nom_souvenir) == row[1]:
                            prix += int(row[2])
            if prix > player.yen:
                achat = -2
                pioche = []
                for it in pioche_memory:
                    pioche.append(it)

        
        player.yen -= prix
        player.inventaire.append(achat)