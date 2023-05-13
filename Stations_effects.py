#tokaido stations and effect of them

import Card_effect_rencontre as cer
import fonction as f
import random as r
import csv
import pygame
import Classe as c
from pygame.locals import *



def station_effect (station,player,relais,nb_joueur,item,repas,screen,font,font2,display_stat,crosshair_group,plateau,plateau_rect,list_of_player,gamemode):

    pygame.init()
    clock = pygame.time.Clock()

    bouton1 = pygame.image.load("IMAGE/egale.png")
    bouton1 = pygame.transform.scale(bouton1, (50,30))
    bouton1_rect = pygame.rect.Rect((50,125),(50,30))

    if station == "echoppe" :
        list_de_prix = []

        nb_acheter = 0

        font = pygame.font.Font(None , 40)

        button = font.render("DONE", True, (0,255,255))
        
        prix = 0
        achat = []
        pioche,memoire = f.pioche(3,station,item.allcard)
        for id in memoire:
            item.allcard.append(id)
        choice = True
        type = []
        for a in range(3):
            query = "IMAGE/objet/" + pioche[a] +".jpeg"
            pos_x = 500 + 425*a
            pos_y = 249
            b=a
            with open('List_souvenirs.csv', newline= '') as svread:
                spamreader = csv.reader(svread, delimiter=',')
                value = 0
                for raw in spamreader:
                    if raw[0] == "ï»¿":
                         pass
                    else:
                        if raw[1] == pioche[a]:
                            value = int(raw[2])
            a = c.temporar_hitbox(query, pos_x, pos_y, (326,522), value, screen)
            a.nom = pioche[b]
            type.append(a)
        while choice:
                for event in pygame.event.get():
                    screen.blit(plateau,plateau_rect)
                    button_rect = pygame.rect.Rect(900,960,100,40)
                    for pla in list_of_player:                            # update les outils interactifs de l'interface
                        screen.blit(pla.img, (plateau_rect.left + pla.coord_x,pla.coord_y))
                    for sprite in type:
                        if sprite.hit() and sprite.enable == True:
                            prix = sprite.value
                            if player.character == "Zen-emon" and nb_acheter == 0:
                                prix = 1
                                nb_acheter += 1
                            achat.append(sprite.nom)
                            type.remove(sprite)
                            list_de_prix.append(prix)

                    if button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                        choice = False

                    elif pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                        display_stat = True

                    elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                        display_stat = False

                    for sprite in type:
                        sprite.draw()

                    f.ability_to_buy(player,type,list_de_prix)

                    screen.blit(button, (900,960))

                    f.stat_player(player, font2, screen, display_stat)
                    f.draw_player_stat(player, font, screen)
                    screen.blit(bouton1,(25,125))
                    
                    crosshair_group.draw(screen)                          # update du cursor sur l'interface
                    crosshair_group.update()
                    clock.tick(60)
                    pygame.display.update()

                    player.yen -= prix
                    prix = 0
        for sv in achat:
            player.inventaire.append(sv)
        if player.character == "Sasayakko" and len(list_de_prix) >= 2:
            min = 10
            if list_de_prix != []:
                for cout in list_de_prix:
                    if min > cout:
                        min = cout
            player.yen += min



    elif station == "temple":
        choice = True
        yen = []
        for a in range(3):
            query = "IMAGE/Yen " + str(a+1) + ".png"
            pos_x = 600 + 300*a
            pos_y = 440
            b = a+1
            a = "Yen " + str(a+1)
            a = c.temporar_hitbox(query,pos_x,pos_y,(200,200),b,screen)
            yen.append(a)
        while choice:
            for event in pygame.event.get():
                for sprite in yen:
                    if sprite.hit():
                        offrande = sprite.value
                        choice = False
                if pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                        display_stat = True

                elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                        display_stat = False

                decor = pygame.image.load("IMAGE/decor/temple.png")
                screen.blit(decor,(0,0))

                for sprite in yen:
                    sprite.draw()

                f.stat_player(player, font2, screen, display_stat)
                f.draw_player_stat(player, font, screen)
                screen.blit(bouton1,(25,125))
                
                crosshair_group.draw(screen)                          # update du cursor sur l'interface
                crosshair_group.update()
                clock.tick()
                pygame.display.update()

        if player.character == "Hirotada":
            player.yen -= offrande 
            player.offrande += offrande + 1
            player.point += offrande + 1 
        else:
            player.yen -= offrande
            player.offrande += offrande
            player.point += offrande

    elif station == "rencontre":
        player.rencontre += 1
        if player.character == "Umegae":
            player.yen += 1
            player.point += 1
        if player.character == "Yoshiyasu":
            p=[]
            pioche = f.pioche(2,station,p)[0]
            choice = True
            type = []
            for a in range(2):
                query = "IMAGE/rencontre/" + pioche[a] +".jpg"
                nom = pioche[a]
                pos_x = 650 + 425*a
                pos_y = 249
                value = a
                a = c.temporar_hitbox(query, pos_x, pos_y, (326,522), value, screen)
                type.append(a)
            while choice:
                    for event in pygame.event.get():
                        prix = 0
                        screen.blit(plateau,plateau_rect)
                        button_rect = pygame.rect.Rect(900,960,100,40)
                        for pla in list_of_player:                            # update les outils interactifs de l'interface
                            screen.blit(pla.img, (plateau_rect.left + pla.coord_x,pla.coord_y))
                        for sprite in type:
                            if sprite.hit() and sprite.enable == True:
                                choix = sprite.value
                                choice = False

                        if pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                            display_stat = True

                        elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                            display_stat = False

                        for sprite in type:
                            sprite.draw()

                        f.stat_player(player, font2, screen, display_stat)
                        f.draw_player_stat(player, font, screen)
                        screen.blit(bouton1,(25,125))

                        crosshair_group.draw(screen)                          # update du cursor sur l'interface
                        crosshair_group.update()
                        clock.tick(60)
                        pygame.display.update()

            cer.effet(pioche[choix],player)
        else : 
            p=[]
            pioche = f.pioche(1,station,p)[0]
            cer.effet(pioche[0],player)

            debut = True
            image = 'IMAGE/rencontre/'+str(pioche[0])+'.jpg'
            img = pygame.image.load(image)
            img = pygame.transform.scale(img, (326,522))
            while debut :    
                for event in pygame.event.get():
                    if pygame.mouse.get_pressed()[0]:
                        debut = False
                    elif pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                        display_stat = True

                    elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                        display_stat = False
                screen.blit(plateau,plateau_rect)
                for pla in list_of_player:                            # update les outils interactifs de l'interface
                    screen.blit(pla.img, (plateau_rect.left + pla.coord_x,pla.coord_y))

                f.stat_player(player, font2, screen, display_stat)
                f.draw_player_stat(player, font, screen)
                screen.blit(bouton1,(25,125))

                screen.blit(img, ((1920/2) - 163,(1080/2) - 266))

                crosshair_group.draw(screen)                          # update du cursor sur l'interface
                crosshair_group.update()
                clock.tick()
                pygame.display.update()
                

    elif station == "riziere":
        rencontre = 'Annaibito Rizière'
        cer.effet(rencontre,player)
        debut = True
        image = 'IMAGE/panorama/riziere/riziere '+ str(player.panorama_riziere)+'.jpeg'
        img = pygame.image.load(image)
        img = pygame.transform.scale(img, (326,522))
        while debut :    
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                    debut = False
                elif pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                        display_stat = True

                elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                        display_stat = False
            screen.blit(plateau,plateau_rect)
            for pla in list_of_player:                            # update les outils interactifs de l'interface
                screen.blit(pla.img, (plateau_rect.left + pla.coord_x,pla.coord_y))

            f.stat_player(player, font2, screen, display_stat)
            f.draw_player_stat(player, font, screen)
            screen.blit(bouton1,(25,125))

            screen.blit(img, ((1920/2) - 163,(1080/2) - 266))

            crosshair_group.draw(screen)                          # update du cursor sur l'interface
            crosshair_group.update()

            clock.tick()
            pygame.display.update()
                

    elif station == "source":
        player.source += 1
        pt = r.randint(2,3)
        player.point += pt
        if player.character == "Mitsukuni":
            player.point += 1
        debut = True
        image = 'IMAGE/source/source '+ str(pt)+'.jpeg'
        img = pygame.image.load(image)
        img = pygame.transform.scale(img, (326,522))
        while debut :    
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                    debut = False
                elif pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                        display_stat = True

                elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                        display_stat = False
            screen.blit(plateau,plateau_rect)
            for pla in list_of_player:                            # update les outils interactifs de l'interface
                screen.blit(pla.img, (plateau_rect.left + pla.coord_x,pla.coord_y))
            f.stat_player(player, font2, screen, display_stat)
            f.draw_player_stat(player, font, screen)
            screen.blit(bouton1,(25,125))

            screen.blit(img, ((1920/2) - 163,(1080/2) - 266))

            crosshair_group.draw(screen)                          # update du cursor sur l'interface
            crosshair_group.update()

            clock.tick()
            pygame.display.update()

    elif station == "montagne":
        rencontre = 'Annaibito Montagne'
        cer.effet(rencontre ,player)
        debut = True
        image = 'IMAGE/panorama/montagne/montagne '+ str(player.panorama_montagne)+'.jpeg'
        img = pygame.image.load(image)
        img = pygame.transform.scale(img, (326,522))
        while debut :    
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                    debut = False
                elif pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                        display_stat = True

                elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                        display_stat = False
            screen.blit(plateau,plateau_rect)
            for pla in list_of_player:                            # update les outils interactifs de l'interface
                screen.blit(pla.img, (plateau_rect.left + pla.coord_x,pla.coord_y))

            f.stat_player(player, font2, screen, display_stat)
            f.draw_player_stat(player, font, screen)
            screen.blit(bouton1,(25,125))

            screen.blit(img, ((1920/2) - 163,(1080/2) - 266))

            crosshair_group.draw(screen)                          # update du cursor sur l'interface
            crosshair_group.update()

            clock.tick()
            pygame.display.update()

    elif station == "ferme":
        player.yen += 3
        img = pygame.image.load("IMAGE/Yen 3.png")
        img = pygame.transform.scale(img,(300,300))
        debut = True
        while debut :    
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                    debut = False
                elif pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                        display_stat = True

                elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                        display_stat = False
            screen.blit(plateau,plateau_rect)
            for pla in list_of_player:                            # update les outils interactifs de l'interface
                screen.blit(pla.img, (plateau_rect.left + pla.coord_x,pla.coord_y))
            f.stat_player(player, font2, screen, display_stat)
            f.draw_player_stat(player, font, screen)
            screen.blit(bouton1,(25,125))

            screen.blit(img, ((1920/2) - 150,(1080/2) - 150))

            crosshair_group.draw(screen)                          # update du cursor sur l'interface
            crosshair_group.update()

            clock.tick()
            pygame.display.update()


    elif station == "mer":
        rencontre = 'Annaibito Mer'
        cer.effet(rencontre,player)
        debut = True
        image = 'IMAGE/panorama/mer/mer '+ str(player.panorama_mer)+'.jpeg'
        img = pygame.image.load(image)
        img = pygame.transform.scale(img, (326,522))
        while debut :    
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                    debut = False
                elif pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                        display_stat = True

                elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                        display_stat = False
            screen.blit(plateau,plateau_rect)
            for pla in list_of_player:                            # update les outils interactifs de l'interface
                screen.blit(pla.img, (plateau_rect.left + pla.coord_x,pla.coord_y))
            f.stat_player(player, font2, screen, display_stat)
            f.draw_player_stat(player, font, screen)
            screen.blit(bouton1,(25,125))

            screen.blit(img, ((1920/2) - 163,(1080/2) - 266))

            crosshair_group.draw(screen)                          # update du cursor sur l'interface
            crosshair_group.update()

            clock.tick()
            pygame.display.update()

    elif station == "relais":

        button = font.render("skip", True, (0,255,255))

        if player.character == "Chuubei":
            player.rencontre += 1
            p=[]
            pioche = f.pioche(1,"rencontre",p)[0]
            cer.effet(pioche[0],player)
            debut = True
            image = 'IMAGE/rencontre/'+str(pioche[0])+'.jpg'
            img = pygame.image.load(image)
            img = pygame.transform.scale(img, (326,522))
            while debut :    
                for event in pygame.event.get():
                    if pygame.mouse.get_pressed()[0]:
                        debut = False
                    elif pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                        display_stat = True

                    elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                        display_stat = False
                screen.blit(plateau,plateau_rect)
                for pla in list_of_player:                            # update les outils interactifs de l'interface
                    screen.blit(pla.img, (plateau_rect.left + pla.coord_x,pla.coord_y))

                f.stat_player(player, font2, screen, display_stat)
                f.draw_player_stat(player, font, screen)
                screen.blit(bouton1,(25,125))

                screen.blit(img, ((1920/2) - 163,(1080/2) - 266))

                crosshair_group.draw(screen)                          # update du cursor sur l'interface
                crosshair_group.update()

                clock.tick()
                pygame.display.update()
                
        if player.character == "Hiroshige":
            choice = True
            pano = ["mer","montagne","riziere"]
            type = []
            for a in range(3):
                query = "IMAGE/panorama/" + pano[a] +"/dos.jpeg"
                pos_x = 600 + 425*a
                pos_y = 249
                b = a+1
                a = "choix " + str(a+1)
                a = c.temporar_hitbox(query,pos_x,pos_y,(326,522),b,screen)
                type.append(a)
            while choice:
                for event in pygame.event.get():
                    button_rect = pygame.rect.Rect(900,960,100,40)
                    for sprite in type:
                        if sprite.hit():
                            ask = sprite.value
                            choice = False
                    if pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                        display_stat = True

                    elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                        display_stat = False

                    elif button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                        choice = False

                    for sprite in type:
                        sprite.draw()

                    f.stat_player(player, font2, screen, display_stat)
                    f.draw_player_stat(player, font, screen)
                    screen.blit(bouton1,(25,125))
                    
                    crosshair_group.draw(screen)                          # update du cursor sur l'interface
                    crosshair_group.update()

                    clock.tick()
                    pygame.display.update()

            if ask == 1:
                rencontre = 'Annaibito Mer'
                cer.effet(rencontre,player)
            elif ask == 2:
                rencontre = 'Annaibito Montagne'
                cer.effet( rencontre ,player)
            elif ask == 3:
                rencontre = 'Annaibito Rizière'
                cer.effet(rencontre,player) 
        
        if relais == 0 and gamemode == "gastronomie":
            repas.actuel,poi = (f.pioche(nb_joueur,"repas",repas.precedent))
            for a in range (len(repas.actuel)):
                repas.precedent.append(poi[a])

        elif relais == 0:
            repas.actuel,poi = (f.pioche(nb_joueur+1,"repas",repas.precedent))
            for a in range (len(repas.actuel)):
                repas.precedent.append(poi[a])
        skip = True
        if player.character == "Satsuki":
            choice = True
            skip = False
            type=[]
            query = "IMAGE/repas/" + repas.actuel[0] + ".jpg"
            nom = repas.actuel[0]
            pos_x = 797
            pos_y = 440
            with open('Repas.csv', newline= '') as repasread:
                    spamreader = csv.reader(repasread, delimiter=',')
                    for raw in spamreader:
                        if raw[0] == repas.actuel[0]:
                            value = int(raw[1])
                    a = c.temporar_hitbox(query, pos_x, pos_y, (326,522), value, screen)
                    a.nom = nom
                    type.append(a)
            while choice:
                    
                    f.legal_meal(player,type)

                    for event in pygame.event.get():
                        prix = 0
                        screen.blit(plateau,plateau_rect)
                        button_rect = pygame.rect.Rect(900,960,100,40)
                        for pla in list_of_player:                            # update les outils interactifs de l'interface
                            screen.blit(pla.img, (plateau_rect.left + pla.coord_x,pla.coord_y))
                        for sprite in type:
                            if sprite.hit() and sprite.enable == True:
                                prix = sprite.value
                                type.remove(sprite)
                                choice = False
                                repas.actuel.remove(sprite.nom)
                                player.point += 6
                                player.repas.append(sprite.nom)
                                if player.character == "Kinko":
                                    player.yen -= 1
                                else : 
                                    player.yen -= prix

                        if pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                            display_stat = True

                        elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                            display_stat = False
                        
                        elif button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                            choice = False
                            skip = True

                        for sprite in type:
                            sprite.draw()


                        f.stat_player(player, font2, screen, display_stat)
                        f.draw_player_stat(player, font, screen)
                        screen.blit(bouton1,(25,125))
                        screen.blit(button, (900,960))
                        
                        crosshair_group.draw(screen)                          # update du cursor sur l'interface
                        crosshair_group.update()
                        clock.tick(60)
                        pygame.display.update()

        if skip == True:
            choice = True
            type = []
            for a in range (len(repas.actuel)):
                query = "IMAGE/repas/" + repas.actuel[a] +".jpg"
                nom = repas.actuel[a]
                pos_x = 50 + 425*a
                pos_y = 340
                with open('Repas.csv', newline= '') as repasread:
                    spamreader = csv.reader(repasread, delimiter=',')
                    for raw in spamreader:
                        if raw[0] == repas.actuel[a]:
                            value = int(raw[1])
                a = c.temporar_hitbox(query, pos_x, pos_y, (326,522), value, screen)
                a.nom = nom
                type.append(a)
            while choice:
                    
                    f.legal_meal(player,type)

                    for event in pygame.event.get():
                        prix = 0
                        screen.blit(plateau,plateau_rect)
                        button_rect = pygame.rect.Rect(900,960,100,40)
                        for pla in list_of_player:                            # update les outils interactifs de l'interface
                            screen.blit(pla.img, (plateau_rect.left + pla.coord_x,pla.coord_y))
                        for sprite in type:
                            if sprite.hit() and sprite.enable == True:
                                prix = sprite.value
                                type.remove(sprite)
                                choice = False
                                repas.actuel.remove(sprite.nom)
                                player.point += 6
                                player.repas.append(sprite.nom)
                                if player.character == "Kinko":
                                    player.yen -= 1
                                else : 
                                    player.yen -= prix

                        if pygame.mouse.get_pressed()[0] and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == False:  # afficher les statistiques   
                            display_stat = True

                        elif event.type == MOUSEBUTTONDOWN and bouton1_rect.collidepoint(pygame.mouse.get_pos()) and display_stat == True:   # cacher les statistiques
                            display_stat = False
                        
                        elif button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                            choice = False

                        for sprite in type:
                            sprite.draw()


                        f.stat_player(player, font2, screen, display_stat)
                        f.draw_player_stat(player, font, screen)
                        screen.blit(bouton1,(25,125))
                        screen.blit(button, (900,960))
                        
                        crosshair_group.draw(screen)                          # update du cursor sur l'interface
                        crosshair_group.update()
                        clock.tick(60)
                        pygame.display.update()

                        
            
                


        # sasayakko   Zen-emon   satsuki