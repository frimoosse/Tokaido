# fonction

# pioche

import mysql.connector as mysql
import random
import csv
import pygame


def pioche (nb_carte_pioche, case_type,piocher):

    conn = mysql.connect(host = "127.0.0.1",
                     user = "root", password="root",
                     database="tokaido")

    cursor = conn.cursor()
    cursor_bis = conn.cursor()

    query_1 = "SELECT COUNT(*) FROM " + case_type

    cursor_bis.execute(query_1)

    for items in cursor_bis:
        lg = items[0]

    id = []
    b=[]
    count= 0
    while count < nb_carte_pioche:
        loop = True
        while loop:
            pioche_rd = [random.randint(1,lg)]
            query_2 = "SELECT * FROM " + case_type + " WHERE id_" + case_type + " = %s "

            cursor.execute(query_2 , pioche_rd)
            for items in cursor:
                if items[1] not in b:
                    if items[0] not in piocher:
                        b.append(items[1])
                        id.append(items[0])
                        count += 1
                        loop = False
        
    cursor.close()
    conn.close()
    return(b,id)

def check_panorama(player,case):
    if player.panorama_mer >= 5 and case == "mer" :
        return True
    elif player.panorama_montagne >= 4 and case == "montagne":
        return True
    elif player.panorama_riziere >= 3 and case == "riziere":
        return True
    else:
        return False

def preparatifs(list_of_player):        # liste des joueurs triée dans l'ordre de départ #########################
    y = 2
    for player in reversed(list_of_player) :
        player.yen += y
        if y != -1 :
            y -= 1

def inventory_count(player):
    loop = True
    while loop:
        collection = []
        if player.inventory == []:
            loop = False
        a=0
        for item in player.inventory:
            if item.type not in collection:
                collection.append(item.type)
                del(player.inventory[a])
            a += 1
        if collection != []:
            player.point += 1 + 2*len(collection-1)  # player derive seconde # suite AHRItmétique

def draw_player_stat(player, font, colour, screen):
    img = font.render(str(player.pseudo) + " " + str(player.point) + "pts",True, (0,0,0))
    pygame.draw.circle(screen,(105, 37, 187),(50,50), 75)        # couleur = player.colour
    pygame.draw.rect(screen,(105, 37, 187),(0,0,400,50))
    pygame.draw.circle(screen,(105, 37, 187),(400,0),50 )
    screen.blit(img, (150,10) )

def stat_player(player, font, colour, screen,display):
    stat_list = player.Display_player()
    list_carte = []
    list_carte2 = []
    list_carte.append(pygame.image.load("IMAGE/Yen.png"))
    list_carte.append(pygame.image.load("IMAGE/panorama/mer/dos.jpeg"))
    list_carte.append(pygame.image.load("IMAGE/panorama/montagne/dos montagne.jpeg"))
    list_carte.append(pygame.image.load("IMAGE/panorama/riziere/dos riziere.jpeg"))
    for b in range (len(stat_list)-1):
        if b != 0:
            img2 = pygame.transform.scale(list_carte[b], (50,80))
            list_carte2.append(img2)
        else:
            img2 = pygame.transform.scale(list_carte[b], (50,50))
            list_carte2.append(img2)

    if display:
        pygame.draw.rect(screen,(105, 37, 187), (0,100,100,450))
        for a in range (len(stat_list)-1):
            img = font.render(str(stat_list[a]),True,(0,0,0))
            screen.blit(list_carte2[a],(5,175+a*90))
            screen.blit(img,(75,185+a*90))

def legal_move (player,board):
    for station in board:
        if player.yen == 0:
            if station.nom == "echoppe":
                station.enable = False
            if station.nom == "temple":
                station.enable = False
        elif player.panorama_mer == 5 and station.nom == "mer":
            station.enable = False
        elif player.panorama_montagne == 4 and station.nom == "montagne":
            station.enable = False
        elif player.panorama_riziere == 3 and station.nom == "riziere":
            station.enable = False
        elif player.position >= station.num_case:
            station.enable = False
        else:
            station.enable = True
