import pygame, sys
from pygame.locals import *
import Classe as c
import csv
import random as r
import Stations_effects as se
import fonction as f

couleur = []


# test

list_of_player =[]           # liste des joueur
repas = c.Repas()           # classe pour avoir les repas actuels et précédents
item = []

nb_joueur = int(input("nombre de joueur "))

for loop in range(nb_joueur):    # donner la possibilité de s'inscrire si pas de compte
    pseudo = input("pseudo ")    # remplacer par la fonction check dans la fonction log in pas encore coder
    colour = input("colour ")
    list_of_player.append(c.joueur(pseudo,colour))

for player in list_of_player:
    player.yen = 7

r.shuffle(list_of_player)
player_turn = list_of_player[0]
case = None

nb_in_relais = 0

purple = (105, 37, 187)
blue = (12,115,178)
green = (13,106,5)
gray = (160,160,160)
orange = (218,85,4)


# setup
pygame.init()
clock = pygame.time.Clock()

# display
screen = pygame.display.set_mode((1920,1080))
img = pygame.image.load("IMAGE/piste.jpg")
board = pygame.image.load("IMAGE/piste.jpg")
board_rect = board.get_rect(topleft = [0,0])
pygame.mouse.set_visible(False)

moving = False

# crosshair
crosshair = c.Crosshair("IMAGE/Cursor/normal.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#plateau
case_board = []
with open('plateau.csv', newline= '') as boardread:
   spamreader = csv.reader(boardread, delimiter=',')
   for raw in spamreader:
      if raw == ['ï»¿']:
          pass
      else:
         case = c.station(int(raw[0]),raw[1],int(raw[2]),int(raw[3])-50,int(raw[4])-50,board)
         case.draw()
         case_board.append(case)

# bouton stat

bouton = pygame.image.load("IMAGE/egale.png")
bouton = pygame.transform.scale(bouton, (50,30))
bouton_rect = pygame.rect.Rect((50,125),(50,30))


display_stat = False
# jeu
while True: 
    f.legal_move(player_turn,case_board)
    font = pygame.font.Font(None, 40)
    font2 = pygame.font.Font(None, 40)
    for event in pygame.event.get():
         for case in case_board:
            if case.hit(board_rect.left ,moving) != False:
               se.station_effect(case.nom,player_turn,nb_in_relais,nb_joueur,item,repas)
               player_turn.position = case.num_case

         if pygame.mouse.get_pressed()[0] and bouton_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:
             display_stat = True
         elif event.type == MOUSEBUTTONDOWN and bouton_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:
             display_stat = False
         elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         elif event.type == MOUSEBUTTONDOWN:
           if board_rect.collidepoint(event.pos):
              moving = True 
         elif event.type == MOUSEBUTTONUP:          
              moving = False
         elif event.type == MOUSEMOTION and moving:
              board_rect.move_ip(event.rel) 
   
    pygame.display.flip()
    screen.fill((0,0,0))
    # fonction hit box
    board_rect.top = 0
    
    if board_rect.left > 0:
       board_rect.left = 0
    elif board_rect.right < 1920:
       board_rect.right = 1920

    board.blit(img,(0,0))
    screen.blit(board,board_rect)

    f.stat_player(player_turn, font2, colour, screen, display_stat)
    f.draw_player_stat(player_turn, font, colour, screen)
    screen.blit(bouton,(25,125))

    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(120)



    
    
   # coder la suite du jeu

pygame.quit()