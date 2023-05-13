import Classe as c
import csv

purple = c.Couleurs("purple",(105, 37, 187))
player = c.joueur("frimousse" ,purple,0,0)
player.inventaire = ["Koma","Ocha","Netsuke","Yukata"]

while player.inventaire != []:
            collect = []
            for item in player.inventaire:
                print(item)
                with open('List_souvenirs.csv', newline= '') as svread:
                    spamreader = csv.reader(svread, delimiter=',')
                    for raw in spamreader:
                        if raw[0] == "ï»¿":
                                pass
                        elif raw[1] == item:
                            if raw[0] not in collect:
                                collect.append(raw[0])
                                player.inventaire.remove(raw[1])
                                print(player.inventaire)
print(player.point)