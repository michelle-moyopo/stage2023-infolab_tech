class Personne:

    def __init__(self, nom:str):
        self.nom = nom
    def SePresenter(self):
        print("bonjour, je m'appelle " + self.nom)
nbrePer = 3
noms = []
for i in range(0,nbrePer):
    noms.append(input("nom de la personne"+str(i+1)+" :"))
l= []
for nom in noms:
    l.append(Personne(nom))

for p in l:
 p.SePresenter()