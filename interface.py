import pygame, sys
from pygame.locals import *
import Classe as c
import csv
import random as r

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
         print (raw)
         case = c.station(int(raw[0]),raw[1],int(raw[2]),int(raw[3])-50,int(raw[4])-50,board)
         case.draw()
         case_board.append(case)
# jeu
while True: 
    for event in pygame.event.get():
         for case in case_board:
            if case.hit(board_rect.left ,moving) != False:
               case.effect(player_turn,repas,item,nb_joueur)

         if event.type == pygame.QUIT:
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

    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(244)



    
    
   # coder la suite du jeu

pygame.quit()