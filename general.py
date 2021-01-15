# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:43:12 2021

@author: Amand
"""

from tkinter import PhotoImage, Toplevel, Label, Button

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
        
    def Level1 (self):
        #blocProtection=protections.Protections(self.canne)
        for i in range(5)  :
            alien=Objets.Alien(self, i)
            self.L = self.L + [alien]
            
        vaisseau1=Objets.Vaisseau(self, self.root)
       

        self.canne.focus_set()
        self.canne.bind('<Key>', vaisseau1.Clavier )  #Permet au joueur de lier son clavier au programme

 
    def MortEnnemi (self, collision):
        for ennemi in self.L : 
            if ennemi.rectangle == collision[0]:
                self.canne.delete(ennemi.rectangle)
                self.L.remove(ennemi)
                ennemi.exist = False
              
        
            
        
    def retry(self):
        
        for i in self.L:
            self.canne.delete(self.L[i])
            i=i+1
    
                
    def MortVaisseau (self, ptsVie, root):
        
        if type(ptsVie)==int and ptsVie >= 1 :
            ptsVie = ptsVie-1
       
            self.canne.delete(self.LVies[ptsVie])   # Suppression du coeur de vie
            return(ptsVie)
        else :
            """"Il faut arrêter le jeu"""
            print("Game over")
            FenKO= Toplevel(self.root)
            FenKO.geometry('900x600')
            labelTitre =Label(FenKO, text = "KO")
            labelRegles =Label(FenKO, text= "ko c est ko")
            buttonRetry = Button(FenKO, text = "Rejouer", command=lambda:[FenKO.destroy, self.retry])    #Bouton permettant la destruction de la sous-fenêtre
            buttonQuitter = Button(FenKO, text = "Quitter le jeu", command=self.root.destroy)
            
            
            labelTitre.pack(pady=10)
            labelRegles.pack(pady=40)
            buttonRetry.pack(side='bottom', pady=10)
            buttonQuitter.pack(side='bottom', pady=10)
            
        
            
    
            
            
        
        
        