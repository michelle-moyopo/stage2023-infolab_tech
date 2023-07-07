import random
##### liste #####
print("\n\n########### liste1 ############")
liste = []
for i in range(1,6):
    element=input(f"Entrez un élémént {i} dans la liste : ")
    liste.append(element)
print("\n\n liste d'élément")
for elem in liste:
    print(f"{elem} possède {len(elem)} caractères")

    ##### liste #####
print("\n\n########### jeu de cartes ############")

listeCartes1=["a","x","2","5","7","k","8","4","9","6","j"]
listeCartes2=["a","3","2","5","7" ,"10","4","9","6","g","f"]
carteTire1=[]
carteTire2=[]
cartes=[]
print(listeCartes1)
print(listeCartes2)
for i in range(0,10):
    n = random.randint(1,10)
    tire1 =random.choices(listeCartes1)
    tire2 =random.choices(listeCartes2)
    carteTire1.append(tire1)
    carteTire2.append(tire2)
    
print(carteTire1)
print(carteTire2)

for i in range(0, len(carteTire1)):
    for j in range(0,len(carteTire2)):
        if carteTire1[i] == carteTire2[j]:
            cartes.append(carteTire2[j])

print(cartes)


