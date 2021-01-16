# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:43:12 2021

@author: Amand


'''TP 3 Jeu Space invaders __ Classe des projections contre les ennemis
 __ Janvier 2021 __ Amandine Piccinali et Sarah Le Corre'''
"""

from tkinter import PhotoImage, Toplevel, Label, Button
import tkinter.font as TkFont
#from Objets import EnnemiBonus

import random as rd

import Objets


class General :
    
    def __init__(self, canne, root):
        
        self.canne=canne
        self.L=[]
        self.root=root
        
        
        self.image_vie = PhotoImage(file = "vie.png")  #création image de fond le l'alien
           # position des coeurs de vie
        self.Hx=870
        self.Hy=5
        self.Bx=890
        self.By=25

		# création de l'alien avec l'image de fond
        self.vie0 = self.canne.create_image((self.Hx+self.Bx)/2, (self.Hy+self.By)/2, image = self.image_vie)
        self.vie1 = self.canne.create_image(((self.Hx+self.Bx)/2)-30, (self.Hy+self.By)/2, image = self.image_vie)
        self.vie2 = self.canne.create_image(((self.Hx+self.Bx)/2)-60, (self.Hy+self.By)/2, image = self.image_vie)
        self.LVies = [self.vie0, self.vie1, self.vie2]
    
        #Existance de l'ennemi bonus necessaire ici pour savoir si on peut le supprimer ou pas
        self.EnnemiBonusExist=False
        
        #Création du vaisseau
        self.vaisseau1=Objets.Vaisseau(self, self.root)
        
        # Vie du vaisseau
        self.ptsVie=3
    
    
    def Level1 (self,nb,niv):
        
        #blocProtection=protections.Protections(self.canne)
      
        for i in range(nb)  :
            alien=Objets.Alien(self, i,niv, self.root)
            self.L = self.L + [alien]
            
        vaisseau1=self.vaisseau1
      
        self.canne.focus_set()
        self.canne.bind('<Key>', vaisseau1.Clavier )  #Permet au joueur de lier son clavier au programme
        self.randomApp()
    
    
    def level2(self,nb,niv):
        
        for i in range(nb)  :
            alien=Objets.Alien(self, i,2, self.root)
            self.L = self.L + [alien]
            
        vaisseau1=self.vaisseau1
        
        self.canne.focus_set()
        self.canne.bind('<Key>', vaisseau1.Clavier )  #Permet au joueur de lier son clavier au programme
        self.randomApp()
        
    def level3(self,nb,niv):
        
        for i in range(nb)  :
            
            alien=Objets.Alien(self, i, 3, self.root)
            self.L = self.L + [alien]
                
            vaisseau1=self.vaisseau1
        
        self.canne.focus_set()
        self.canne.bind('<Key>', vaisseau1.Clavier )  #Permet au joueur de lier son clavier au programme
        self.randomApp()
    
    
    def randomApp(self):
        app= rd.randrange(5000,30000)
        self.canne.after(app,self.appEnnBon)
    
        
    def appEnnBon(self):
        self.EnnemiBonus=Objets.EnnemiBonus(self)
        self.EnnemiBonusExist=True
        
 
    def MortEnnemi (self, collision):
        for ennemi in self.L : 
            if ennemi.rectangle == collision[0]:
                self.canne.delete(ennemi.rectangle)
                self.L.remove(ennemi)
                ennemi.exist = False
        
            elif self.EnnemiBonusExist==True and self.EnnemiBonus.exist==True and self.EnnemiBonus.ennemiBonus==collision[0] :
                self.EnnemiBonus.exist=False
                self.canne.delete(self.EnnemiBonus.ennemiBonus)
        
                
                
        #VICTOIRE LORSQUE TOUS LES ALIENS SONT MORTS

        if len(self.L)==0:
            
             FenKO= Toplevel(self.root)
             FenKO.geometry('900x600')
             FenKO.configure(bg='')
            
             fontStyle = TkFont.Font(family="Lucida Grande", size=20)
             fontStyle2= TkFont.Font(family="Lucida Grande", size=12)
             labelTitre =Label(FenKO, text = "BRAVO QUELLE VICTOIRE !", font= fontStyle, fg = 'spring green', bg= 'black')
             labelKO =Label(FenKO, text= "Vous n'êtes pas si mauvais finalement...", font= fontStyle2, bg='black', fg= 'spring green')
          
             buttonRetry = Button(FenKO, activebackground='spring green',activeforeground='black',  text = "Niveau suivant", command=lambda:[FenKO.destroy(), self.retry()])    #Bouton permettant la destruction de la sous-fenêtre
             buttonQuitter = Button(FenKO,activebackground='spring green', activeforeground='black', text = "Quitter le jeu", command=self.root.destroy)
            
#            buttonQuitter = Button(FenKO, text = "Quitter le jeu", command=self.root.destroy)
            
            
             labelTitre.pack(side='top',pady=80)
             labelKO.pack(side='top',pady=10)
            
             buttonQuitter.pack(side='bottom', pady=10)
             buttonRetry.pack(side='bottom', pady=10)
                      
        
    def retry(self):
        self.canne.destroy()
#        for i in self.L:
#            self.canne.delete(self.L[i])
#            i=i+1
    
                
    def MortVaisseau (self, collision, root):
        
        if self.vaisseau1.vaisseau==collision[0]:
            if type(self.ptsVie)==int and self.ptsVie >= 1 :
                self.ptsVie = self.ptsVie-1
                self.canne.delete(self.LVies[self.ptsVie])   # Suppression du coeur de vie
               
            
            else :
                """"Il faut arrêter le jeu"""
                print("Game over")
                FenKO= Toplevel(self.root)
                FenKO.geometry('900x600')
                FenKO.configure(bg='black')
                
                fontStyle = TkFont.Font(family="Lucida Grande", size=40)
                fontStyle2= TkFont.Font(family="Lucida Grande", size=20)
                labelTitre =Label(FenKO, text = "GAME OVER", font= fontStyle, fg = 'blue', cursor= 'pirate', bg= 'black')
                labelKO =Label(FenKO, text= "KO c'est KO", font= fontStyle2, bg='black', fg= 'blue')
    #          
                buttonRetry = Button(FenKO, activebackground='blue',activeforeground='white',  text = "Rejouer", command=lambda:[FenKO.destroy(), self.retry()])    #Bouton permettant la destruction de la sous-fenêtre
                buttonQuitter = Button(FenKO,activebackground='blue', activeforeground='white', text = "Quitter le jeu", command=self.root.destroy)
                
    #            buttonQuitter = Button(FenKO, text = "Quitter le jeu", command=self.root.destroy)
                
                
                labelTitre.pack(side='top',pady=80)
                labelKO.pack(side='top',pady=10)
                
                buttonQuitter.pack(side='bottom', pady=10)
                buttonRetry.pack(side='bottom', pady=10)
        # elif 
                
            