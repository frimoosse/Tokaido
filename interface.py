import pygame, sys
from pygame.locals import *
import Classe as c
import csv
import random as r
import Stations_effects as se
import fonction as f

gamemode = "trajet retour"

# prérequis

character = ["Kinko","Sasayakko","Chuubei","Yoshiyasu","Satsuki","Mitsukuni","Hirotada","Umegae","Zen-emon","Hiroshige"]
r.shuffle(character)
relais = [1,15,28,42,55]
list_of_player =[]            # liste des joueur
repas = c.Repas()             # classe pour avoir les repas actuels et précédents
item = c.item()
if gamemode == "trajet retour":
   count = 4                    # numéro du prochain relais
else:
   count = 1
acc_mer = None                # accomplissement panorama
acc_montagne = None
acc_riziere = None

# setup des différentes couleurs

purple = c.Couleurs("purple",(105, 37, 187))
blue = c.Couleurs("blue",(12,115,178))
green = c.Couleurs("green",(13,106,5))
gray = c.Couleurs("gray",(160,160,160))
orange = c.Couleurs("orange",(218,85,4))
couleur =[purple, blue, green, gray, orange]

# setup position de départs
if gamemode == "trajet retour":
   coordx = 3560
   coordy = [196,260,330,395,463]
else:
   coordx = 195
   coordy = [694,762,826,890,954]

nb_joueur = int(input("nombre de joueur "))

if gamemode =="trajet retour":
   start = 55
else:
   start = 1

z = 0
for loop in range(nb_joueur):    # donner la possibilité de s'inscrire si pas de compte
    pseudo = input("pseudo ")    # remplacer par la fonction check dans la fonction log in pas encore coder
    print([purple.nom, blue.nom, green.nom, gray.nom, orange.nom])
    colour = int(input("colour"))
    colour = couleur[colour]
    list_of_player.append(c.joueur(pseudo, colour, coordx - 20, coordy[z] - 50, position=start))
    z += 1

r.shuffle(list_of_player)                 # mélange l'ordre de la liste des joueurs pour connaitre l'ordre du début     
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
         case = c.station(int(raw[0]),raw[1],int(raw[2]),int(raw[3])-50,int(raw[4])-50,board,raw[5])
         case.draw()
         case_board.append(case)

# bouton stat

bouton = pygame.image.load("IMAGE/egale.png")
bouton = pygame.transform.scale(bouton, (50,30))
bouton_rect = pygame.rect.Rect((50,125),(50,30))

display_stat = False       # affichage des stats du joueurs qui joue

# sttings
perso_choix = 0
prepa_done = 0

# jeu
game = True
for case in case_board:
    if gamemode == "trajet retour":
      if case.num_case == 55:
         for player in list_of_player:
            case.chara.append(player)
    else:
      if case.num_case == 1:
         for player in list_of_player:
            case.chara.append(player)


while game: 
    font = pygame.font.Font(None, 40)
    font2 = pygame.font.Font(None, 40)
    choix = []    
    if gamemode == "voyage initiatique" and perso_choix == 0:
      perso_choix = 1
      for player in list_of_player:
         player.yen = 7

    elif perso_choix == 0:
      a=0
      for player in list_of_player:
         type = []
         for b in range (2):
            query = "IMAGE/character/" + character[a+b] +".jpg"
            pos_x = 300 + 425*b
            pos_y = 249
            e = c.temporar_hitbox(query, pos_x, pos_y, (326,522), character[a+b], screen,True)
            e.nom = character[a+b]
            type.append(e)
         a += 2
         choice = True
         while choice:
            for event in pygame.event.get():
                        screen.fill((0,0,0))
                        for pla in list_of_player:                            # update les outils interactifs de l'interface
                            screen.blit(pla.img, (board_rect.left + pla.coord_x,pla.coord_y))
                        for sprite in type:
                            if sprite.hit() and sprite.enable == True:
                                choix.append(sprite.value)
                                choice = False

                        for sprite in type:
                            sprite.draw()

                        f.stat_player(player, font2, screen, display_stat)
                        f.draw_player_stat(player, font, screen)

                        crosshair_group.draw(screen)                          # update du cursor sur l'interface
                        crosshair_group.update()
                        clock.tick(60)
                        pygame.display.update()
                        
    if perso_choix == 0:
      a=0
      perso_choix = 1
      for player in list_of_player:
         with open('Character_list.csv', newline= '') as chararead:
               spamreader = csv.reader(chararead, delimiter=',')
               for raw in spamreader:
                  if raw == ['ï»¿']:
                     pass
                  elif raw[1] == choix[a]:
                     player.character = raw[1]
                     player.yen = int(raw[2])
         a += 1

    if gamemode == "preparatif" and prepa_done == 0:
      b = 2
      prepa_done = 1
      for a in range(nb_joueur):
         list_of_player[-(a+1)].yen += b
         if b != -1:
            b -= 1 


    player_turn = f.tour_du_joueur(list_of_player, case_board, gamemode)
    f.legal_move(player_turn, case_board, relais, count, gamemode)
    
    for event in pygame.event.get():
         for case in case_board:
            if case.hit(board_rect.left ,moving) != False:     # ation du jeu
               
               f.set_all_disable(case_board)                   # disable toute les stations

               screen.blit(board,board_rect)                   # update de la position du joueur sur le plateau
               f.pos_jeton( player_turn, case)
               for pla in list_of_player:                                              # la position du jeton
                  screen.blit(pla.img, (board_rect.left + pla.coord_x,pla.coord_y))
               pygame.display.update()

               se.station_effect(case.nom,player_turn,nb_in_relais,nb_joueur,item,repas,screen,font,font2,display_stat,crosshair_group,board,board_rect,list_of_player,gamemode)        # effet de la case

               f.change_pose(player_turn,case_board)           # changement de la position pour le jeu
               player_turn.position = case.num_case
               case.chara.append(player_turn)

         if pygame.mouse.get_pressed()[0] and bouton_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
             display_stat = True

         elif event.type == MOUSEBUTTONDOWN and bouton_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
             display_stat = False

         elif event.type == pygame.QUIT:       # fermer la fenêtre : ragequit
            pygame.quit()
            sys.exit()

         elif event.type == MOUSEBUTTONDOWN:             # commencer le déplacement du plateau
           if board_rect.collidepoint(event.pos):
              moving = True 

         elif event.type == MOUSEBUTTONUP:               # arret du deplacement de plateau
              moving = False

         elif event.type == MOUSEMOTION and moving:      # le plateau bouge suivant la souris
              board_rect.move_ip(event.rel) 
    if gamemode == "trajet retour":
      if str(count) != str(0):
         count = f.station_cap(list_of_player,relais,count,gamemode)      # test du changement de cap
      if str(count) != str(0):
         nb_in_relais = f.nb_jour_in_relais(list_of_player,relais,count)
    else:
       if str(count) != str(5):
         count = f.station_cap(list_of_player,relais,count,gamemode)      # test du changement de cap
       if str(count) != str(5):
         nb_in_relais = f.nb_jour_in_relais(list_of_player,relais,count)

    pygame.display.flip()           
    screen.fill((0,0,0))

    # fonction hit box
    board_rect.top = 0                                # garder le board sur le meme axe y
    
    if board_rect.left > 0:                                       # empecher le board d'aller trop loin a droite et a gauche
       board_rect.left = 0
    elif board_rect.right < 1920:
       board_rect.right = 1920

    board.blit(img,(0,0))                              # update du plateau
    screen.blit(board,board_rect)

    for pla in list_of_player:                            # update les outils interactifs de l'interface
      screen.blit(pla.img, (board_rect.left + pla.coord_x,pla.coord_y))
    f.stat_player(player_turn, font2, screen, display_stat)
    f.draw_player_stat(player_turn, font, screen)
    screen.blit(bouton,(25,125))

    crosshair_group.draw(screen)                          # update du cursor sur l'interface
    crosshair_group.update()
    clock.tick()                                          # FPS (frame per second)
    
    acc_mer,acc_montagne,acc_riziere = f.acc_pano(list_of_player,acc_mer,acc_montagne,acc_riziere)
        
    if f.fin_de_partie(list_of_player, nb_joueur, gamemode):
       game = False

# Distribution des accomplissement et des point de temple 
f.achievement_get(list_of_player,acc_mer,acc_montagne,acc_riziere)
#f.collection(list_of_player)   bug

list_of_player = f.ordre_final(list_of_player)     #  organiser dans l'ordre du premier au dernier
# debut du scoreboard final

img_scoreboard = pygame.image.load("IMAGE/decor/scoreboard.jpg")
font3 = pygame.font.Font(None, 55)
scoreboard = True
while scoreboard:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:      
         pygame.quit()
         sys.exit()
      if pygame.mouse.get_pressed()[2]:
         scoreboard = False
   screen.blit(img_scoreboard,(0,0))
   f.scoreboard(list_of_player,font3,screen)
   clock.tick(60)
   pygame.display.update()

# plus qu'a ajouter la victoire sur la BDD mais apres avoir forcer à ce connecter

pygame.quit()