#modification des accès
# public: nom
#private : __nom
#proteged: _nom


class Personne:
    TYPE = "Humain"
    def __init__(self, nom, age):
        # attribut private
        self._nom = nom
        # attribut public
        self._age = age
    #methode d'instance
    def Sepresenter(self):
        print(f"je m'appele {self.formater_chaine(self._nom)}, j'ai  {self._age}, type: {Personne.TYPE}")
    
    #méthode statique
    @staticmethod
    def formater_chaine(a):
        return a[0].upper()+a[1:].lower()
    #méthode de classe
    @classmethod
    def methodeClass(cls):
        pass


class Etudiant(Personne):
    def Sepresenter(self):
        super().Sepresenter()
        print("je suis etudiant")


personne =Personne("jean", 45)
personne._nom ="toto"
print(personne.__dict__)
personne.Sepresenter()

etudiant1= Etudiant("mii", 21)
etudiant1.Sepresenter()