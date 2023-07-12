class Personne:
    etre_vivant = "Humain(Mammifère Homo sapiens)"
    def __init__(self, nom ="", age = 0):
        self.nom = nom
        self.age = age
        if nom == "": 
            self.DemandeNom()
        
    def SePresenter(self):
        if self.age == 0:
            print("bonjour, je m'appelle " + self.nom )
        else:
            print("bonjour, je m'appelle " + self.nom + ",j'ai "+ str(self.age) +" ans")
            if self.EstMajeur():
                print("je suis majeur")
            else:
                print("je suis mineur")

    def EstMajeur(self):
        return self.age>=18
        
    def DemandeNom(self):
        self.nom= input("entrez nom : ") 

    def afficherInfoEtreVivant(self):
         print("Info être vivant:" + Personne.etre_vivant)


#personne1 =Personne("toto",30)
#personne2 =Personne("mii",15)
#personne1.SePresenter()
#personne2.SePresenter()


liste_personne = (Personne("toto",30),Personne("mii",15),Personne("paul",15))
for personne in liste_personne:
    personne.SePresenter()
    personne.afficherInfoEtreVivant()