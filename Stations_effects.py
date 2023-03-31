#tokaido stations and effect of them

import Card_effect_rencontre as cer
import fonction as f
import random as r
import csv

def station_effect (station,player,relais,nb_joueur):

    if station == "echoppe" :
        print("pas coder")
        player.point += 1

    elif station == "temple":
        offrande = int(input("nombre de piece a offrir"))
        while offrande > player.yen:
            offrande = int(input("nombre de piece a offrir"))
        player.yen -= offrande
        player.offrande += offrande

    elif station == "rencontre":
        p=[]
        pioche = f.pioche(1,station)[0]
        print(pioche)
        cer.effet(pioche,player)

    elif station == "riziere":
        cer.effet("Annaibito Rizière",player)

    elif station == "source":
        pt = r.randint(2,3)
        player.point += pt

    elif station == "montagne":
        cer.effet("Annaibito Montagne",player)

    elif station == "ferme":
        player.yen += 3

    elif station == "mer":
        cer.effet("Annaibito Mer",player)

    elif station == "relais":
        if relais == 0:
            pioche = f.pioche(nb_joueur+1,"repas")
        print(pioche)
        choix = int(input("repas choisi"))

        if choix == -1:
            return

        else:
            choix = pioche[choix]

        with open('repas.csv') as repas:                      
            csv_reader = csv.reader(repas, delimiter = ',')
            nom_repas = choix
            for row in csv_reader:
                if str(nom_repas) == row[0]:
                    prix = row[1]
            
        if int(prix) > player.yen:
            choix = int(input("repas choisi"))

        else:
            player.point += 6
            player.yen -= int(prix)
            


    else:
        print("Fonctionne pas")