#Tokaido meeting card and impact

from fonction import pioche

def effet(rencontre, player):
    if rencontre == 'Annaibito Rizière' :
        if player.panorama_riziere != 3:
            player.panorama_riziere += 1
            player.point += player.panorama_riziere
        else:
            None
    
    elif rencontre == 'Annaibito Mer':
        if player.panorama_mer != 5:
            player.panorama_mer += 1
            player.point += player.panorama_mer
        else:
            None
    
    elif rencontre == 'Annabito Montagne':
        if player.panorama_montagne != 4:
            player.panorama_montagne += 1
            player.point += player.panorama_montagne
        else:
            None

    elif rencontre == 'Shokunin':
        player.point += 1         ## a faire dans la BDD
        return(pioche(1,"rencontre"))

    elif rencontre == 'Miko':
        player.offrande += 1        ## a faire dans la BDD

    elif rencontre == 'Kuge':
        player.yen += 3

    elif rencontre == 'Samurai':
        player.point += 3         ## a faire dans la BDD

    else:
        print("J'ai oublier quelques chose")