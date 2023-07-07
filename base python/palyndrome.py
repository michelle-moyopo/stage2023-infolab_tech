def palyndrome(mot):
   # mot_reverse ="".join(reversed(mot))
    mot_reverse = ""
    c=""
    for i in range(1, len(mot)+1):
        mot_reverse= mot_reverse + mot[i-2]
    print(mot_reverse)  
    if mot == mot_reverse:
        c=mot
        #print("Ce mot est un palyndrome")
    else:
        mot= "false"
        #print("Ce mot n'est pas un palyndrome")
    return c

def lireDico():
    mot = ""
    file = open('dico.txt', "r")
    lines = file.readlines()
    file.close()
    liste = []
    # Itérer sur les lignes
    for line in lines:
        mot = palyndrome("ici")
        if mot != "":
            liste.append(mot)
    print(liste)
lireDico()