#Tokaido initiatique game

# imports

import pygame as pyg
import random as r
import Card_effect_rencontre as ce
import Character as ch
import Stations_effects as se
import pickle as p
import csv

# répartition des cases relais sur le plateau

relais = [1,15,28,42,55]

# jeux initiatique

partie = True
place = 1                   ## il faudra allez chercher la position sur la bdd

a = 1

piece = 0
point = 0
panorama_riziere = 0
panorama_mer = 0
panorama_montagne = 0

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
        print(piece)
        print(panorama_mer)
        print(panorama_montagne)
        print(panorama_riziere)
        print(place)


#    ch.chara_effect(choice)                                 # effet du personnage choisis

    ## mettre ici l'effet de la case

    if move == relais[a]:                                   # nouvelle limite
        a += 1    

    place = move              ## il faudra modifier la position sur la BDD en plus