

mdp = input("Entrer un mot de passe(min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
mdp_nbre = "votre mot de passe ne contient que des nombres."
mdp_valide = "Inscription terminé"
if len(mdp)<8:
    print(mdp_trop_court)
    
elif mdp.isdigit():
        print(mdp_nbre)
else:
    print(mdp_valide)