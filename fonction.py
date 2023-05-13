# fonction

# pioche

import mysql.connector as mysql
import random
import csv
import pygame
import Classe as c


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

def draw_player_stat(player, font, screen):
    img = font.render(str(player.pseudo) + " " + str(player.point) + "pts",True, (0,0,0))
    pygame.draw.circle(screen,player.colour.clef,(50,50), 75)        # couleur = player.colour
    pygame.draw.rect(screen,player.colour.clef,(0,0,400,50))
    pygame.draw.circle(screen,player.colour.clef,(400,0),50 )
    screen.blit(img, (150,10) )

def stat_player(player, font, screen,display):
    stat_list = player.Display_player()
    list_carte = []
    list_carte2 = []
    list_carte.append(pygame.image.load("IMAGE/Yen 1.png"))
    list_carte.append(pygame.image.load("IMAGE/panorama/mer/dos.jpeg"))
    list_carte.append(pygame.image.load("IMAGE/panorama/montagne/dos.jpeg"))
    list_carte.append(pygame.image.load("IMAGE/panorama/riziere/dos.jpeg"))
    for b in range (len(stat_list)-1):
        if b != 0:
            img2 = pygame.transform.scale(list_carte[b], (50,80))
            list_carte2.append(img2)
        else:
            img2 = pygame.transform.scale(list_carte[b], (50,50))
            list_carte2.append(img2)

    if display:
        pygame.draw.rect(screen,player.colour.clef, (0,100,100,450))
        for a in range (len(stat_list)-1):
            img = font.render(str(stat_list[a]),True,(0,0,0))
            screen.blit(list_carte2[a],(5,175+a*90))
            screen.blit(img,(75,185+a*90))

def legal_move (player, board, relais, count, gamemode):
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
        elif len(station.chara) == station.place:
            station.enable = False

        if gamemode == "trajet retour":
            if player.position <= station.num_case:
                station.enable = False
            elif station.num_case < relais[count]:
                station.enable = False
            else:
                station.enable = True

        elif gamemode != "trajet retour":
            if player.position >= station.num_case:
                station.enable = False
            elif station.num_case > relais[count]:
                station.enable = False
            else:
                station.enable = True    

def tour_du_joueur(playerlist, board, gamemode):
    if gamemode == "trajet retour":
        p_turn = 0
        for player in playerlist:
            if p_turn == 0:
                p_turn = player
            elif p_turn.position < player.position:
                p_turn = player
            elif p_turn.position == player.position:
                for case in board:
                    if p_turn.position == 1:
                        pass
                    elif case.num_case == p_turn.position:
                        p_turn = case.chara[-1]
    else:
        p_turn = 0
        for player in playerlist:
            if p_turn == 0:
                p_turn = player
            elif p_turn.position > player.position:
                p_turn = player
            elif p_turn.position == player.position:
                for case in board:
                    if p_turn.position == 1:
                        pass
                    elif case.num_case == p_turn.position:
                        p_turn = case.chara[-1]
    return p_turn

def change_pose (player, board):
    for case in board:
        if player in case.chara:
            case.chara.remove(player)

def pos_jeton (player, case):
    a = 0
    if case.sens == '+':
        if case.nom == "relais":
            for pla in case.chara:
                if pla == player:
                    break
                else:
                    a += 1 
            player.coord_x, player.coord_y = case.pos_x + 30,case.pos_y + 5 + a * 64 + 90
        else:
            for pla in case.chara:
                if pla == player:
                    break
                else:
                    a += 1 
            player.coord_x, player.coord_y = case.pos_x + 30,case.pos_y + 5 + (case.place - a) * 100
    elif case.sens == '-':
        if case.nom == "relais":
            for pla in case.chara:
                if pla == player:
                    break
                else:
                    a += 1 
            player.coord_x, player.coord_y = case.pos_x + 30,case.pos_y - a * 64 - 90
        else:
            for pla in case.chara:
                if pla == player:
                    break
                else:
                    a += 1 
            player.coord_x, player.coord_y = case.pos_x + 30,case.pos_y - (case.place - a) * 93

def station_cap (player_list,relais,count, gamemode):
    if gamemode == "trajet retour":
        b = 0
        for pla in player_list:
            if pla.position == relais[count]:
                b += 1
        if b == len(player_list):
            a = 0
            for case in relais:
                if player_list[0].position == case:
                    b = a - 1
                a += 1
        else:
            b = count
        return b


    else:
        b = 0
        for pla in player_list:
            if pla.position == relais[count]:
                b += 1
        if b == len(player_list):
            a = 0
            for case in relais:
                if player_list[0].position == case:
                    b = a+1
                a += 1
        else:
            b = count
        return b

def set_all_disable(board):
    for case in board:
        case.enable = False

def nb_jour_in_relais(player,relais,a):
    b = 0
    for joueur in player:
        if joueur.position == relais[a]:
            b += 1
    return b

def ability_to_buy (player, type, list_prix):
    min = 10
    if player.character == "Sasayako":
            if list_prix != []:
                for cout in list_prix:
                    if min > cout:
                        min = cout

    for sprite in type:
        if min > sprite.value:
            if sprite.value > player.yen + sprite.value:
                sprite.enable = False
            else:
                sprite.enable = True
        else:
            if sprite.value > player.yen + min:
                sprite.enable = False
            else:
                sprite.enable = True

def legal_meal (player, type):
    for meal in type:
        if player.character == "Kinko":
            if player.yen > 1:
                meal.enable = True
        elif meal.value > player.yen:
            meal.enable = False
        elif meal.nom in player.repas:
            meal.enable = False
        else:
            meal.enable = True

def acc_pano(player_list,acc_mer,acc_montagne,acc_riziere):
    if acc_mer == None:
        for player in player_list:
            if player.panorama_mer == 5:
                acc_mer = player
    if acc_montagne == None:
        for player in player_list:
            if player.panorama_montagne == 4:
                acc_montagne = player
    if acc_riziere == None:
        for player in player_list:
            if player.panorama_riziere == 3:
                acc_riziere = player
    return acc_mer,acc_montagne,acc_riziere

def fin_de_partie(list_player, nb_joueur, gamemode):
    if gamemode == "trajet retour":
        a = 0
        for player in list_player:
            if player.position == 1:
                a += 1
        if a == nb_joueur:
            return True
        else:
            return False
    else:
        a = 0
    for player in list_player:
        if player.position == 55:
            a += 1
    if a == nb_joueur:
        return True
    else:
        return False
    
def achievement_get(list_of_player,acc_mer,acc_montagne,acc_riziere):
    if acc_mer != None:
        for player in list_of_player:
            if player == acc_mer:
                if player.character == "mitsukuni":
                    player.point += 4
                else:
                    player.point += 3

    if acc_montagne != None:
        for player in list_of_player:
            if player == acc_montagne:
                if player.character == "mitsukuni":
                    player.point += 4
                else:
                    player.point += 3

    if acc_riziere != None:
        for player in list_of_player:
            if player == acc_riziere:
                if player.character == "mitsukuni":
                    player.point += 4
                else:
                    player.point += 3

    collec = []
    min = 0
    for player in list_of_player:
        if len(player.inventaire) > min:
            collec = []
            collec.append(player)
        elif len(player.inventaire) == min :
            collec.append(player)
    for player in collec:
        if player.character == "mitsukuni":
            player.point += 4
        else:
            player.point += 3

    source_chaude = []
    min = 0
    for player in list_of_player:
        if player.source > min:
            source_chaude = []
            source_chaude.append(player)
        elif player.source == min :
            source_chaude.append(player)
    for player in source_chaude:
        if player.character == "mitsukuni":
            player.point += 4
        else:
            player.point += 3

    rencontre_fait = []
    min = 0
    for player in list_of_player:
        if player.rencontre > min:
            rencontre_fait = []
            rencontre_fait.append(player)
        elif player.rencontre == min :
            rencontre_fait.append(player)
    for player in rencontre_fait:
        if player.character == "mitsukuni":
            player.point += 4
        else:
            player.point += 3

    gourmet = {}
    for player in list_of_player:
        bought = 0
        for eat in player.repas:
            with open('Repas.csv', newline= '') as repasread:
                spamreader = csv.reader(repasread, delimiter=',')
                for raw in spamreader:
                    if raw[0] == eat:
                        bought += int(raw[1])
        gourmet[player] = bought
        gourmetpoint = []
        min = 0
    for player in list_of_player:
        if gourmet[player] > min:
            gourmetpoint = []
            min = gourmet[player]
            gourmetpoint.append(player)
        elif gourmet[player] == min:
            gourmetpoint.append(player)
    for player in gourmetpoint:
        if player.character == "mitsukuni":
            player.point += 4
        else:
            player.point += 3

def collection(list_player): #bug
    for player in list_player:
        while player.inventaire != []:
            collect = []
            for item in player.inventaire:
                with open('List_souvenirs.csv', newline= '') as svread:
                    spamreader = csv.reader(svread, delimiter=',')
                    for raw in spamreader:
                        if raw[0] == "ï»¿":
                                pass
                        elif raw[1] == item:
                            if raw[0] not in collect:
                                collect.append(raw[0])
                                player.inventaire.remove(raw[1])
            if len(collect) == 4:
                player.point += 16
            elif len(collect) == 3:
                player.point += 9
            elif len(collect) == 2:
                player.point += 4
            elif len(collect) == 1:
                player.point += 1

def scoreboard(playerlist,font,screen):
    a=0
    for player in playerlist:
        query = str(a+1) + "ier :     " + player.pseudo
        img = font.render(query,True,(0,255,125))
        img2 = font.render(str(player.point),True,(0,255,125))
        img3 = font.render(player.colour.nom,True,(0,255,125))
        screen.blit(img,(600,300+100*a))
        screen.blit(img2,(900,300+100*a))
        screen.blit(img3,(1200,300+100*a))
        a += 1

def ordre_final(playerlist):
    liste = []
    a=0
    for player in playerlist:
        if liste == []:
            liste.append(player)
        a=0
        for play in liste:
            if player.point > play.point:
                liste.insert(a,player)
                break
            a += 1
    return liste