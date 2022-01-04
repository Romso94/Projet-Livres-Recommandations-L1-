# Projet : Systeme de recommandation de livres  ( projet L1)
#Ce fichier est le fichier principal qui permets de gerer l'affichage et d'appeler les fonctions nécéssaires



from tkinter import *
from tkinter import font
from typing import List, Sized, Tuple
from function_window_register import *
from tkinter import messagebox
from function_window_login import *
from Login_Info_File import *
import Login_Info_File
from Books_Modif import *
import Books_Modif
from Matrice_Notation_ import *
import Matrice_Notation_

# Fonction global :
def meme_pseudo(pseudo):
    #Cette fonction permets de verifier l'existence d'un pseudo dans readers.txt
    #entré : pseudo ; readers.txt
    #Sortie : booléen 
    with open ('readers.txt','r') as f2:
        d = f2.readlines()
        L_Propre = []
        for i in d:
            var = i.split(',')
            L_Propre.append(var[0])
        for i in L_Propre:
            if pseudo==i[0]:
                return True
        return False

#Fenetre de lancement
def Fenetre_Principal():
    #Cette fonction est la fenetre principal qui permets a un utilisateur de s'enregistrer ou de se connecter 

    #Fonction : 
    def Accueil_vers_enregistrement():                 #Ouvre la fenetre pour s'enregistrer
        Window.destroy()
        Fenetre_Enregistrement()

    def Accueil_vers_connexion():                    #Ouvre la fenetre pour se connecter
        Window.destroy()
        Fenetre_connexion()




    # Initialisation de la fenetre :
    Window = Tk()                   #Appel de la fonction Tk pour créer un fenetre 
    Window.title("App Projet")      #Titre de la fenetre 
    Window.geometry("300x300")      #Taille de la fenetre  400 pixel de haut / 300 de Large

    #Création des bouttons : 
    Boutton_Enregistrement = Button(Window,text="S'enregistrer",height='2',width='10',bg="snow3",command=Accueil_vers_enregistrement)
    Boutton_Enregistrement.pack(pady=50,anchor=CENTER)

    

    Boutton_Connexion = Button(Window,text="Se connecter",height='2',width='10',bg="snow3",command=Accueil_vers_connexion)
    Boutton_Connexion.pack(pady=30,anchor=CENTER)  #Placement du boutton grace a la methode .pack()
    

    Window.mainloop()   #Permets l'affichage de la fenetre

#Fenetre d'enregistrement
def Fenetre_Enregistrement():
     #Cette fonction gere la fenetre d'enregistrement et les appels des differentes fonctions associé aux differents bouttons

    
    
    #Fonction :
    def Enregistrement_vers_accueil():                 #Permet de retourner a l'accueil
        Fenetre_Enregistrement.destroy()
        Fenetre_Principal()
    def enregistrer(*args): #Permet de s'enregistrer
        pseudoo = Pseudo.get()
        genres = Boutton_Genres.get()
        age = Boutton_Age.get()
        Style_Lecture = Boutton_Style_Lecture.get()
        Liste_Livres = [] 
        for i in Liste_Livre.curselection():
            element = Liste_Livre.get(i)
            Liste_Livres.append(element)
        Mdp = Mot_De_Passe.get()
        Confirm_Mdp = Valider_MDP.get()
        identitque = meme_pseudo(pseudoo)
        if Mdp != Confirm_Mdp:  #verification de la saisie du meme mot de passe
            messagebox.showwarning('Attention', "Attention les mots de passes ne correspondent pas")
            Mot_De_Passe.delete(0,END)
            Valider_MDP.delete(0,END)
        elif identitque==True:          #Verifie si le pseudo existe deja dans readers.txt
            messagebox.showwarning('Attention', 'Ce pseudo existe deja')
            Pseudo.delete(0,END)
            Mot_De_Passe.delete(0,END)
            Valider_MDP.delete(0,END)
      
        else :  #Enregistre dans readers.txt
           pseudoo.encode('utf-8')   
           Enregistrer(pseudoo,genres,age,Style_Lecture,Liste_Livres,Mdp)
           matrice_init()
           messagebox.showinfo('Valider', 'Votre enregistrement a bien ete validé')
           Enregistrement_vers_accueil()
    

   
            

        
   
    # Initialisation de la fenetre :
    Fenetre_Enregistrement = Tk()                   #Appel de la fonction Tk pour créer un fenetre 
    Fenetre_Enregistrement.title("Enregistrement")      #Titre de la fenetre 
    Fenetre_Enregistrement.geometry("700x800")      #Taille de la fenetre  800 pixel de haut / 600 de Large

    #Création des bouttons : 
    Boutton_accueil = Button(Fenetre_Enregistrement,text='Accueil',bg="snow3",command=Enregistrement_vers_accueil)
    Boutton_Enregistrement = Button(Fenetre_Enregistrement,text="S'enregistrer",bg="snow3",font=('Arial',16),command=enregistrer)

    
    #Creation de Label :
    Indication_Page = Label(Fenetre_Enregistrement,text="Inscription",font=("Comic Sans MS",26,'underline'))
    Indication_Genre = Label(Fenetre_Enregistrement,text="Genre :",font=("Comic Sans MS",16))
    Indication_Pseudo = Label(Fenetre_Enregistrement,text='Pseudonyme :',font=('Comic Sans MS',16))
    Indication_Age = Label(Fenetre_Enregistrement,text='Age :',font=("Comic Sans MS",16))
    Indication_Style_Lecture = Label(Fenetre_Enregistrement,text='Style de Lecture :',font=("Comic Sans MS",16))
    Indication_Livres_Lus = Label(Fenetre_Enregistrement,text='Livres Lus :',font=('Comic Sans MS',16))
    Indication_MDP = Label(Fenetre_Enregistrement,text='Mot de Passe :',font=("Comic Sans MS",16))
    Indication_Confirmer_MDP = Label(Fenetre_Enregistrement,text='Confirmer le Mot de Passe :',font=("Comic Sans MS",14))
    #Entry :
    Pseudo = Entry(Fenetre_Enregistrement,font=("Comic Sans MS",16))
    Mot_De_Passe = Entry(Fenetre_Enregistrement,font=("Comic Sans MS",16),show='*')
    Valider_MDP = Entry (Fenetre_Enregistrement,font=("Comic Sans MS",16),show='*')

    #Livres deja lus :
    scrollbar_vertical = Scrollbar(Fenetre_Enregistrement,orient='vertical')
    All_livres = ListeLivres()

   
    Liste_Livre = Listbox(Fenetre_Enregistrement,yscrollcommand=scrollbar_vertical.set,selectmode='multiple',font=('Comic Sans MS',8),width=40)
    for i in range (len(All_livres)):
       Liste_Livre.insert(i,f"{i+1}   : {All_livres[i]}")
   #Creation d'une listbox pour afficher tous les livres disponibles dans books.txt
    
    scrollbar_vertical['command']=Liste_Livre.yview



    #Choix du Genre :
    Genres_Options = (
        "Homme",
        "Femme",
        "Peu Importe"
    )

    Boutton_Genres  = StringVar(Fenetre_Enregistrement)
    Boutton_Genres.set(Genres_Options[0])

    Option_Genre = OptionMenu(Fenetre_Enregistrement,Boutton_Genres,*Genres_Options)
    Option_Genre.config(width=9,bg='snow3',font=("Comic Sans MS",16))
    

     
    ###############

    #Choix Age :
    Age_option = (
        '<=18 ans',
        'Entre 18 et 25 ans',
        '> 25 '
    )
    Boutton_Age = StringVar(Fenetre_Enregistrement)
    Boutton_Age.set(Age_option[0])

    Option_Age = OptionMenu(Fenetre_Enregistrement,Boutton_Age,*Age_option)
    Option_Age.config(width=15,bg='snow3',font=("Commic Sans MS",16))

    #Choix Style de Lecture :
    Style_Lecture_Option = (
        '1. Science-fiction', 
        '2. Biographie', 
        '3. Horreur',
        '4. Romance',
        '5. Fable', 
        '6. Histoire', 
        '7. Comédie'
    )

    Boutton_Style_Lecture = StringVar(Fenetre_Enregistrement)
    Boutton_Style_Lecture.set(Style_Lecture_Option[0])

    Option_Style_Lecture = OptionMenu(Fenetre_Enregistrement,Boutton_Style_Lecture,*Style_Lecture_Option)
    Option_Style_Lecture.config(width=15,bg='snow3',font=("Comic Sans MS",16))




    
    
    
    #.grid() pour placer et afficher les elements 
    Frame(Fenetre_Enregistrement,width=10,height=10).grid(row=1,column=1)
    Frame(Fenetre_Enregistrement,width=140).grid(row=2,column=3)
    Indication_Page.grid(row=2,column=4)
    Boutton_accueil.grid(row=2,column=2)
    Frame(Fenetre_Enregistrement,height=30).grid(row=4,column=1)
    Indication_Pseudo.grid(row=5,column=3)
    Pseudo.grid(row=5,column=4)
    Frame(Fenetre_Enregistrement,height=20).grid(row=6,column=1)
    Option_Genre.grid(row=7,column=4)
    Indication_Genre.grid(row=7,column=3)
    Frame(Fenetre_Enregistrement,height=20).grid(row=8)
    Indication_Age.grid(row=9,column=3)
    Option_Age.grid(row=9,column=4)
    Frame(Fenetre_Enregistrement,height=20).grid(row=10)
    Indication_Style_Lecture.grid(row=11,column=3)
    Option_Style_Lecture.grid(row=11,column=4)
    Frame(Fenetre_Enregistrement,height=20,width=30).grid(row=12,column=1)
    Liste_Livre.grid(row=13,column=4,sticky='nsew')
    scrollbar_vertical.grid(row=13,column=5)
    Indication_Livres_Lus.grid(row=13,column=3)
    Frame(Fenetre_Enregistrement,height=20).grid(row=14)
    Mot_De_Passe.grid(row=15,column=4)
    Indication_MDP.grid(row=15,column=3)
    Frame(Fenetre_Enregistrement,height=20).grid(row=16)
    Frame(Fenetre_Enregistrement,height=20).grid(row=18)
    Valider_MDP.grid(row=19,column=4)
    Indication_Confirmer_MDP.grid(row=19,column=3)
    Frame(Fenetre_Enregistrement,height=40).grid(row=20)
    Boutton_Enregistrement.grid(row=21,column=4)



    Fenetre_Enregistrement.mainloop()


#Fenetre de connexion
def Fenetre_connexion():
    #Cette fonction gere la connexion 

    #Fonction  : 
    def Connexion_Principal():                            #Permets de Retourner a l'accueil
        Fenetre_connexion.destroy()
        Fenetre_Principal()
    
    def Login_(*args):              #Permet de se connecter
        pseudo= Pseudo_login.get()
        pseudo.encode('utf-8')
        Mdp = Pass_word_login.get()
        global mdp
        mdp = Hash_MDP(Mdp)
        login = Login(mdp,pseudo)
        if login[0]==True:  #Si la conenxion est valide
            messagebox.showinfo('Connexion Reussi',f'Bienvenue {login[1]} sur votre espace')
            Fenetre_connexion.destroy()
            global Pseudonyme
            Pseudonyme=login[1]
            Connexion_Fenetre() 
        elif login[0]==False:   #Si la connexion est refusé
            messagebox.showerror('Connexion echoue', "Attention le mot de passe  ou nom d'utilisateur n'existe pas")
            Pseudo_login.delete(0,END)
            Pass_word_login.delete(0,END)

    
#
                    

            
           


    # Initialisation de la fenetre :
    Fenetre_connexion = Tk()                   #Appel de la fonction Tk pour créer un fenetre 
    Fenetre_connexion.title("Connexion")      #Titre de la fenetre 
    Fenetre_connexion.geometry("600x600")      #Taille de la fenetre  400 pixel de haut / 300 de Large

    #Création des bouttons : 
    Boutton_accueil = Button(Fenetre_connexion,text='Accueil',bg="snow3",command=Connexion_Principal)
    Boutton_Validate = Button(Fenetre_connexion,text='Se connecter',bg="snow3", font =('Arial', 16 ),command=Login_)

    
   
    Pseudo_login = Entry(Fenetre_connexion,font=("Comic Sans MS",16))
    Pass_word_login = Entry(Fenetre_connexion,font=("Comic Sans MS",16))

    
    #Creation de Label :
    Indication_Pseudo_login = Label(Fenetre_connexion,text='Pseudonyme :',font=('Comic Sans MS',16))
    Indication_PassWord_login = Label(Fenetre_connexion,text='Mot de passe : ',font=('Comic Sans MS',16))
    Indication_Page = Label(Fenetre_connexion,text="Connexion",font=("Comic Sans MS",26,'underline'))


    
    
    
    #.grid() pour placer et afficher les elements 
    

   
    Frame(Fenetre_connexion,width=10,height=10).grid(row=1,column=1) #Frame : Espace blanc qui permets de gerer l'espace entre les widgets
    Frame(Fenetre_connexion,width=170).grid(row=2,column=3)    
    Indication_Page.grid(row =2, column= 4)
    Boutton_accueil.grid(row=2, column=2)
    Pseudo_login.grid(row=4, column= 4)
    Frame(Fenetre_connexion,width=50).grid(row=4,column=1)
    Indication_Pseudo_login.grid(row = 4, column = 3)
    Frame(Fenetre_connexion,width=10,height=80).grid(row=5,column=1)
    Indication_PassWord_login.grid(row=6, column =3 )
    Pass_word_login.grid(row = 6, column = 4)
    Frame(Fenetre_connexion, width= 10, height= 80).grid(row=8,column=4)
    Boutton_Validate.grid(row=16, column= 4)

    
    
    

    Fenetre_connexion.mainloop()

def Connexion_Fenetre():
    #Cette fonction gere la page une fois connecté elle affiche trois bouttons qui permettent d'acceder aux différentes fonctionnalités
    #Fonction
    def Deco(): #Permet de se deconnecter
        ConnexionFenetre.destroy()
        Fenetre_Principal()
    def Profil():   #Permets d'afficher son profil
        ConnexionFenetre.destroy()
        Fenetre_Profil()
        
    def Depot_livre():      #Permets d'acceder au dépot de livre
        ConnexionFenetre.destroy()
        Depotlivre()
    
    def Reco(): #Permets d'acceder au system de recommandation
        ConnexionFenetre.destroy()
        Recommandation()

    ConnexionFenetre = Tk()
    ConnexionFenetre.geometry("1080x800")
    ConnexionFenetre.title(f'{Pseudonyme}')

    #Bouttons
    Deconnexion = Button(ConnexionFenetre,text='Deconnexion',command=Deco,bg='snow3')
    Profil_Lecteur = Button(ConnexionFenetre,text='Votre Profil',font=("Arial",18),width=10,bg='snow3',command=Profil)
    Depot_livres = Button(ConnexionFenetre,text='Dépot des Livres',font=("Arial",18),bg='snow3',command=Depot_livre)
    Recomandation = Button(ConnexionFenetre,text='Livres recommandés pour vous',font=('Arial',18),bg="snow3",command=Reco)





    Frame(height=10,width=10).grid(row=0,column=0)
    Deconnexion.grid(row=1,column=1)
    Frame(height=250,width=100).grid(row=2,column=2)
    Profil_Lecteur.grid(row=3,column=3)
    Frame(width=10).grid(row=3,column=4)
    Depot_livres.grid(row=3,column=5)
    Frame(width=10).grid(row=3,column=6)
    Recomandation.grid(row=3,column=7)


    ConnexionFenetre.mainloop()

def Fenetre_Profil():
    #Cette fonction gere l'affichage du profil 

    def Deco(): #Permet de se deconnecter
        FenetreProfil.destroy()
        Connexion_Fenetre()
    def Modif_Profil(): #Permet de lancer la modification du profil
        FenetreProfil.destroy()
        Fenetre_modif()
    
    def Suppr_Profil():     #Permet d'acceder a la page pour supprimer son profil
        FenetreProfil.destroy()
        Suppr_confirm()
        

    global Info_Profil,Info_Livre_lu
    
    Info_Profil = Info_Login(Pseudonyme)
    Info_Books_Read = Info_Books(Pseudonyme)
    
    FenetreProfil = Tk()
    FenetreProfil.geometry("900x600")
    FenetreProfil.title(f'Profil de {Pseudonyme}')


    Deconnexion = Button(FenetreProfil,text='Accueil',command=Deco,bg='snow3')
    Pseudo_Label = Label(FenetreProfil,text='Pseudonyme :',font=('Comic Sans MS',18))
    Pseudo = Label(FenetreProfil,text=Pseudonyme,font=("Comic Sans MS",18),bg='LightSteelBlue3')
    Genre_Label = Label(FenetreProfil,text='Genre :',font=("Comic Sans MS",18))
    Genre = Label(FenetreProfil,text=Info_Profil[0],font=("Comic Sans MS",18),bg='LightSteelBlue3')
    Age_Label = Label(FenetreProfil,text="Age :",font=('Comic Sans MS',18))
    Age = Label(FenetreProfil,text=Info_Profil[1],font=("Comic Sans MS",18),bg='LightSteelBlue3')
    Style_Lecture_Label = Label(FenetreProfil,text='Style de lecture :',font=('Comic Sans MS',18))
    Style_Lecture =  Label(FenetreProfil,text=Info_Profil[2],font=("Comic Sans MS",18),bg='LightSteelBlue3')
    Livres_Lu = Label(FenetreProfil,text="Livres Lus :",font=('Comic Sans MS',18))

    Info_Livre_lu = []
    Livres_Lus = []
    if Info_Books_Read==None:
        Livres_Lus.append('Aucun')
    else :
        for i in Info_Books_Read[0]:
            Info_Livre_lu.append(i)
        Livres_Lus = Info_Livre_lu
   
    Boutton_Livres_Lus = StringVar(FenetreProfil)
    Boutton_Livres_Lus.set(Livres_Lus[0])

    Option_Livres_Lus = OptionMenu(FenetreProfil,Boutton_Livres_Lus,*Livres_Lus)
    Option_Livres_Lus.config(width=30,bg='LightSteelBlue3',font=("Comic Sans MS",14))


    Boutton_Modifier = Button(FenetreProfil,text='Modifier Mon Profil',font=("Comic Sans MS",18),bg='snow3',command=Modif_Profil)
    Boutton_Supprimer = Button(FenetreProfil,text='Supprimer Mon Profil',font=("Comic Sans MS",18),bg='snow3',command=Suppr_Profil)


    #Placement 

    Frame(height=20,width=10).grid(row=0,column=0)
    Deconnexion.grid(row=1,column=1)
    Frame(height=50,width=30).grid(row=2,column=2)
    Pseudo_Label.grid(row=3,column=3)
    Frame(height=20).grid(row=4,column=3)
    Frame(width=30).grid(row=4,column=4)
    Pseudo.grid(row=3,column=5)
    Frame(width=30).grid(row=5,column=4)
    Frame(height=20).grid(row=5,column=3)
    Genre_Label.grid(row=6,column=3)
    Genre.grid(row=6,column=5)
    Frame(height=20).grid(row=7,column=3)
    Frame(width=30).grid(row=7,column=4)
    Age.grid(row=8,column=5)
    Age_Label.grid(row=8,column=3)
    Frame(height=20).grid(row=9,column=3)
    Frame(width=30).grid(row=9,column=4)
    Style_Lecture.grid(row=10,column=5)
    Style_Lecture_Label.grid(row=10,column=3)
    Frame(height=20).grid(row=11,column=3)
    Frame(width=30).grid(row=11,column=4)
    Livres_Lu.grid(row=12,column=3)
    Option_Livres_Lus.grid(row=12,column=5)
    Frame(height=30).grid(row=13,column=3)
    Boutton_Modifier.grid(row=14,column=3)
    Boutton_Supprimer.grid(row=14,column=5)






    FenetreProfil.mainloop()


def Fenetre_modif():
    #Cette fonction affiche une page contenant des entrés pour modifer son pseudo,genre,age,stylede lecture et les livres lus par l'utilisateur

    
    
    #Fonction :
    def Modif_pour_Profil():                 #Permet de retourner a l'accueil
        Fenetre_Modif.destroy()
        Fenetre_Principal()
    def Profil():   #Permet de retourner voir son profil
        Fenetre_Modif.destroy()
        Fenetre_Profil()
    def enregistrer(*args): #Permet de modifier ses informations dans readers.txt
        global Pseudo_Modif
        Pseudo_Modif = Pseudo.get()
        genres = Boutton_Genres.get()
        age = Boutton_Age.get()
        Style_Lecture = Boutton_Style_Lecture.get()
        Liste_Livres = [] 
        for i in Liste_Livre.curselection():
            element = Liste_Livre.get(i)
            Liste_Livres.append(element)
        

        
        if Pseudo_Modif != Pseudonyme:
            identitque = meme_pseudo(Pseudo_Modif)
            if identitque==True:
                messagebox.showwarning('Attention', 'Ce pseudo existe deja')
                Pseudo.delete(0,END)
           
        if Pseudo_Modif==Pseudonyme or meme_pseudo(Pseudo_Modif)==False:
            Pseudo_Modif.encode('utf-8')   
            Modif(Pseudonyme,genres,age,Style_Lecture,Liste_Livres,Pseudo_Modif)
            messagebox.showinfo('Enregistrement', "Vos modifications ont été enregistré veuillez vous reconnecter")
            Modif_pour_Profil()
    

   


        
   
    # Initialisation de la fenetre :
    Fenetre_Modif = Tk()                   #Appel de la fonction Tk pour créer un fenetre 
    Fenetre_Modif.title('Modification du Profil')      #Titre de la fenetre 
    Fenetre_Modif.geometry("700x800")      #Taille de la fenetre  800 pixel de haut / 600 de Large

    #Création des bouttons : 
    Boutton_accueil = Button(Fenetre_Modif,text='Accueil',bg="snow3",command=Profil)
    Boutton_Modif = Button(Fenetre_Modif,text='Modifier',bg='snow3',command=enregistrer,font=("Comic Sans MS",16))


    
    #Creation de Label :
    Indication_Page = Label(Fenetre_Modif,text="Modification",font=("Comic Sans MS",26,'underline'))
    Indication_Genre = Label(Fenetre_Modif,text="Genre :",font=("Comic Sans MS",16))
    Indication_Pseudo = Label(Fenetre_Modif,text='Pseudonyme :',font=('Comic Sans MS',16))
    Indication_Age = Label(Fenetre_Modif,text='Age :',font=("Comic Sans MS",16))
    Indication_Style_Lecture = Label(Fenetre_Modif,text='Style de Lecture :',font=("Comic Sans MS",16))
    Indication_Livres_Lus = Label(Fenetre_Modif,text='Livres Lus :',font=('Comic Sans MS',16))
    
    #Entry :
    Pseudo = Entry(Fenetre_Modif,font=("Comic Sans MS",16))
    Pseudo.insert(0,Pseudonyme)
    
    

    scrollbar_vertical = Scrollbar(Fenetre_Modif,orient='vertical')
    All_livres = ListeLivres()
    
    
            

   
    Liste_Livre = Listbox(Fenetre_Modif,yscrollcommand=scrollbar_vertical.set,selectmode='multiple',font=('Comic Sans MS',8),width=40)
    for i in range (len(All_livres)-1):
       Liste_Livre.insert(i,f"{i+1}   : {All_livres[i]}")
   
    
    scrollbar_vertical['command']=Liste_Livre.yview



    #Choix du Genre :
    Genres_Options = (
        "Homme",
        "Femme",
        "Peu Importe"
    )

    Boutton_Genres  = StringVar(Fenetre_Modif)
    Boutton_Genres.set(Info_Profil[0])

    Option_Genre = OptionMenu(Fenetre_Modif,Boutton_Genres,*Genres_Options)
    Option_Genre.config(width=9,bg='snow3',font=("Comic Sans MS",16))
    

     
    ###############

    #Choix Age :
    Age_option = (
        '<=18 ans',
        'Entre 18 et 25 ans',
        '> 25 '
    )
    Boutton_Age = StringVar(Fenetre_Modif)
    Boutton_Age.set(Info_Profil[1])

    Option_Age = OptionMenu(Fenetre_Modif,Boutton_Age,*Age_option)
    Option_Age.config(width=15,bg='snow3',font=("Commic Sans MS",16))

    #Choix Style de Lecture :
    Style_Lecture_Option = (
        'Science-fiction', 
        'Biographie', 
        'Horreur',
        'Romance',
        'Fable', 
        'Histoire', 
        'Comédie'
    )

    Boutton_Style_Lecture = StringVar(Fenetre_Modif)
    Boutton_Style_Lecture.set(Info_Profil[2])

    Option_Style_Lecture = OptionMenu(Fenetre_Modif,Boutton_Style_Lecture,*Style_Lecture_Option)
    Option_Style_Lecture.config(width=15,bg='snow3',font=("Comic Sans MS",16))




    
    
    
    #.grid() pour placer et afficher les elements 
    Frame(Fenetre_Modif,width=10,height=10).grid(row=1,column=1)
    Frame(Fenetre_Modif,width=140).grid(row=2,column=3)
    Indication_Page.grid(row=2,column=4)
    Boutton_accueil.grid(row=2,column=2)
    Frame(Fenetre_Modif,height=30).grid(row=4,column=1)
    Indication_Pseudo.grid(row=5,column=3)
    Pseudo.grid(row=5,column=4)
    Frame(Fenetre_Modif,height=20).grid(row=6,column=1)
    Option_Genre.grid(row=7,column=4)
    Indication_Genre.grid(row=7,column=3)
    Frame(Fenetre_Modif,height=20).grid(row=8)
    Indication_Age.grid(row=9,column=3)
    Option_Age.grid(row=9,column=4)
    Frame(Fenetre_Modif,height=20).grid(row=10)
    Indication_Style_Lecture.grid(row=11,column=3)
    Option_Style_Lecture.grid(row=11,column=4)
    Frame(Fenetre_Modif,height=20,width=30).grid(row=12,column=1)
    Liste_Livre.grid(row=13,column=4,sticky='nsew')
    scrollbar_vertical.grid(row=13,column=5)
    Indication_Livres_Lus.grid(row=13,column=3)
    Frame(Fenetre_Modif,height=20).grid(row=14)
    Boutton_Modif.grid(row=15,column=4)



    Fenetre_Modif.mainloop()

def Suppr_confirm():
    #Cette fonction affiche une page qui demande la confirmation pour supprimer un utilisateur
    Supp = Tk()
    Supp.geometry("250x200")
    Supp.title('SUPPRESSION')
    def Suppr ():   #Permets d'appeler la fonction pour supprimer l'utilisateur
        suppr_l_matrice(Pseudonyme)
        SupprimerPseudo(Pseudonyme)
        messagebox.showwarning('Attention', 'Vous venez de supprimer votre compte')
        Deco()
        

    def Deco ():    #Pour se deconnecter
        Supp.destroy()
        Fenetre_Principal()

    Boutton_Suppr = Button(Supp,text='Supprimer',font=('Arial Black',22),bg='SlateBlue1',command=Suppr)
    Boutton_Annuler = Button(Supp,text='Annuler',font=('Arial Black',22),bg='SlateBlue1',command=Deco)

    
    
    Frame(width=30,height=20).grid(row=0,column=0)
    Boutton_Suppr.grid(row=1,column=1)
    Frame(height=15).grid(row=2,column=0)
    Boutton_Annuler.grid(row=3,column=1)

    
    
    Supp.mainloop()


def Depotlivre():
    #Cette fonction gere le depot de livres

    def Suppr_Livre():   #Cette fonction permets de supprimer un livre du depot
        Livre_Modif = Boutton_Livres_Lus.get()
        modif_matrice_s(Livre_Modif)
        messagebox.showwarning('Attention', f'Vous venez de supprimer le livre : {Livre_Modif} de la liste')
        Depot.destroy()
        Recup_Livre_Supp(Livre_Modif)
        Connexion_Fenetre()

    def Modif_Titre_Livre():    #Permets de modifier le titre d'un livre du depot
        Depot.destroy()
        Livre_Modif = Boutton_Livres_Lus.get()
        Modif_Titre()
        Valeur_Modif = Modif_valeur
                
        Recup_Livre_Modif(Livre_Modif,Valeur_Modif)
        Connexion_Fenetre()

    def Deco(): #Permets de se deconnecter
        Depot.destroy()
        Connexion_Fenetre()     
    
    def Ajouter_Livres():   #Permets d'ajouter un livre au depot
        modif_matrice_a()
        Depot.destroy()
        Ajouter_Livre()
        
    

    Depot = Tk()
    Depot.title('Dépot des livres')
    Depot.geometry('500x600')

    Select_Books = ListeLivres()

    Boutton_Livres_Lus = StringVar(Depot)
    Boutton_Livres_Lus.set(Select_Books[0])

    Option_Livres_Lus = OptionMenu(Depot,Boutton_Livres_Lus,*Select_Books)
    Option_Livres_Lus.config(width=30,bg='LightSteelBlue3',font=("Comic Sans MS",14))

    Select_Books_Label = Label(Depot,text='Selectionner un livre :',font=('Comic Sans MS',14))

    Bouton_Add = Button(Depot,text='Ajouter un Livre',font=('Comic Sans MS',16),bg='snow3',command=Ajouter_Livres)
    Boutton_modif = Button(Depot,text='Modifier le titre du livre',font=("Comic Sans MS",16),bg='snow3',command=Modif_Titre_Livre)
    Boutton_Supp =  Button(Depot,text='Supprimer le livre',font=("Comic Sans MS",16),bg='snow3',command=Suppr_Livre)
    Boutton_Accueil = Button(Depot,text='Accueil',bg='snow3',command=Deco)
    
    
    Frame(width=10,height=20).grid(row=0,column=0)
    Boutton_Accueil.grid(row=1,column=1)
    Frame(height=80,width=40).grid(row=2,column=2)
    Select_Books_Label.grid(row=3,column=2)
    Frame(height=30).grid(row=4,column=2)
    Option_Livres_Lus.grid(row=5,column=2)
    Frame(height=100).grid(row=6,column=2)
    Boutton_modif.grid(row=7,column=2)
    Frame(height=20).grid(row=8,column=2)
    Boutton_Supp.grid(row=9,column=2)  
    Frame(height=20).grid(row=10,column=2)
    Bouton_Add.grid(row=11,column=2)  

    Depot.mainloop()


def Modif_Titre():
    #Cette fonction demande un nouveau titre pour un titre donné afin de le modifier

    def Modif_Val():    #Appel la fonction pour modifier le titre
        global Modif_valeur
        Modif_valeur = Titre_Modif.get()
        Modif.destroy()

   

    Modif = Tk()
    Modif.geometry('700x150')
    Modif.title('Modification')

    Label_Titre = Label(Modif,text='Entrez le nouveau titre :',font=('Comic Sans MS',16))
    Titre_Modif = Entry(Modif,width=30,font=('Comic Sans MS',12))
    Boutton_Modif = Button(Modif,text='Modifier',font=('Comic Sans MS',14),bg='snow3',command=Modif_Val)
    

    Frame(height=40,width=40).grid(row=0,column=0)
    Label_Titre.grid(row=1,column=1)
    Frame(width=20).grid(row=1,column=2)
    Titre_Modif.grid(row=1,column=3)
    Boutton_Modif.grid(row=2,column=1)
    
    Modif.mainloop()

def Ajouter_Livre():    #Permets d'ajouter un livre au depot
    AjouterLivre = Tk()
    AjouterLivre.geometry('500x300')
    AjouterLivre.title('Ajouter un Livre')

    def Add():
        
        Titre_Add = Titre_Livre.get()
        AjouterLivre.destroy()
        Ajouter_Livre_Txt(Titre_Add)
        Connexion_Fenetre()

    Label_entrer = Label(AjouterLivre,text='Entrer un titre :',font=('Comic Sans MS',16))
    Titre_Livre = Entry(AjouterLivre,font=('Comic Sans MS',16))

    Boutton_Valider = Button(AjouterLivre,text='Enregistrer ',font=("Comic Sans MS",16),bg='snow3',command=Add)

    Frame(height=50,width=40).grid(row=0,column=0)
    Label_entrer.grid(row=1,column=1)
    Frame(width=20).grid(row=1,column=2)
    Titre_Livre.grid(row=1,column=3)
    Frame(height=20).grid(row=2)
    Boutton_Valider.grid(row=3,column=3)

    AjouterLivre.mainloop()


def Recommandation():
    #Cette fonction gere la page de notation

    def Accueil(): #Permets de retourner a l'accueil
        Recoo.destroy()
        Connexion_Fenetre()
    
    def Note(): #Permets d'ajouter une note 
        Recoo.destroy()
        note_()
    Recoo = Tk()
    Recoo.geometry('350x300')
    Recoo.title('Recomandation')
    
    Bouton_Ajouter_Note = Button(Recoo,text="Ajouter une note",font=("Comic Sans MS",16),bg='snow3',command=Note)
    Boutton_Reco = Button(Recoo)
    Boutton_Accueil = Button(Recoo,text='Accueil',bg='snow3',command=Accueil)

    Frame(height=20,width=20).grid(row=0,column=0)
    Boutton_Accueil.grid(row=1,column=1)
    Frame(height=50,width=20).grid(row=2,column=2)
    Bouton_Ajouter_Note.grid(row=3,column=3)



    Recoo.mainloop()

def note_():

    def Accueil(): #Permets de retourner a l'accueil
        note.destroy()
        Connexion_Fenetre()
    
    def noter_livre(): #Permets de noter un livre en appelant la fonction noter_livre_()
        Note = Boutton_Note.get()
        Livre = Boutton_Livres_Lus.get()
        noter_livre_(Pseudonyme,Note,Livre)
        note.destroy()
        Connexion_Fenetre()
    
    note = Tk()
    note.geometry('800x400')
    note.title('Noter un Livre')

    boutton_Accueil = Button(note,text='Accueil',command=Accueil,bg='snow3')
    selection_titre_label = Label(note,text='Selectionner un titre : ',font=('Comic Sans MS',16))

    Info_Livre = Info_Books(Pseudonyme)
    Info_Livre_lu = []
    Livres_Lus = []
    if Info_Livre==None:
        Livres_Lus.append('Aucun')
    else :
        for i in Info_Livre[0]:
            Info_Livre_lu.append(i)
        Livres_Lus = Info_Livre_lu
   
    Boutton_Livres_Lus = StringVar(note)
    Boutton_Livres_Lus.set(Livres_Lus[0])

    Option_Livres_Lus = OptionMenu(note,Boutton_Livres_Lus,*Livres_Lus)
    Option_Livres_Lus.config(width=30,bg='LightSteelBlue3',font=("Comic Sans MS",14))
    
    
    Boutton_noter = Button(note,text='Noter',font=('Comic Sans MS',16),bg='snow3',command=noter_livre)

    

    Note_Options = (
        1,
        2,
        3,
        4,
        5
    )

    Boutton_Note  = StringVar(note)
    Boutton_Note.set(Note_Options[0])

    Option_Note = OptionMenu(note,Boutton_Note,*Note_Options)
    Option_Note.config(width=9,font=("Comic Sans MS",16),bg='LightSteelBlue3')

    Note_Label = Label(note,text='Note :',font=('Comic Sans MS',16))

    Frame(width=20,height=20).grid(row=0,column=0)
    boutton_Accueil.grid(row=1,column=1)
    Frame(width=30,height=20).grid(row=2,column=1)
    selection_titre_label.grid(row=3,column=2)
    Frame(width=10).grid(row=3,column=3)
    Option_Livres_Lus.grid(row=3,column=4)
    Frame(height=50).grid(row=4,column=3)
    Option_Note.grid(row=5,column=4)
    Note_Label.grid(row=5,column=2)
    Frame(height=30).grid(row=6,column=2)
    Boutton_noter.grid(row=7,column=4)

    note.mainloop()

if __name__=='__main__':
    Fenetre_Principal() #Appel de la fonction pour lancer le programme

    


