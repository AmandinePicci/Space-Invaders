 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:26:13 2020
@author: amandine et sarah lecorre

TP 3 Jeu Space invaders __ Programme Principal __ Janvier 2021 __ Amandine Piccinali et Sarah Le Corre

TODO : 

    protections interactives
    projectiles alien bonus se suppriment
    Rendre projectiles alien et alien dangereux
"""

#IMPORTATION BIBLIOTHEQUES
from tkinter import Tk, Button, Canvas, Label, Menu, PhotoImage, NW, Toplevel
import tkinter.font as TkFont
#from Objets import EnnemiBonus
from protections import Protections1
from protections import Protections2
from general import General

#PP
fenetre = Tk()                                                                 #Création fenêtre graphique
fenetre.title ('Space Invaders')
fenetre.geometry ('1000x800+100+40')
 
#------------------------------------------------------------------------------------------------------ -------------------------
#Fonction ouverture sous-fenêtre 

def newFen():
    """ Fonction permettant l'ouverture d'une nouvelle fenêtre tkinter avec les règles inscrites à l'interieur"""
    
    newFen= Toplevel(fenetre)
    newFen.geometry('850x350')
    newFen.configure(bg='deep sky blue')
    fontStyle= TkFont.Font(family= "Lucida Grande", size=20)
    
    fontStyle2= TkFont.Font(family= "Lucida Grande", size=5)
    labelTitre =Label(newFen, text = "Règles du jeu", font=fontStyle, fg='blue', bg='deep sky blue')
    labelRegles =Label(newFen,font=fontStyle2, bg='deep sky blue', text= "Le but du jeu est de tirer sur les Aliens (en haut de l'écran) afin de les tuer, \n grâce à un vaisseau , avant que les Aliens ne vous tuent.\n Les Aliens ont également la possibilité de vous tirer dessus… \n Heureusement vous pouvez vous abriter derrière les ilots de protection.\n Déplacez-vous avec les flèches de votre clavier, et tirez grâce à la barre espace.\n\n Bonne chance et attention à l'ennememi mystère !")
    buttonQuit = Button(newFen,activebackground='blue', activeforeground='white', text = "Revenir au jeu", command=newFen.destroy)    #Bouton permettant la destruction de la sous-fenêtre

    labelTitre.pack(pady=10)
    labelRegles.pack(pady=40)
    buttonQuit.pack(side='bottom', pady=10)
  
    
    
    
def Lancement(nb):
    #Création d'un objet PhotoImage pour reconnaître les .git et .png   

        
        can1 = Canvas(fenetre, width =900 , height =600)                       #Création du canvas
        item=can1.create_image(0,0, anchor=NW, image=image1)                  #Création de l'image de fond du canvas
        
        can1.pack(side='top')
        
        gen=General(can1, fenetre)
        gen.Level1(nb,1)
        P=Protections1(can1)

        P.pack()    
        
        
        

    
def Lancement2(nb):
    #Création d'un objet PhotoImage pour reconnaître les .git et .png   

         
        can1 = Canvas(fenetre, width =900 , height =600)                       #Création du canvas
        item=can1.create_image(0,0, anchor=NW, image=image2)                  #Création de l'image de fond du canvas
        
        can1.pack(side='top')
        
        gen=General(can1, fenetre)
        gen.Level1(nb,2)
        P=Protections2(can1)

        P.pack()  
        
        
def Lancement3(nb):
    #Création d'un objet PhotoImage pour reconnaître les .git et .png   

        
        can1 = Canvas(fenetre, width =900 , height =600)                       #Création du canvas
        item=can1.create_image(0,0, anchor=NW, image=image3)                  #Création de l'image de fond du canvas
        
        can1.pack(side='top')
        
        gen=General(can1, fenetre)
        gen.Level1(nb,3)
    
#
#def Lancement():
#    gen=General(can1, fenetre)
#    gen.Level1()
#    P=Protections(can1)
    # P.pack()    #sait que c'est pas censé mettre pack mais affiche les blocs de protections sinon ça marche pas
    #ennemiBonus=EnnemiBonus(can1)
#-------------------------------------------------------------------------------------------------------------------------------
# Création de la barre menu comportant les options 'Quitter' et 'à propos'
    
menu1=Menu(fenetre)                                                            

menufichier2=Menu(menu1, tearoff=0) 
menufichier2.add_command(label="Règles du jeu", command=newFen)     # Appel de la fonction newFen pour ouvrir une nouvelle fenêtre comprenant les rêgles du jeu
menu1.add_cascade(label="A propos", menu=menufichier2)              

menufichier=Menu(menu1, tearoff=0) 
menufichier.add_command(label="Quitter", command=fenetre.destroy)   # Destruction de la fenêtre principale lorsque l'on appuie sur le bouton 'Quitter'
menu1.add_cascade(label="Quitter", menu=menufichier)

fenetre.config(menu=menu1)
#-------------------------------------------------------------------------------------------------------------------------------
image1=PhotoImage(file="sky.gif")
image2=PhotoImage(file="eau.png")
image3=PhotoImage(file="lave.png") 
#buttonStart = Button(fenetre, text="Nouvelle Partie", fg='red', command=Lancement)    #Bouton start permettant de commencer une nouvelle partie

buttonStart = Button(fenetre, text="Nouvelle Partie", fg='red',command= lambda:[Lancement(3)])    #Bouton start permettant de commencer une nouvelle partie
buttonStart.pack(side='top', pady=5)   


buttonLevel2 = Button(fenetre, text="Niveau 2", fg='red',command= lambda:[Lancement2(6)])    
buttonLevel3 = Button(fenetre, text="Niveau 3", fg='red',command= lambda:[Lancement3(9)])    
buttonLevel3.pack(side='bottom', pady=5)       
buttonLevel2.pack(side='bottom', pady=5) 

                                      
#-------------------------------------------------------------------------------------------------------------------------------
#image1=PhotoImage(file="sky.gif")                                     #Création d'un objet PhotoImage pour reconnaître les .git et .png          
#can1 = Canvas(fenetre, width =900 , height =600)                       #Création du canvas
#item=can1.create_image(0,0, anchor=NW, image=image1)                  #Création de l'image de fond du canvas
#can1.pack(side='top')


#-------------------------------------------------------------------------------------------------------------------------------
Label1 = Label(fenetre, text = 'Score :')                                      #Label affichant le score du joueur
Label1.pack(side='top', padx=5)
#-------------------------------------------------------------------------------------------------------------------------------
fenetre.mainloop()  #lance l'attente des évênements