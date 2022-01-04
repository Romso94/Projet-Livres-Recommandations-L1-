# Projet : Systeme de recommandation de livres  ( projet L1)
#Ce fichier sert à gérer les modifications dans le dépot de livre
from function_window_register import ListeLivres
import main

def Recup_Livre_Supp (Valeur):
    #Cette fonction permets de supprimer un livre donné par l'utilisateur dans le fichier books.txt
    #Entrée : Valeur:le titre du livre a supprimer ; le fichier books.txt
    #Sortie : le fichier books.txt sans le livre donné 
    
    Liste_Livre =ListeLivres()      #fonction du fichier function_window_register qui permet de recuperer la liste de tous les livres de books.txt

    for element in range(len(Liste_Livre)-1):
        if Liste_Livre[element]==Valeur:                    #Parcours de la liste des livres
            Liste_Livre.pop(element)                        #Suppression du livre grace à l'indice dans la liste
    with open('books.txt','w',encoding='utf-8') as f :
        for element in Liste_Livre:
            f.write(element + '\n')                        #Réécriture du fichier books.txt sans le livre donné

    
def Recup_Livre_Modif(Valeur,Valeur_Modif):             
    #Cette fonction permet de modifier le titre d'un livre du fichier books.txt
    #Entrée : books.txt ; Valeur:le titre du livre a modifier ; Valeur_Modif : le nouveau titre
    #Sortie : le fichier books.txt avec le titre (Valeur) modifier en (Valeur_Modif)
    
    Liste_Livre = ListeLivres()                      #fonction du fichier function_window_register qui permet de recuperer la liste de tous les livres de books.txt
    for element in range(len(Liste_Livre)-1):       #Verifie que le titre n'existe pas deja
        if Liste_Livre[element]==Valeur_Modif:
            return()
        
        if Liste_Livre[element]==Valeur:
            Liste_Livre.pop(element)            #Supprime le titre 
            Liste_Livre.insert(element,Valeur_Modif)    #Insert à la place de l'ancien titre le nouveau

    with open('books.txt','w',encoding='utf-8') as f :
        for element in Liste_Livre:
            f.write(element + '\n')             #Réecriture dans books.txt






def Ajouter_Livre_Txt(Title):
    #Cette fonction permet d'ajouter un livre au fichier books.txt
    #Entrée : books.txt, Title : Nouveau titre
    #Sortie : books.txt avec le nouveau livre

    Liste_Livre = ListeLivres()      #fonction du fichier function_window_register qui permet de recuperer la liste de tous les livres de books.txt
    for element in range(len(Liste_Livre)-1):    #Verifie que le titre n'existe pas deja
        if Liste_Livre[element]==Title:
            return()
    
    with open('books.txt','a',encoding='utf-8') as f:
        f.write(Title)          #Ajout dans books.txt
