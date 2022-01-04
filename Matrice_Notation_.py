# Projet : Systeme de recommandation de livres  ( projet L1)
#Ce fichier python sert à modifier le fichier Notation.txt qui contient la matrice de notation

def matrice_init():
    #Cette fonction sert a initialiser la matrice de notation elle est appelé a chaque enregistrement d'un nouvel utilisateur
    #Entrée : books.txt ; readers.txt ; Notation.txt
    #Sortie : Notation.txt : La matrice est modifié
    with open("books.txt", "r",encoding='utf-8') as f1, open("readers.txt", "r",encoding='utf-8') as f2, open('Notation.txt','r')as f3:
        c = f1.readlines()
        L = f2.readlines()
        ligne = 0
        for s in c:                     #Récuperation du nombre de ligne a initialisé dans la matrice en fonction du nombre d'utilisateurs inscrit
            if s != "\n":
                ligne += 1
        user = f3.readlines()
        user_n = 0
        for s in user:
            if s !='\n':
                user_n += 1
        


        colonne = 0                                 #Récuperation du nombre de colonne a initialiser dans la matrice en fonction du nombre de livres enregistrés
        for s in L: 
            if s!= "\n":
             colonne += 1
        
        matricenotation=[]
        
        if user_n!=colonne:         #Ajout d'une ligne dans la matrice

            
            for i in range(ligne):
                matricenotation.append(0)

        with open ('Notation.txt','a') as f:
            if matricenotation!=[]:
                for element in matricenotation:
                    f.write(f'{element} ')
                f.write("\n")                   #Notation.txt est initialisé en fonction du nombre d'utilisateurs enregistrés

def suppr_l_matrice(pseudo):
    #Cette fonction permets de supprimer une ligne  dans la matrice lors de la suppression d'un utilisateur
    #Entrée  : pseudo:le pseudo de l'utilisateur connecté ; Notation.txt ; readers.txt ; 
    #Sortie  : Notation.txt : la matrice modifié
    with open ('Notation.txt','r') as f,open('readers.txt','r',encoding='utf-8') as f2:
        M = f2.readlines()
        L = []
    
        M2 = f.readlines()

        for element in M:
            var = element.split(',')
            L.append(var)
        for element in range(len(L)):       
            if L[element][0]==pseudo:
                M2.pop(element)                 #Suppression de la ligne de l'utilisateur concerné
    with open ('Notation.txt','w') as f:
        for element in M2:
            f.write(element)        #réécriture de la nouvelle matrice


def modif_matrice_s(titre_modif):
    #Cette fonction permet de supprimer une colonne dans la matrice lors de la suppression d'un livre dans books.txt
    #Entrée : titre_modif: le titre supprimé dans books.txt ; Notation.txt ; books.txt
    #Sortie : Notation.txt avec la colonne du livre suppr en moins
    with open('books.txt','r',encoding='utf-8') as f, open('Notation.txt','r') as f2:
        M = f.readlines()
        M2 = f2.readlines()
        L = []
        for i in M2:                    #Recuperation de la colonne du livre supprimer
            var = i.split(' ')
            var.pop(-1)
            L.append(var)
        for i in range(len(M)):
            
            if M[i]==titre_modif + '\n':    #suppression de la colonne dans la matrice
                for j in L:
                    j.pop(i)
    with open ('Notation.txt','w') as f3:
        for element in L:
            for i in element:
                f3.write(f"{i} ")
            f3.write('\n')              #Réécriture de la matrice

def modif_matrice_a():
    #Cette fonction sert à ajouter une colonne lorsque l'on rajoute un livre à books.txt
    #Entrée : Notation.txt
    #Sortie : Notation.txt avec une colonne en plus
    with open('Notation.txt','r') as f:
        M = f.readlines()
        L = []
        for i in M:
            var = i.split(' ')
            var.pop(-1)
            L.append(var)
        for element in L:
            element.append('0')                 #Ajout d'une colonne initialisé a 0 
    with open('Notation.txt','w') as f2:
        for element in L:
            for i in element:
                f2.write(f"{i} ")
            f2.write('\n')
        
        
    
def noter_livre_(pseudo,note,livre):
    #Cette fonction sert à noter un livre pour un utilisateur donné
    #Entrée : pseudo:le pseudo de l'utilisateur ; note:la note donné par l'utilisateur ; livre : le titre du livre que l'utilisateur à noté ; books.txt ; readers.txt ; Notation.txt
    #Sortie : Notation.txt contenant la note de l'utilisateur dans la colonne du livre choisis par celui-ci  
    with open ('readers.txt','r',encoding='utf-8')as f1 , open('books.txt','r',encoding='utf-8')as f2, open('Notation.txt','r')as f3:
        M = f1.readlines()

        L = []

        for element in M:
            var = element.split(',')
            L.append(var)
        for element in range(len(L)):
            if L[element][0]==pseudo:
                ligne = element                 #Recuperation de la ligne dans la matrice a modifier

        M2 = f2.readlines() 


        for element in range(len(M2)):
            if M2[element]==livre:
                colonne = element           #Recupération de la colonne a modifier
            
        M3 = f3.readlines()

        L_M = []
        for i in M3:
            var = i.split(' ')
            var.pop(-1)
            L_M.append(var)
        
        for i in range(len(L_M)):
            for element in range(i):
                L_M[ligne][colonne]=str(note)   #Modification de la matrice

        Liste_Matrice = []
        for element in L_M:
            t=' '.join(element)
            Liste_Matrice.append(t)
        
        with open('Notation.txt',"w")as f:
            for element in Liste_Matrice:
                f.write(f"{element}\n") #réecriture de la matrice dans Notation.txt
                
        



