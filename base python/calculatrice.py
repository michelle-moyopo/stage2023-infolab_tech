

def add (x, y):
    return int(x) + int(y)

def sous(x, y):
    return x-y

def div(x,y):
    return x/y

def mult(x,y):
    return x*y
rest = "false"
premiernbre= input("Entrez un premier nombre: ")
secondnbre = input("Entrez un deuxième nombre: ")
while rest == "false": 
    if (not premiernbre.isdigit()) or (not secondnbre.isdigit()):
        print('Veuillez entrer deux nombre valides')
        premiernbre= input("Entrez un premier nombre: ")
        secondnbre = input("Entrez un deuxième nombre: ")
    else:
        result= add(premiernbre,secondnbre)
        rest = "true"     
        print("Le resultat de l'addition de "+ str(premiernbre) + " avec " + str(secondnbre) +" est egale à "+ str(result))
        
    # ou
    a=b=""
    while not (a.isdigit() and b.isdigit()):
        a = input("Entrez un premier nombre: ")
        b = input("Entrez un deuxième nombre: ")
        if not (a.isdigit() and b.isdigit()):
            print("veuillez entrer deux nombres valides")
    print("Le resultat de l'addition de {a} avec {b} est egale à  {int(a) +int(b)}")
        

