 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:26:13 2020
@author: amandine et sarah lecorre

Space invaders

TODO : 
Lorsque le projectile émis par le vaisseau entre en collision
avec l’Alien, les deux objets doivent disparaître ! 
"""

#IMPORTATION BIBLIOTHEQUES
from tkinter import Tk, Button, Canvas, Label, Menu, PhotoImage, NW, Toplevel
from Objets import Alien, Vaisseau, EnnemiBonus

#PP
fenetre = Tk()                                                                 #Création fenêtre graphique
fenetre.title ('Space Invaders')
fenetre.geometry ('1000x800+100+40')
 
#-------------------------------------------------------------------------------------------------------------------------------
#Fonction ouverture nouvelle fenêtre avec les règles à l'interieur

def newFen():
    newFen= Toplevel(fenetre)
    newFen.geometry('800x300')
    labelTitre =Label(newFen, text = "Règles du jeu")
    labelRegles =Label(newFen, text= "Le but du jeu est de tirer sur les Aliens (en haut de l'écran) afin de les tuer, grâce à un vaisseau , avant que les Aliens ne vous tuent.\n Les Aliens ont également la possibilité de vous tirer dessus… Heureusement vous pouvez vous abriter derrière les ilots de protection.\n Déplacez-vous avec les flèches de votre clavier, et tirez grâce à la barre espace.\n\n Bonne chance et attention à l'ennememi mystère !")
    buttonQuit = Button(newFen, text = "Revenir au jeu", command=newFen.destroy)

    labelTitre.pack(pady=10)
    labelRegles.pack(pady=40)
    buttonQuit.pack(side='bottom', pady=10)
    

#-------------------------------------------------------------------------------------------------------------------------------
menu1=Menu(fenetre)                                                            #Menu

menufichier2=Menu(menu1, tearoff=0) 
menufichier2.add_command(label="Règles du jeu", command=newFen)
menu1.add_cascade(label="A propos", menu=menufichier2)

menufichier=Menu(menu1, tearoff=0) 
menufichier.add_command(label="Quitter", command=fenetre.destroy)
menu1.add_cascade(label="Quitter", menu=menufichier)

fenetre.config(menu=menu1)
#-------------------------------------------------------------------------------------------------------------------------------
buttonStart = Button(fenetre, text="Nouvelle Partie", fg='red') #command=)     #Bouton start
buttonStart.pack(side='top', pady=5)                                                                 
#-------------------------------------------------------------------------------------------------------------------------------
image1=PhotoImage(file="sky.gif")
can1 = Canvas(fenetre, width =900, height =600)                                #Création du canvas
item=can1.create_image(0,0, anchor=NW, image=image1)
can1.pack(side='top')
#-------------------------------------------------------------------------------------------------------------------------------
Label1 = Label(fenetre, text = 'Score :')                                      #Permet d'afficher le score
Label1.pack(side='top', padx=5)
#-------------------------------------------------------------------------------------------------------------------------------

alien1=Alien(can1) 
vaisseau1=Vaisseau(can1)
ennemiBonus=EnnemiBonus(can1)
can1.focus_set()
can1.bind('<Key>', vaisseau1.Clavier )
  
#-------------------------------------------------------------------------------------------------------------------------------
fenetre.mainloop()  