

# palyndrome
print("palyndrome")
def palyndrome(mot):
    c=""
    mot_reverse ="".join(reversed(mot))
    if mot == mot_reverse:
        c=mot
         #print("Ce mot est un palyndrome")
    else:
        mot ="false"
        #print("Ce mot n'est pas un palyndrome")
    return c
### dico ###
def lireDico():
    mot = ""
    file = open('dico.txt', "r")
    lines = file.readlines()
    file.close()
    liste = []
    # Itérer sur les lignes
    for line in lines:
        mot = palyndrome(line.strip())
        if mot != "":
            liste.append(mot)
    print(liste)



### read file ##
print("lire une fichier")
my_file = open("loremipsum.txt", "r" )
read_c = my_file.read()
print(read_c)


### read file ##
print("lire une fichier")
my_file = open("fichier.txt", "w" )

liste1=["chaud", "froid","tempéré","glacial","brûlant"]
liste = ["hot", "cold", "moderate","icy", "ardent" ]
for i in liste1:
    my_file.write(i+' : \n')

my_file.close()
my_file = open("fichier.txt", "a" )
for i in liste1:
    my_file.write(i+' : \n')
