# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:43:12 2021

@author: Amand
"""

import Objets

class General :
    
    def __init__(self, canne):
        
        self.canne=canne
        self.L=[]
        
    def Level1 (self):

        for i in range(5)  :
            alien=Objets.Alien(self, i)
            self.L = self.L + [alien]
            
        vaisseau1=Objets.Vaisseau(self)
        self.canne.focus_set()
        self.canne.bind('<Key>', vaisseau1.Clavier )  #Permet au joueur de lier son clavier au programme
        
        
    def MortEnnemi (self, collision):
        for ennemi in self.L : 
            if ennemi.rectangle == collision[0]:
                self.canne.delete(ennemi.rectangle)
                self.L.remove(ennemi)
                ennemi.exist = False