import sys


def menu():
    print("Choisissez parmi les ( options suivantes:")
    print("1: Ajouter un élément a la liste")
    print("2: retirer un élément a la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")

liste = ["pomme", "banane","orange", "courgette"]

menu()
choix =""
while not (choix.isdigit()):
    choix = input("votre choix : ")

if choix =="1":
    element = input(" Entrez l'element à ajouter : ")
    if element in liste :
        print("cet élément existe déja")
    else:
        liste.append(element)
        print(liste)
elif choix == "2":
    element = input(" Entrez l'element à supprimer : ")
    if element in liste :
        liste.remove(element)
        print(liste)
    else:
        print("cet élément n'existe pas")

elif choix == "4":
    liste.clear()
    print(liste)
elif choix == "3":
    for i in enumerate(liste):
        print(i)

elif choix == "5":
    print("A bientot")
    sys.exit()
