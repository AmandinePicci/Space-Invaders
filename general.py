# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:43:12 2021

@author: Amand
"""

from tkinter import Toplevel, Label, Button

import Objets

class General :
    
    def __init__(self, canne, root):
        
        self.canne=canne
        self.L=[]
        self.root=root
        
        
    def Level1 (self):
        for i in range(5)  :
            alien=Objets.Alien(self, i)
            self.L = self.L + [alien]
            
        vaisseau1=Objets.Vaisseau(self, self.root)
        self.canne.focus_set()
        self.canne.bind('<Key>', vaisseau1.Clavier )  #Permet au joueur de lier son clavier au programme
        
     
        
    def GameOver(self, root):
        """ Fonction permettant l'ouverture d'une nouvelle fenêtre tkinter pour signaler que le joueur a perdu"""
        
        GameOver= Toplevel(root)
        GameOver.geometry('800x300')
        labelTitre =Label(GameOver, text = "GAME OVER")
        labelRegles =Label(GameOver, text= "Vous avez perdu !!!! (Quel nul !)")
        buttonQuit = Button(GameOver, text = "Recommencer", command=lambda:[root.mainloop(),GameOver.destroy])    #Bouton permettant la destruction de la sous-fenêtre
    
        labelTitre.pack(pady=10)
        labelRegles.pack(pady=40)
        buttonQuit.pack(side='bottom', pady=10)
    
    def MortEnnemi (self, collision):
        for ennemi in self.L : 
            if ennemi.rectangle == collision[0]:
                self.canne.delete(ennemi.rectangle)
                self.L.remove(ennemi)
                ennemi.exist = False
                
    def MortVaisseau (self, ptsVie, root):
        if ptsVie >= 1 :
            ptsVie = ptsVie-1
            print("pts de vie", ptsVie)
            return(ptsVie)
        else :
            """"Il faut arrêter le jeu"""
            print("game over")
            root.destroy()
            self.GameOver(root)
    
            
            
        
        
        