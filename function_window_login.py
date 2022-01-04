# Projet : Systeme de recommandation de livres  ( projet L1)
# Le fichier function_window_login.py est appelé lorsque l'utilisateur ce connecte.
# Ce fichier sert à vérifier que l'utilisateur existe et qu'il a bien entré le pseudo associé au bon mot de passe.

from main import *

def Login(mdp,pseudo): 
    # Fonction pour se connecter
    # Entrée : mdp(le mot de passe fournit par l'utilisateur) et pseudo(le pseudo fournit par l'utilisateur)
    # Sortie : True,pseudo (Si la connexion est validé) ; False,' '(Si la connexion est refusé)
       
        mdp_h = mdp
        mdp_h += '\n'
        with open ('readers.txt','r') as f2:        #Recherche du pseudo associe au mot de passe dans le fichier readers.txt
            d = f2.readlines()
            L_Propre = []
            for i in d:
                var = i.split(',')
                L_Propre.append(var)
            for i in L_Propre:
                if i[0]==pseudo and i[-1]==mdp_h:
                    return(True,pseudo)
            return (False,' ')                          #Retourne faux si la connexion n'est pas validé : -pseudo n'existe pas ou -{pseudo;mdp} ne correspondent pas dans readers.txt
