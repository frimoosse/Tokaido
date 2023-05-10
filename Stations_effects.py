#tokaido stations and effect of them

import Card_effect_rencontre as cer
import fonction as f
import random as r
import csv


def station_effect (station,player,relais,nb_joueur,item,repas):

    if station == "echoppe" :
        achat = []
        pioche_memory =[]
        pioche,memoire = f.pioche(3,station,item.allcard)
        for it in pioche:
            pioche_memory.append(it)
        item.allcard.append(memoire)
        print(pioche)
        choix = int(input("quel item? " ))
        if choix != -1:
            achat.append(pioche[choix])
            del(pioche[choix])
            print(pioche)
            choix = int(input("autre item ? "))
            if choix != -1:
                achat.append(pioche[choix])
                del(pioche[choix])
                print(pioche)
                choix = int(input("un dernire item ? "))
                if choix != -1:
                    achat.append(pioche[choix])
        prix = 0
        with open('List_souvenirs.csv') as souvenir:                      
            csv_reader = csv.reader(souvenir, delimiter = ',')
            for row in csv_reader:
                for count in achat:
                    nom_souvenir = str(count)
                    if str(nom_souvenir) == row[1]:
                        prix += int(row[2])
        if prix > player.yen:
            achat = -2
            pioche = []
            for it in pioche_memory:
                pioche.append(it)
        while achat == -2:
            achat = []
            print("voux n'avez pas assez d'argent")
            print(pioche)
            choix = int(input("quel item? " ))
            if choix != -1:
                achat.append(pioche[choix])
                del(pioche[choix])
                print(pioche)
                choix = int(input("autre item ? "))
                if choix != -1:
                    achat.append(pioche[choix])
                    del(pioche[choix])
                    print(pioche)
                    choix = int(input("un dernire item ? "))
                    if choix != -1:
                        achat.append(pioche[choix])
            
            prix = 0
            with open('List_souvenirs.csv') as souvenir:                      
                csv_reader = csv.reader(souvenir, delimiter = ',')
                for row in csv_reader:
                    for count in achat:
                        nom_souvenir = str(count)
                        if str(nom_souvenir) == row[1]:
                            prix += int(row[2])
            if prix > player.yen:
                achat = -2
                pioche = []
                for it in pioche_memory:
                    pioche.append(it)

        
        player.yen -= prix
        player.inventaire.append(achat)



    elif station == "temple":
        offrande = int(input("nombre de piece a offrir"))
        player.yen -= offrande
        player.offrande += offrande
        player.point += offrande

    elif station == "rencontre":
        if player.character == "Umegae":
            player.yen += 1
            player.point += 1
        if player.character == "Yoshiyasu":
            p=[]
            pioche = f.pioche(2,station,p)[0]
            print(pioche)
            choix =int(input("quel carte ?"))
            cer.effet(pioche[choix],player)
        else : 
            p=[]
            pioche = f.pioche(1,station,p)[0]
            print(pioche)
            cer.effet(pioche[0],player)

    elif station == "riziere":
        rencontre = 'Annaibito Rizière'
        cer.effet(rencontre,player)

    elif station == "source":
        pt = r.randint(2,3)
        player.point += pt
        if player.character == "Mitsukuni":
            player.point += 1

    elif station == "montagne":
        rencontre = 'Annaibito Montagne'
        cer.effet(rencontre ,player)

    elif station == "ferme":
        player.yen += 3

    elif station == "mer":
        rencontre = 'Annaibito Mer'
        cer.effet(rencontre,player)

    elif station == "relais":
        if player.character == "Chuubei":
            p=[]
            pioche = f.pioche(1,"rencontre",p)[0]
            print(pioche)
            cer.effet(pioche[0],player)
        if player.character == "Hiroshige":
            ask = int(input("which panorama choice ? "))
            if ask == 1:
                rencontre = 'Annaibito Mer'
                cer.effet(rencontre,player)
            elif ask == 2:
                rencontre = 'Annaibito Montagne'
                cer.effet( rencontre ,player)
            elif ask == 3:
                rencontre = 'Annaibito Rizière'
                cer.effet(rencontre,player) 

        elif relais == 0:
            repas.actuel,poi = (f.pioche(nb_joueur+1,"repas",repas.precedent))
            for a in range (len(repas.actuel)):
                repas.precedent.append(poi[a])

        
        
        choix = 0
        while choix != -2:
            print(repas.actuel)
            
            choix = int(input("repas choisi"))

            if choix == -1:
                return

            with open('repas.csv') as repas2:                      
                csv_reader = csv.reader(repas2, delimiter = ',')
                nom_repas = repas.actuel[choix]
                for row in csv_reader:
                    if str(nom_repas) == row[0]:
                        prix = row[1]

            if player.character == "Kinko":
                if (int(prix)-1) <= player.yen:
                    del(repas.actuel[choix])
                    player.point += 6
                    player.yen -= (int(prix)-1)
                    choix = -2
                    
            else:
                if int(prix) < player.yen:
                    del(repas.actuel[choix])
                    player.point += 6
                    player.yen -= int(prix)
                    choix = -2

            


    else:
        print("Fonctionne pas")


        # sasayakko   Zen-emon   satsuki