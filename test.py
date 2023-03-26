import mysql.connector as mysql
import random

conn = mysql.connect(host = "127.0.0.1",
                     user = "root", password="root",
                     database="tokaido")

cursor = conn.cursor()

a = [random.randint(1,24)]

cursor.execute("SELECT * FROM echoppe" "WHERE id_souvenir = %s " , a)

for items in cursor:
    print(items)

cursor.close()
conn.close()