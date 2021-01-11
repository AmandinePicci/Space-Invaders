# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:39:35 2021

@author: sarah
"""


'''TP 3 Jeu Space invaders __ Classe des projections contre les ennemis
 __ Janvier 2021 __ Amandine Piccinali et Sarah Le Corre'''
 

# IMPORTATION DES BIBLIOTHEQUES     
from tkinter import PhotoImage


class Protections:
    
    '''Classe gérant les boucliers de protection placés au dessus du vaisseau'''
      # INITIALISATION DES VARIABLES
    
    def __init__(self, canne):
        
        self.canne = canne              #canvas
        
        self.image_bloc = PhotoImage(file = "bloc1.png")  #création image de fond d'un des blocs de protection
		
        
        # position du bloc
        self.Hx=150
        self.Hy=510
        self.Bx=170
        self.By=530

		# création protection ligne 1
        i=0
        while i<7:
            self.bloc = self.canne.create_image(((self.Hx+20*i)+(self.Bx+20*i))/2, (self.Hy+self.By)/2, image = self.image_bloc)
            i=i+1
        i=0    
        while i<7:
            self.bloc = self.canne.create_image(((self.Hx+250+20*i)+(self.Bx+250+20*i))/2, (self.Hy+self.By)/2, image = self.image_bloc)
            i=i+1
        i=0    
        while i<7:
            self.bloc = self.canne.create_image(((self.Hx+490+20*i)+(self.Bx+490+20*i))/2, (self.Hy+self.By)/2, image = self.image_bloc)
            i=i+1
     
        # création protection ligne 2
        
        i=0
        while i<4:
            self.bloc = self.canne.create_image(((self.Hx+30+20*i)+(self.Bx+30+20*i))/2, ((self.Hy-20)+(self.By-20))/2, image = self.image_bloc)
            i=i+1
        i=0    
        while i<4:
            self.bloc = self.canne.create_image(((self.Hx+250+30+20*i)+(self.Bx+250+30+20*i))/2, ((self.Hy-20)+(self.By-20))/2, image = self.image_bloc)
            i=i+1
        i=0    
        while i<4:
            self.bloc = self.canne.create_image(((self.Hx+490+30+20*i)+(self.Bx+490+30+20*i))/2, ((self.Hy-20)+(self.By-20))/2, image = self.image_bloc)
            i=i+1
     