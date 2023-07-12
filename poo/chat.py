class EtreVivant:
    ESPACE_ETRE_VIVANT= "(être vivant non idntifié)"
    def AfficherInfosEtreVivant(self):
        print("info être vivant : "+self.ESPACE_ETRE_VIVANT)
   

#héritage et surcharge
class Chat(EtreVivant):
    ESPACE_ETRE_VIVANT= "Chat (Mammifère Felin)"
    def AfficherInfosEtreVivant(self):
        print("info être vivant : "+self.ESPACE_ETRE_VIVANT)
chat =Chat()
chat.AfficherInfosEtreVivant()