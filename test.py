import mysql.connector as mysql

# nécessite une personne dans la bdd

loop = True

while loop:
    count = 0
    id = input("identifiant : ")
    conn = mysql.connect(host = "127.0.0.1",
                         user = "root", password="root",
                         database="tokaido")

    cursor = conn.cursor()

    query = "SELECT J_pseudo FROM Joueur"
    cursor.execute(query)

    for pseudo in cursor:
        if pseudo[0] == id:
            print("pseudo déja utilisé")
            count += 1

    if count == 0:
        loop = False

mdp = input("mot de passe ")

user = (id , mdp)

query_bis = "INSERT INTO joueur" "(j_pseudo,j_mdp)" "VALUES (%s,%s)"
cursor.execute(query_bis , user)

conn.commit()
cursor.close()
conn.close()