#Tokaido meeting card and impact

def effet(rencontre):
    if rencontre == 'Annaibito Rizière' :
        if panorama_riziere != 3:
            panorama_riziere += 1
        else:
            None
    
    elif rencontre == 'Annaibito Mer':
        if panorama_mer != 5:
            panorama_mer += 1
        else:
            None
    
    elif rencontre == 'Annabito Montagne':
        if panorama_montagne != 4:
            panorama_montagne += 1
        else:
            None

    elif rencontre == 'Shokunin':
        point += 1         ## a faire dans la BDD
        ## pioche une carte souvenir

    elif rencontre == 'Miko':
        temple += 1        ## a faire dans la BDD

    elif rencontre == 'Kuge':
        piece += 3

    elif rencontre == 'Samurai':
        point += 3         ## a faire dans la BDD

    else:
        print("J'ai oublier quelques chose")