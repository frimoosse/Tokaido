#Tokaido initiatique game

# imports

import Classe as cl
import pygame as pyg
import random as r
import Card_effect_rencontre as ce
import Stations_effects as se
import pickle as p
import csv
import fonction as f

# répartition des cases relais sur le plateau

relais = [1,15,28,42,55]     # position des relais
list_of_player =[]           # liste des joueur
repas = cl.Repas()           # classe pour avoir les repas actuels et précédents
item = cl.item()             # classe pour avoir les objets déja pioché

# jeux initiatique

partie = True                # pour rester dans la partie

a = 1

# Avant le début de la partie (a remettre plus tard dans main)

nb_joueur = int(input("nombre de joueur "))

for loop in range(nb_joueur):    # donner la possibilité de s'inscrire si pas de compte
    pseudo = input("pseudo ")    # remplacer par la fonction check dans la fonction log in pas encore coder
    colour = input("colour ")
    list_of_player.append(cl.joueur(pseudo,colour))

for player in list_of_player:
    player.yen = 7

# Debut de la partie

r.shuffle(list_of_player)
player_turn = list_of_player[0]
case = None

nb_in_relais = 0

while partie:

    print("Tour de " + player_turn.pseudo)
    #player_turn.Display_player()

    move = int(input("allez a la case X"))
    for player in list_of_player:
        if player.position == move and case != "relais":
            move = -1

    with open('plateau.csv') as board:                      #  permet de lire le csv contenant les cases du plateau
        csv_reader = csv.reader(board, delimiter = ',')
        line_count = move
        for row in csv_reader:
            if str(line_count) == row[0]:
                case = row[1]
    
    if case == "echoppe" and player_turn.yen == 0:
        move = -1

    if case == "temple" and player_turn.yen == 0:
        move = -1

    if f.check_panorama(player_turn,case):
        move = -1

    while move <= player_turn.position or move > relais[a]:
        print('vous ne pouvez pas')
        move = int(input("allez a la case X"))

        for player in list_of_player:
            if player.position == move and case != "relais":
                move = -1

        with open('plateau.csv') as board:                      
            csv_reader = csv.reader(board, delimiter = ',')
            line_count = move
            for row in csv_reader:
                if str(line_count) == row[0]:
                    case = row[1]

        if case == "echoppe" and player_turn.yen == 0:
            move = -1

        if case == "temple" and player_turn.yen == 0:
            move = -1

        if f.check_panorama(player_turn,case):
            move = -1

    se.station_effect(case,player_turn,nb_in_relais,nb_joueur,item,repas)

    player_turn.position = move              ## il faudra modifier la position sur la BDD en plus

    player_turn.Display_player()

    last = 100
    for player in list_of_player:
        if player.position < last:
            last = player.position
            player_turn = player

    nb_in_relais = 0

    for player in list_of_player:
        if player.position == relais[a]:
            nb_in_relais += 1
    
    if nb_in_relais == nb_joueur:
        a += 1
        nb_in_relais = 0

    if a == 5:
        partie = False

max = 0
for player in list_of_player:
    if player.point > max:
        max = player

print(f"gagnant est {max.pseudo}")