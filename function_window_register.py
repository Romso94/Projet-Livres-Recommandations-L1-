# Projet : Systeme de recommandation de livres  ( projet L1)
# Le fichier function_window_register est appelé lors de l'enregistrement des informations d'un utilisateur


import hashlib
from tkinter.constants import E

def ListeLivres():
    # Cette fonction sert à recuperer tous les livres contenus dans le fichier books.txt
    # Entrée : books.txt 
    # Sortie : Liste_Livres:Liste de tous les livres présents dans books.txt
    with open ('books.txt','r',encoding='utf-8') as livre:
        livres =  livre.readlines()   
        Liste_Livre=livres
        Liste_Livres = []
        for i in Liste_Livre:        #Chaques elements de Liste_Livre sont ajoutés dans une nouvelle liste
            var = i.split('\n')      
            Liste_Livres.append(var[0])
        return(Liste_Livres)

def Enregistrer(pseudo,genre,age,style,livreslus,mdp):
    # Cette fonction sert à transformer les informations récupérées via les données de l'utilisateur en données a inscrire dans les fichiers readers.txt et booksread.txt
    # Entrée : pseudo:string:Le pseudo de l'utilisateur ; genre:string:Le genre de l'utilisateur ; age:string:L'age de l'utilisateur ; style:string: Le style de lecture de l'utilisateur ;
    #livreslus:tableau : Tableau contenant tous les livres lus par l'utilisateur ; mdp:string: le mot de passe de l'utilisateur ; readers.txt ; booksread.txt 

    # Sortie :  readers.txt: le fichier contient maintenant  : pseudo,genre,age,style,mdp ; booksread.txt : le fichier contient maintenant : pseudo,livreslus
   
    with open('readers.txt','a',encoding='utf-8') as f1,open('booksread.txt','a',encoding='utf-8') as f2 : #Ouverture en mode a pour ajouter les informations dans les fichiers
        Dico_Genre = {'Homme':1,'Femme':2,'Peu Importe':3}
        genre_=Dico_Genre[genre]                                    #Transformation du string genre donnée en int

        Dico_Age = {'<=18 ans':1,'Entre 18 et 25 ans':2,'> 25 ':3}
        age_ = Dico_Age[age]                                        #Transformation du string age donnée en int
        
        style = style[0]                                            
        mdp_hash = Hash_MDP(mdp)                                   #Hashage du mot de passe par la fonction Hash_MDP pour enregistrer l'empreinte du mot de passe de l'utilisateur
        L=[]
        f2.write(f'{pseudo}')
        Listelivre = []
        for i in livreslus:
            var =i.split(' ')
            Listelivre.append(var)

       
        if len(Listelivre)>0:                                       #Inscription différentes selon : -Si l'utilisateur a lus plusieurs ou aucun livres.
            f2.write(',' )
            for i in range (len(Listelivre)-1):
                f2.write(f'{Listelivre[i][0]},')
            f2.write(f'{Listelivre[-1][0]}\n')
        else :
            f2.write('\n')
            
        
        f1.write(f"{pseudo},{str(genre_)},{str(age_)},{str(style)},{mdp_hash}\n")               #Inscription dans le fichier readers.txt des différentes informations
    
def Hash_MDP(mdp):  
    #Cette fonction calcule l'empreinte sha256 d'un string via la librairie Hashlib
    #Entrée : un string ici mdp
    #Sortie : l'empreinte sha256 
    MDP = mdp.encode('utf-8')
    mdp_h = hashlib.sha256()
    mdp_h.update(MDP)
    return (mdp_h.hexdigest())


        
        







