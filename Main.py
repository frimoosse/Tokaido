#Tokaido game

# imports

import pygame as pyg
import random as r
import Card_effect as ce
import Stations_effects as se
import pickle as p
import csv

# répartition des cases relais sur le plateau

relais = [1,15,28,42,55]

# jeux à update sans interface singleplayer

partie = True
place = 1                   ## il faudra allez chercher la position sur la bdd
a=1
while partie:

    move = int(input("allez a la case X"))
    while move <= place or move > relais[a]:
        move = int(input("allez a la case X"))

    with open('plateau.csv') as board:                      #  permet de lire le csv contenant les cases du plateau

        csv_reader = csv.reader(board, delimiter = ',')
        line_count = move
        for row in csv_reader:

            if str(line_count) == row[0]:
                effect = row[1]
    
    if move == relais[a]:                                   # nouvelle limite
        a += 1    

    place = move              ## il faudra modifier la position sur la BDD en plus