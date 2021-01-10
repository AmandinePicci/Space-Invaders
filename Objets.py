#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:36:25 2020

@author: amandine et sarah

TODO :
Lorsque le projectile émis par le vaisseau entre en collision
avec l’Alien, les deux objets doivent disparaître !
"""
from tkinter import PhotoImage
import random as rd
import Projectiles as P 

class Alien: 
    def __init__(self, canne,): 
        self.canne = canne 
        
        self.image_ennemi = PhotoImage(file = "alien_PNG.png")
        
		# direction horizontale de l'alien
        self.dx = 2
		#direction verticale de l'alien
        self.dy = 0
        
        # position de l'alien
        self.Hx=5
        self.Hy=5
        self.Bx=35
        self.By=35

		# crée l'alien
        self.rectangle = self.canne.create_image((self.Hx+self.Bx)/2, (self.Hy+self.By)/2, image = self.image_ennemi)
        self.exist=True

		# méthode qui permet de faire bouger l'alien
        self.movement() 
        
        #méthode pour faire tirer l'alien
        self.randomTire()

    def descAlienD(self):
        #met la vitesse en ordonnée de l'alien à 0, et celle en abscisse à -1 (l'alien se déplace de la droite vers la gauche)
        self.dy=0       
        self.dx=-2
        
    def descAlienG(self):
         #met la vitesse en ordonnée de l'alien à 0, et celle en abscisse à 1 (l'alien se déplace de la gauche vers la droite)
        self.dy=0
        self.dx=2
	
    def movement(self):
        
        # if self.canne.find_overlapping(self.canne.coords(self.rectangle)[0]-10,self.canne.coords(self.rectangle)[1]-10,self.canne.coords(self.rectangle)[0]+10,self.canne.coords(self.rectangle)[1]+10)!=(1,2):
        #         #self.exist=False
        #         print ("coucou")
        #         print(self.canne.find_overlapping(self.canne.coords(self.rectangle)[0]-10,self.canne.coords(self.rectangle)[1]-10,self.canne.coords(self.rectangle)[0]+10,self.canne.coords(self.rectangle)[1]+10)[2])
        #         self.exist=True
        # else:
        #     self.exist=True
              
          
    
        

                
        if self.exist==True :
    		# Bouge l'alien aux coordonnés x, y 
            self.canne.move(self.rectangle, self.dx, self.dy) 
            
            # Changer la vitesse
            self.canne.after(10, self.movement) 
            
            #Permet le retour de l'alien quand il touche les bords du canvas
            if self.canne.coords(self.rectangle)[0] >=885 :
                #Lorsque l'alien arrive sur le bord droit du Canva, sa vitesse horizontale est annulée et on lui met une vitesse verticale pour le faire descendre.
                self.dx=0
                self.dy=10
                self.canne.after(10, self.descAlienD)  # après 10 ms, on applique la fonction descAlienD, ce qui va stopper la descente de l'alien et le faire repartir du côté gauche 
            
  
            elif self.canne.coords(self.rectangle)[0]<=25:
                self.dx=0
                self.dy=10
                self.canne.after(10, self.descAlienG) # après 10 ms, on applique la fonction descAlienG, ce qui va stopper la descente de l'alien et le faire repartir du côté droit
            
        else:
            self.canne.delete(self.rectangle)
            
            
    def tire(self):
         P.ProjectileAlien(self.canne, self.canne.coords(self.rectangle)[0],  self.canne.coords(self.rectangle)[1])
         self.canne.after(10,self.randomTire)
        
        
    def randomTire(self):
        
        tire = rd.randrange(1000,6000) #Tire  aléatoirement toutes les 1 à 6 secondes
        self.canne.after(tire, self.tire)
        
        
        
        
        
#    def ClavierA (self,event):
#        touche=event.keysym
#        
#        if touche =='space':
#            projectile=ProjectileAlien(self.canne,  self.canne.coords(self.rectangle)[0],  self.canne.coords(self.rectangle)[1])
#        
#        
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
            
               
class EnnemiBonus:
    def __init__(self,canne):
        self.canne = canne
        self.image_ennemiBonus = PhotoImage(file = "alienBonus.png")
         
		# direction horizontale de l'ennemi Bonus
        self.dx = 3
		#direction verticale de l'ennemi Bonus
        self.dy = 2
        
        # position de l'ennemiBonus
        self.Hx=400
        self.Hy=95
        self.Bx=self.Hx+90
        self.By=self.Hy+119
        
		# crée l'ennemi Bonus
        self.ennemiBonus = self.canne.create_image((self.Hx+self.Bx)/2, (self.Hy+self.By)/2, image = self.image_ennemiBonus)#create_rectangle(self.Hx, self.Hy, self.Bx, self.By, fill = "SpringGreen2") 
        self.exist=True

		# méthode qui permet de faire bouger l'alien
        self.movement() 
        
        self.randomTire()
        
    def movement(self):
        
#        if self.canne.find_overlapping(self.canne.coords(self.ennemiBonus)[0]-10,self.canne.coords(self.ennemiBonus)[1]-10,self.canne.coords(self.ennemiBonus)[0]+10,self.canne.coords(self.ennemiBonus)[1]+10)!=(1,2):
#                self.exist=False
#        else:
#            self.exist=True
            
            
        # L=[-2,2,-1,1,-3,3] 
        if self.exist==True :
    		# Bouge l'alien aux coordonnés x, y 
            self.canne.move(self.ennemiBonus, self.dx, self.dy) 
            # Changer la vitesse
            self.canne.after(5, self.movement) 
            
            #Permet le retour de l'alien quand il touche les bords du canvas
            if self.canne.coords(self.ennemiBonus)[0] >=885 :
                #Lorsque l'alien arrive sur le bord droit du Canva, sa vitesse horizontale et verticale sont modifiées aléatoirement
                self.dx=-2
                # self.dy=-rd.choice(L)
              
  
            elif self.canne.coords(self.ennemiBonus)[0]<=25:
                #Lorsque l'alien arrive sur le bord gauche du Canva, sa vitesse horizontale et verticale sont modifiées aléatoirement
                self.dx=2
                #self.dy=rd.choice(L)
             
            elif self.canne.coords(self.ennemiBonus)[1]<=25:
                #Lorsque l'alien arrive sur le bord haut du Canva, sa vitesse horizontale et verticale sont modifiées aléatoirement
                # self.dx=rd.choice(L)
                self.dy=2
                
            elif self.canne.coords(self.ennemiBonus)[1]>=550:
                #Lorsque l'alien arrive sur le bord bas du Canva, sa vitesse horizontale et verticale sont modifiées aléatoirement
                # self.dx=rd.choice(L)
                self.dy=-2
                
  
        else:
            self.canne.delete(self.ennemiBonus)
            
        
    def descAlienD(self):
        #met la vitesse en ordonnée de l'alien à 0, et celle en abscisse à -1 (l'alien se déplace de la droite vers la gauche)
        self.dy=0       
        self.dx=-2
        
    def descAlienG(self):
         #met la vitesse en ordonnée de l'alien à 0, et celle en abscisse à 1 (l'alien se déplace de la gauche vers la droite)
        self.dy=0
        self.dx=2
        
        
    def tire(self):
         P.ProjectileEnnemiBonus(self.canne, self.canne.coords(self.ennemiBonus)[0],  self.canne.coords(self.ennemiBonus)[1])
         self.canne.after(10,self.randomTire)
        
        
    def randomTire(self):
        
        tire = rd.randrange(1000,6000) #Tire  aléatoirement toutes les 1 à 6 secondes
        self.canne.after(tire, self.tire)
        
        
        
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
            
class Vaisseau: 
    def __init__(self, canne):
        self.canne = canne
        
        #Position vaisseau
        self.Vax=430
        self.Vay=550
        
        self.image_vaisseau = PhotoImage(file = "vaisseau.png")
		# crée le vaisseau
        self.vaisseau =  self.canne.create_image((self.Vax+self.Vax+67)/2,(self.Vay+self.Vay+67)/2, image = self.image_vaisseau)#"self.canne.create_rectangle(self.Vax, 550, self.Vax +40, 595 , fill = "RoyalBlue1")
        		
        
    def Clavier (self,event):
        touche=event.keysym
        
        #déplacement vers la droite
        if touche == 'Right':
            self.Vax = self.Vax +20
        
        #déplacement vers la gauche
        if touche == 'Left':
            self.Vax = self.Vax - 20
        
        #lancement projectile
        if touche =='space':
            P.ProjectileVaisseau(self.canne, self.Vax) 
            
        #arret du vaisseau sur les bords du canvas   
        if self.Vax>=850 :
            self.Vax=850
        elif self.Vax<0:
            self.Vax=10    
            
        #on dessine le vaisseau à sa nouvelle position
        self.canne.coords(self.vaisseau,(self.Vax+self.Vax+67)/2,(self.Vay+self.Vay+67)/2)
        

        
    

