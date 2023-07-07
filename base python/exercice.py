## question 1##
print("\n\n###########b afficher type ############")
a=3
print(type(a))
print(type(a==3))

######conditions #####
### afficher min ###
print("\n\n###########b afficher min ############")
a = b= ""

while not(a.isdigit() and b.isdigit()):
    a = input("entrez un premier nombre : ")
    b = input("entrez un deuxième nombre : ")
if a<b:
    print(f"{a} est inferieur à {b}")
elif b<a:
    print(f"{b} est inferieur à {a}")
elif b==a:
    print(f"{a} est égale à {b}")

### afficher min ###
print("\n\n###########b afficher longueur ############")
chaine1 = input("entrez une chaine: ")
chaine2 = input("entrez une autre chaine : ")

if len(chaine1)<len(chaine2):
    print(f"le mot {chaine2} est plus longue que le mot  {chaine1}")
elif len(chaine2)<len(chaine1):
    print(f"le mot {chaine1} est plus longue que le mot {chaine2}")
elif len(chaine1)==len(chaine2):
    print(f"le mot {chaine1} est égale au mot  {chaine2}")

#### boucle for ###
print("\n\n########### boucle for ############")
for i in range (1,50):
    print("Je dois ranger mon bureau")

##### nombre #####
print("\n\n########### nombre ############")

nombre = int(input("entrez un nombre :"))
if nombre % 2 == 0:
    print("Ce nombre est pair. ")
elif nombre % 2 != 0 and nombre % 3 !=0:
    print("Ce nombre n’est ni pair ni multiple de 3.")
elif nombre % 2 != 0 and nombre % 3 ==0:
    print("Ce nombre est impair, mais est multiple de 3.")

