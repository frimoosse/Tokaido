# Character
## fonctionne probablement pas

def chara_effect(choice, panorama_mer, panorama_riziere, panorama_montagne, point, effect, achat, case) :
    if choice == 'Hiroshige':
        if effect == 'relais' :
            panorama = 0 
            while panorama != 1 or panorama != 2 or panorama != 3:
                panorama = int(input('1 : riziere ; 2 : mer ; 3 : montagne '))
            if panorama == 1 :
                if panorama_riziere != 3:
                    panorama_riziere += 1
                else :
                    None
            elif panorama == 2:
                if panorama_mer != 5:
                    panorama_mer += 1
                else:
                    None
            elif panorama == 3:
                if panorama_montagne != 4:
                    panorama_montagne += 1
                else:
                    None

    elif choice == 'Kinko':
            ## prix du repas 1 piece moins chere
            ### pas encore coder les repas a chaque relais
            print('pas coder')

    elif choice == 'Sasayakko':
            if achat >= 2:
                print('pas coder')
                ## le moins gratuit
                ### achat pas encore coder
            else:
                None

    elif choice == 'Chuubei':
        ## pioche une carte rencontre, fonction pioche pas coder
        print('pas coder')

    elif choice == 'Yoshiyasu':
        ## pioche 2 carte rencontre et en choisi 1
        print('pas coder')

    elif choice == 'Satsuki':
        ## plat aléatoire gratuit, peut refuser
        print('pas coder')

    elif choice == 'Mitsukuni':
        ## accomplissement et source chaude pas coder
        print('pas coder')

    elif choice == 'Hirotada':
        ## si veut offrande +1
        print('pas coder')

    elif choice == 'Umegae':
        if case == 'rencontre':
            point += 1
        else : 
            None

    elif choice == 'Zen-emon':
        ## achat d'un souvenir pour 1 piece, 1 par echoppe 
        print('pas coder')