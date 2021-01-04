#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:36:25 2020

@author: amandine et sarah

TODO :
Lorsque le projectile émis par le vaisseau entre en collision
avec l’Alien, les deux objets doivent disparaître !
"""

class Alien: 
    def __init__(self, canne): 
        self.canne = canne 

		# direction horizontale de l'alien
        self.dx = 1
		#direction verticale de l'alien
        self.dy = 0
        
        # position de l'alien
        self.Hx=5
        self.Hy=5
        self.Bx=25
        self.By=25

		# crée l'alien
        self.rectangle = self.canne.create_rectangle(self.Hx, self.Hy, self.Bx, self.By, fill = "SpringGreen2") 
        self.exist=True

		# méthode qui permet de faire bouger l'alien
        self.movement() 
        
	
    def movement(self):
        
        if self.canne.find_overlapping(self.canne.coords(self.rectangle)[0],self.canne.coords(self.rectangle)[1],self.canne.coords(self.rectangle)[2],self.canne.coords(self.rectangle)[3])!=(1,2):
                self.exist=False
        else:
            self.exist=True
            
        if self.exist==True :
    		# Bouge l'alien aux coordonnés x, y 
            self.canne.move(self.rectangle, self.dx, self.dy) 
            # Changer la vitesse
            self.canne.after(5, self.movement) 
            #Permet le retour de l'alien quand il touche les bords du canvas
            if self.canne.coords(self.rectangle)[2] >=895 :
                self.dx=-1
            elif self.canne.coords(self.rectangle)[2]<=25:
                self.dx=1
                
        else:
            self.canne.delete(self.rectangle)
        
            
         
            
            
class Vaisseau: 
    def __init__(self, canne):
        self.canne = canne
        
        #Position vaisseau
        self.Vax=10
        
		# crée le vaisseau
        self.rectangle = self.canne.create_rectangle(self.Vax, 550, self.Vax +40, 595 , fill = "RoyalBlue1")
        		
        
    def Clavier (self,event):
        touche=event.keysym
        
        #déplacement vers la droite
        if touche == 'Right':
            self.Vax = self.Vax +20
        
        #déplacement vers la gauche
        if touche == 'Left':
            self.Vax = self.Vax - 20
            
        if touche =='space':
            projectile=Projectile(self.canne, self.Vax)
            
        if self.Vax>=850 :
            self.Vax=850
        elif self.Vax<0:
            self.Vax=10    
            
        #on dessine le vaisseau à sa nouvelle position
        self.canne.coords(self.rectangle,self.Vax, 550, self.Vax +40, 595)
    

class Projectile :
    def __init__(self, canne, vax):
        
        self.canne = canne
        
        # direction horizontale du projectile
        self.dx = 0
		#direction verticale du projectile
        self.dy = -1
        
        # position du projectile
        self.Vax=vax+20
        
        #créé projectile
        self.cercle=self.canne.create_oval(self.Vax -5, 550, self.Vax +5,560, outline='black', fill="dark violet")
       
        #lance le projectile
        self.move()
        
        
    def move(self):

        #Permet la suppression du projectile quand il sort du canevas
        if self.canne.coords(self.cercle)[1] ==20 :
            self.canne.delete(self.cercle)
        else :
            # Bouge le projectile aux coordonnés x, y 
            self.canne.move(self.cercle, self.dx, self.dy) 
            # Changer la vitesse
            self.canne.after(2, self.move)

        