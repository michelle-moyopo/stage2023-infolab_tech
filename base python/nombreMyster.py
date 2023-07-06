import random

print("** le jeu du nombre mystère***")
MIN = 1
MAX = 5
NOMBREMYSTER = random.randint(MIN,MAX)
NOMBREVIE = 5
vie = 0
nombre = ""
while vie < NOMBREVIE :
    print(f"il reste {NOMBREVIE-vie} essais")
    nombre = input("Devine le nombre : ")
    while not nombre.isdigit():
        nombre = input("Devine le nombre : ")
        if not nombre.isdigit():
            print("Veuillez entrer un nombre valide")
            nombre = input("Devine le nombre : ")
    if int(nombre) < NOMBREMYSTER:
        print("le nombre myster est plus grand ")
        vie = vie +1

    elif int(nombre) > NOMBREMYSTER:
        print("le nombre myster est plus petit ")
        vie = vie +1
    elif  int(nombre) == NOMBREMYSTER:
        print("Bravo!!!!! vous avez trouvé le nombre Mystère ")
        choix = input("voulez vous continuer ? (oui/non) : ")
        while choix != "oui" and  choix != "non" :
            choix = input("voulez vous continuer ? (oui/non) : ")
        if choix == "non":
            print("A bientôt!")
            break
        elif vie == NOMBREVIE:
            vie == 0
        vie = vie +1
   
if vie == NOMBREVIE:
    print(f"Dommage!! le nombre mystere était  {NOMBREMYSTER} \n Fin du jeu")
