import Classe
import fonction
import csv

player = Classe.joueur("fr","p")


pioche = fonction.pioche(2,"repas")
print(pioche)
choix = int(input("repas choisi"))

if choix == -1:
    print("ici")

else:
    choix = pioche[choix]

with open('repas.csv') as repas:                      
    csv_reader = csv.reader(repas, delimiter = ',')
    nom_repas = choix
    for row in csv_reader:
        if str(nom_repas) == row[0]:
            prix = row[1]
            
print(prix)
print(player.yen)
