# classe
import Card_effect_rencontre as cer
import fonction as f
import random as r
import csv
import pygame
import sys

class joueur ():
    def __init__ (self, pseudo, colour, coord_x, coord_y, character = None, position = 1):
        self.pseudo = pseudo
        self.colour = colour
        prompt = "IMAGE/" + str(colour.nom) + ".png"
        self.character = character
        self.img = pygame.image.load(prompt)
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.position = position

        self.inventaire = []
        self.repas = []
        self.point = 0
        self.yen = 0
        self.offrande = 0
        self.source = 0
        self.rencontre = 0

        self.panorama_mer = 0
        self.panorama_montagne = 0
        self.panorama_riziere = 0

    def Display_player (self):
        return [self.yen,self.panorama_mer,self.panorama_montagne,self.panorama_riziere,self.offrande]
    
class Couleurs():
    def __init__(self, nom, clef):
        self.nom = nom
        self.clef = clef

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
    def update (self):
        self.rect.topleft = pygame.mouse.get_pos()

class Repas():
    def __init__ (self):
        self.actuel = []
        self.precedent = []

class item ():
    def __init__(self):
        self.actuel = []
        self.allcard = []
        
class station():
    def __init__(self, num_case, nom, place, pos_x, pos_y,board,sens):
        # pour le jeu
        self.num_case = num_case
        self.nom = nom
        self.place = place
        self.chara = []     
        self.sens = sens

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
            return self.nom
        else:
            return False

class temporar_hitbox():
    def __init__(self,img,pos_x,pos_y,scale,value,screen,enable = True, nom = None):
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (scale))
        self.scale = scale
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.value = value
        self.screen = screen
        self.enable = enable
        self.nom = nom

    def draw(self):
        self.screen.blit(self.img,(self.pos_x,self.pos_y))
        

    def hit(self):
        hitbox = pygame.rect.Rect((self.pos_x,self.pos_y),self.scale)
        if pygame.mouse.get_pressed()[0] and hitbox.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False