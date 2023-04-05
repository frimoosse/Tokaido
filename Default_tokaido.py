#Tokaido default game

# imports

import pygame as pyg
import random as r
import Card_effect_rencontre as ce 
import Stations_effects as se
import pickle as p
import csv

# répartition des cases relais sur le plateau

relais = [1,15,28,42,55]
Character_random = [1,2,3,4,5,6,7,8,9,10]

# jeux à update sans interface singleplayer

partie = True
place = 1                   ## il faudra allez chercher la position sur la bdd

a = 1

yen = 0
point = 0
panorama_riziere = 0
panorama_mer = 0
panorama_montagne = 0


# Choix du personnage surement changer dans les prochaines versions

choice = None

r.shuffle(Character_random) ## il faudrait trouver un moyen d'étendre ce shuffle a tout le monde ou un autre moyen de distribuer les cartes

while choice !=1 and choice !=2:
    choice = int(input(' choix 1 : '+ str(Character_random[1])+' choix 2 : '+ str(Character_random[2])))
choice = Character_random[choice]

with open('Character_list.csv') as chara:
    csv_reader = csv.reader(chara, delimiter = ',')
    line_count = choice
    for row in csv_reader:
        if str(line_count) == str(row[0]):
            name = row[1]
            piece = row[2]

# Debut de la partie

while partie:
    achat = 0

    move = int(input("allez a la case X"))
    while move <= place or move > relais[a]:
        print('vous ne pouvez pas')
        move = int(input("allez a la case X"))

    with open('plateau.csv') as board:                      #  permet de lire le csv contenant les cases du plateau
        csv_reader = csv.reader(board, delimiter = ',')
        line_count = move
        for row in csv_reader:
            if str(line_count) == row[0]:
                case = row[1]
        


        print(case)
        print(point)
        print(yen)
        print(panorama_mer)
        print(panorama_montagne)
        print(panorama_riziere)
        print(place)


#    ch.chara_effect(choice)                                 # effet du personnage choisis

    ## mettre ici l'effet de la case

    if move == relais[a]:                                   # nouvelle limite
        a += 1    

    place = move              ## il faudra modifier la position sur la BDD en plus
