# fonction

# pioche

import mysql.connector as mysql
import random


def pioche (nb_carte_pioche, case_type):

    conn = mysql.connect(host = "127.0.0.1",
                     user = "root", password="root",
                     database="tokaido")

    cursor = conn.cursor()
    cursor_bis = conn.cursor()

    query_1 = "SELECT COUNT(*) FROM " + case_type

    cursor_bis.execute(query_1)

    for items in cursor_bis:
        lg = items[0]

    b=[]
    count= 0
    while count < nb_carte_pioche:

        pioche_rd = [random.randint(1,lg)]
        query_2 = "SELECT * FROM " + case_type + " WHERE id_" + case_type + " = %s "

        cursor.execute(query_2 , pioche_rd)
        for items in cursor:
            if items[0] not in b:
                b.append(items[0])
                count += 1
        
    cursor.close()
    conn.close()
    return(b)

