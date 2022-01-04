# Projet : Systeme de recommandation de livres  ( projet L1)
#Ce fichier sers a modifer le profil de l'utilisateur - supprimer l'utilisateur - afficher les infos de l'utilisateur

from tkinter.constants import E, S, W
from typing import ChainMap
import main

def Info_Login(pseudo):
    #Cette fonction recupere les info de l'utilisateur dans readers.txt et appelle: convert_Info() pour retransformer les valeurs en string
    #Entrée  : pseudo ; readers.txt 
    #Sortie : i : un tuple contant les infos de l'utilisateur
    with open('readers.txt','r',encoding='utf-8') as f:
        L = []
        Ligne=f.readline()
        L.append([Ligne])
        while Ligne !='':
            Liste = []
            Ligne=f.readline()
            Liste.append(Ligne)
            L.append(Liste)
    for i in L:
        for j in i:
            Var = j.split(',')
            if Var[0]==pseudo:
               return convert_Info(i)
        
def convert_Info(tuple):
    #Cette fonction convertit les int associé aux donnés de l'utilisateur
    #Entrée : un tuple avec toutes les données de l'utilisateur sous forme de : pseudo,1,2,etc
    #Sortie : Une liste avec les infos sous forme : [pseudo,'Homme',etc...]

    Liste_Info = []

    for i in tuple:
        var = i.split(',')
        Liste=var
    Dico_Genre ={'1':'Homme',
                 '2':"Femme",
                 '3':"Peu Importe"}  

    Dico_Age = {'1':'<=18 ans',
                '2':'Entre 18 et 25 ans',
                "3":'> 25 '} 


    Dico_Style_Lecture = {'1':'Science-fiction',
                          '2':'Biographie',
                          '3':'Horreur',
                          '4':'Romance',
                          '5':'Fable',
                          '6':'Histoire',
                          '7':'Comédie'}

    Liste.pop(-1)               #Suppression du mot de passe qui est present dans la liste

    Liste_Info.append(Dico_Genre[Liste[1]])
    Liste_Info.append(Dico_Age[Liste[2]])    
    Liste_Info.append(Dico_Style_Lecture[Liste[3]]) 

    return(Liste_Info)

def Info_Books(pseudo):
    #Cette fonction permets de recuperer  les indices des livres lus par l'utilisateur 
    #Entrée : pseudo ; booksread.txt
    #Sortie : appelle de la fonction convert_books()
    with open('booksread.txt','r',encoding='utf-8') as f:
        L = []
        Ligne=f.readline()
        L.append([Ligne])
        while Ligne !='':
            Liste = []
            Ligne=f.readline()
            Liste.append(Ligne)
            L.append(Liste)
    for i in L:
        for j in i:
            Var = j.split(',')
            if Var[0]==pseudo :
               return(convert_books(i)) #i est une liste qui contient : [pseudo,indicelivre,Etc...]
            
            
            

def convert_books(Liste_info_books):
    #Cette fonction permets de transformer les indices des livres en titres des livres
    #Entrée : Liste : contenants les indices des livres lus
    Liste = []
    Livre_Lus = []
    Liste_Books_Read = []
    for i in Liste_info_books:
        var =i.split(',')
        Liste.append(var)
    for i in Liste:
        for j in i:
            var=j.split('\n')
    if var[0]=='':
        Livre_Lus.append('Aucun')
        return(Livre_Lus,Liste_Books_Read)  #Si l'utilisateur n'a lus aucun livres 
    Liste_int = []
    for i in Liste:
        for j in range(1,len(i)):
            Liste_int.append(int(i[j]))
    
    with open('books.txt','r',encoding='utf-8') as b :
        Ligne = b.readline()
        Liste_Books = [Ligne]
        while Ligne !='':
            Ligne = b.readline()
            Liste_Books.append(Ligne)
    
    for i in range(len(Liste_Books)-1):
        if i+1 in Liste_int:
            Livre_Lus.append(Liste_Books[i])
    return(Livre_Lus,Liste_Books_Read)  #quand l'utilisateur a lus plusieurs livres
    


def Modif(Pseudo,genres,age,Style_Lecture,Liste_Livres,Pseudo_Modif):
    #Cette fonction permets de modifier les info dans readers.txt d'un utilisateur
    #Entrée : Pseudo:le pseudo actuel de l'utilisateur, genres : le genres de l'utilisateur ; age : son age ; Style_Lecture : son style de lecture
    #Liste_Livres : les livres qu'il a lus ; Pseudo_Modif : son nouveau pseudo ; readers.txt ; booksread.txt
    #Sortie : readers.txt modifie ; booksread.txt : modifié
    global Pseudonyme
    Pseudonyme = Pseudo
    Style_Lecture_ = Style_Lecture
    Dico_Genre = {'Homme':1,
                  'Femme':2,
                  'Peu Importe':3}

    Dico_Age = {'<=18 ans':1,
                'Entre 18 et 25 ans':2,
                '> 25 ':3}
    
    Dico_Style_Lecture = {'Science-fiction':1,
                          'Biographie':2,
                          'Horreur':3,
                          'Romance':4,
                          'Fable':5,
                          'Histoire':6,
                          'Comédie':7}

    
    with open('readers.txt','r',encoding='utf-8') as modif_file1, open('booksread.txt','r',encoding='utf-8') as modif_file_2:

        Liste1 = modif_file1.readlines()
        N_Liste = []
        for i in Liste1:
            var = i.split(',')
            N_Liste.append(var)
        
          
        for i in N_Liste:                           #récuperation de ses informations
            if i[0]==Pseudonyme:
                i[0]=Pseudo_Modif
                i[1]=Dico_Genre[genres]
                i[2]=Dico_Age[age]
                i[3]=Dico_Style_Lecture[Style_Lecture_]

        D_Liste =[]
        Liste2 = modif_file_2.readlines()
        for i in Liste2:
            var = i.split(',')
            D_Liste.append(var)
        I_Livre = []
        for i in Liste_Livres:
            var_livre= i.split('   :')
            I_Livre.append(var_livre)
        Liste_F = []
        for j in D_Liste:
            if len(j)==1:
                for i in j:
                    var = i.split('\n')
                    Liste_F.append(var)
            else : 
                Liste_F.append(j)
        for j in Liste_F:
            if j[0]==Pseudonyme:
                j[0]=Pseudo_Modif
                for i in I_Livre:
                    
                    if i[0] not in j:
                        j.append(i[0])
       
  

        for element in Liste_F:
            for i in range(len(element)-1) :
                if element[i]=='':
                    pass
        
        L = []                                  #Sécurité pour les cas ou : -il a lus aucun livres -il a lus plusieurs livres        
        for element in Liste_F:
                if '' not in element:
                    t = ','.join(element)   
                    L.append(t)
                elif element[-1]=='' :
                    L.append(element[0])
                else:
                    for i in range(len(element)-1):
                        if element[i]=='':
                            element.pop(i)
                    t = ','.join(element)
                    L.append(t)
        
               
                              

         
    with open('readers.txt','w',encoding='utf-8') as f ,open('booksread.txt','w',encoding='utf-8') as f2:   #Modification des informations dans les fichiers
        
        for i in N_Liste:
            c = 0
            for j in i:
                f.write(str(j))
                if c<=3:
                    t = 6
                    f.write(',')
                c+=1
        Liste_Propre = []
        for w in L:
            val = w.split(',')
            Liste_Propre.append(val)
        for a in Liste_Propre:
            for element in range (len(a)):
                if '\n' in a[element]:
                    val = a[element]
                    a.pop(element)
                    a.append(val)
        for e in Liste_Propre:
            L=[]
            if '\n' in e[-1]:
                t=','.join(e)
                L.append(t)
                f2.write(L[0])
            else :
                t=','.join(e)
                L.append(t)
                f2.write(f"{L[0]} \n")







def SupprimerPseudo(pseudo):
    #Cette fonction permets de recuperer les infos a supprimer
    #Entrée : pseudo ; booksread.txt ; readers.txt
    #Sortie : Suppr_Books() ; Suppr_User()
    with open('readers.txt','r',encoding='utf-8') as f , open('booksread.txt','r',encoding='utf-8') as f2:
        Liste_Compte = f.readlines()
        for i in range (len(Liste_Compte)):
            if Liste_Compte[i][0]==pseudo:
                Liste_Compte.pop(i)
        
        Liste_Livres = f2.readlines()
        User_Livre = []
        L = []
        
        for i in Liste_Livres:
            var = i.split('\n')
            L.append(var)
        for i in L:
            i.pop(-1)
        User_Livre = []
        for j in L:
            for element in j:
                val = element.split(',')
                User_Livre.append(val)
        for i in range(len(User_Livre)):
            if User_Livre[i][0]==pseudo:
                User_Livre.pop(i)

        return(Suppr_Books(User_Livre),Suppr_User(Liste_Compte))

def Suppr_User(User_L):
    #Cette fonction permets de supprimer un utilisateur dans readers.txt
    #Entrée : User_L:les infos de l'utilisateur
    #Sortie : le fichier readers.txt avec l'utilisateur en moins
    with open('readers.txt',"w",encoding='utf-8') as sup_us:
        for element in User_L:
           sup_us.write(element)

def Suppr_Books(User_l):
    #Cette fonction permets de supprimer un utilisateur dans booksread.txt
    #Entrée : User_l : la liste des livres lus par l'utilisateur
    #Sortie : booksread.txt sans l'utilisateur
    with open ('booksread.txt','w') as s_books :
        L_Final = []

        for i in range(len(User_l)):
            t = ','.join(User_l[i])
            L_Final.append(t)
        for i in L_Final:
            s_books.write(f"{i}\n")  
        
       
