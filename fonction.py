# fonction

# pioche

import mysql.connector as mysql
import random
import csv


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

def create_board():
    print("a faire")