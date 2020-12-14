#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:26:13 2020
@author: amandine et sarah lecorre

Space invaders

TODO : 
 
Insérer un vaisseau (une image ou une forme simple) vers le bas de l’image et permettre au joueur de
déplacer ce vaisseau avec les touches gauche et droite. 
"""

#IMPORTATION BIBLIOTHEQUES
from tkinter import Tk, Button, Canvas, Label, Menu
from Fonctions import Alien, Vaisseau

#Fonctions tests


#PP
fenetre = Tk()                                                                 #Création fenêtre graphique
fenetre.title ('Space Invaders')
fenetre.geometry ('1000x800+100+40')

#-------------------------------------------------------------------------------------------------------------------------------
menu1=Menu(fenetre)                                                            #Menu A RAJOUTER COMMANDE POUR A PROPOS !!!!!!!

menufichier2=Menu(menu1, tearoff=0) 
menufichier2.add_command(label="A propos")
menu1.add_cascade(label="A propos", menu=menufichier2)

menufichier=Menu(menu1, tearoff=0) 
menufichier.add_command(label="Quitter", command=fenetre.destroy)
menu1.add_cascade(label="Quitter", menu=menufichier)

fenetre.config(menu=menu1)
#-------------------------------------------------------------------------------------------------------------------------------
buttonStart = Button(fenetre, text="Nouvelle Partie", fg='red') #command=)     #Bouton start
buttonStart.pack(side='top', pady=5)                                                                 
#-------------------------------------------------------------------------------------------------------------------------------
can1 = Canvas(fenetre, width =1000, height =600, bg ='black')                   #Création du canvas
can1.pack(side='top')
#-------------------------------------------------------------------------------------------------------------------------------
Label1 = Label(fenetre, text = 'Score :')                                #Permet d'afficher le score
Label1.pack(side='top', padx=5)
#-------------------------------------------------------------------------------------------------------------------------------
#rectangle = can1.create_rectangle(5, 5, 25, 25, fill = "SpringGreen2") 
#can1.move(rectangle, 1, 0) 
#can1.after(10, movement) 

alien1=Alien(can1)
vaisseau1=Vaisseau(can1)
	

#-------------------------------------------------------------------------------------------------------------------------------
fenetre.mainloop()  