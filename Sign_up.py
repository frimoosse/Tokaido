import mysql.connector as mysql

pseudo = input('pseudo : ')
mdp = input('mdp : ')

conn = mysql.connect(host = "127.0.0.1",
                     user = "root", password="root",
                     database="tokaido")

cursor = conn.cursor()

user = (pseudo,mdp)
cursor.execute("INSERT INTO joueur" "(j_pseudo,j_mdp)" "VALUES (%s,%s)", user)

conn.commit()
cursor.close()
conn.close()