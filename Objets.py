#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:36:25 2020

@author: amandine et sarah

TP 3 Jeu Space invaders __ Classes des objects principaux (vaisseau, alien et ennemi bonus)
 __ Janvier 2021 __ Amandine Piccinali et Sarah Le Corre

"""

# IMPORTATION DES BIBLIOTHEQUES     
from tkinter import PhotoImage
import random as rd

#IMPORTATION DES FICHIERS
import Projectiles as P 


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Alien: 
    '''Classe gérant les ennemis simples'''
    
    # INITIALISATION DES VARIABLES
    
    def __init__(self, general, id):         
        
        self.general=general
        self.canne = self.general.canne             #canvas
        
        
        self.image_ennemi = PhotoImage(file = "alien_PNG.png")  #création image de fond le l'alien
        
		# direction horizontale de l'alien (vitesse)
        self.dx = 1
		#direction verticale de l'alien (vitesse)
        self.dy = 0
        
        # position de l'alien
        self.Hx=25 +id*100
        self.Hy=5
        self.Bx=25 +id*100 +30
        self.By=35

		# création de l'alien avec l'image de fond
        self.rectangle = self.canne.create_image((self.Hx+self.Bx)/2, (self.Hy+self.By)/2, image = self.image_ennemi)
        
        self.exist=True

		#  appel de la méthode qui permet de faire bouger l'alien
        self.movement() 
        
        # appel de la méthode pour faire tirer l'alien
        self.randomTire()
        
        # #position de l'alien
        # self.pos=self.canne.coords(self.rectangle)
        
        
    # METHODES

    def descAlienD(self):
        '''Méthode permettant à l'alien de stopper sa descente et de repartir vers le bord gauche du canva'''

        self.dy=0       #La vitesse verticale de l'alien est annulée
        self.dx=-1      # On remet un déplacement horizontal à l'alien (de droite à gauche)
        
        
    def descAlienG(self):
        '''Méthode permettant à l'alien de stopper sa descente et de repartir vers le bord droit du canva'''
         
        self.dy=0       #La vitesse verticale de l'alien est annulée
        self.dx=1       # On remet un déplacement horizontal à l'alien (de gauche à droite)
        
	
    def movement(self):
        '''Méthode gérant les déplacements de l'alien'''
        
        # if self.canne.find_overlapping(self.canne.coords(self.rectangle)[0]-10,self.canne.coords(self.rectangle)[1]-10,self.canne.coords(self.rectangle)[0]+10,self.canne.coords(self.rectangle)[1]+10)!=(1,2):
        #         #self.exist=False
        #         print ("coucou")
        #         print(self.canne.find_overlapping(self.canne.coords(self.rectangle)[0]-10,self.canne.coords(self.rectangle)[1]-10,self.canne.coords(self.rectangle)[0]+10,self.canne.coords(self.rectangle)[1]+10)[2])
        #         self.exist=True
        # else:
        #     self.exist=True
        
        if self.exist==True :
    		# Bouge l'alien aux coordonnés x, y  grâce à la méthode move
            self.canne.move(self.rectangle, self.dx, self.dy) 
            
            # Appel la méthode movement après 10 ms pour continuer le mouvement
            self.canne.after(10, self.movement) 
            
            #Permet le retour de l'alien quand il touche les bords du canvas
            if self.canne.coords(self.rectangle)[0] >=885 :
                #Lorsque l'alien arrive sur le bord droit du Canva, sa vitesse horizontale est annulée et on lui met une vitesse verticale pour le faire descendre.
                self.dx=0
                self.dy=50
                self.canne.after(10, self.descAlienD)  # après 10 ms, on applique la méthode descAlienD, ce qui va stopper la descente de l'alien et le faire repartir du côté gauche 
            
  
            elif self.canne.coords(self.rectangle)[0]<=25:
                self.dx=0
                self.dy=50
                self.canne.after(10, self.descAlienG) # après 10 ms, on applique la méthode descAlienG, ce qui va stopper la descente de l'alien et le faire repartir du côté droit
                

    def tire(self):
        '''Méthode gérant le tir aléatoire de l'alien'''
        if self.exist ==True :
            P.ProjectileAlien(self.canne, self.canne.coords(self.rectangle)[0],  self.canne.coords(self.rectangle)[1])     #création du projectile et lancement en appelant la classe ProjectileAlien du fichier Projectiles
            self.canne.after(10,self.randomTire)       #appel de la méthode randomTire après 10 ms pour tirer au bout d'une durée aléatoire
            
        
    def randomTire(self):
        '''Méthode permettant le tire d'un projectile au bout d'une durée aléatoire entre 1 et 6 secondes'''
        
        tire = rd.randrange(1000,6000)      # Choisit un nombre aléatoire entre 1000 et 6000
        self.canne.after(tire, self.tire)   #appel de la méthode tire pour réitérer le tire
        
    def get (self):
        return(self.rectangle)
        
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
            
               
class EnnemiBonus:
    '''Classe gérant les ennemis bonus'''
    
    # INITIALISATION DES VARIABLES
    
    def __init__(self,canne):   
        self.canne = canne
        self.image_ennemiBonus = PhotoImage(file = "alienBonus.png")     #Création image de fond de l'ennemi Bonus
         
		# direction horizontale de l'ennemi Bonus
        self.dx = 3
		#direction verticale de l'ennemi Bonus
        self.dy = 2
        
        # position de l'ennemi Bonus
        self.Hx=400
        self.Hy=95
        self.Bx=self.Hx+90
        self.By=self.Hy+119
        
		# création de l'ennemi Bonus
        self.ennemiBonus = self.canne.create_image((self.Hx+self.Bx)/2, (self.Hy+self.By)/2, image = self.image_ennemiBonus)
        self.exist=True

		# méthode qui permet de faire bouger l'ennemi
        self.movement() 
        
        # méthode qui permet le tire de l'ennemi
        self.randomTire()
        
        
 # METHODES       
        
    def movement(self):
        '''Méthode gérant les déplacements de l'ennemi Bonus'''
        
#        if self.canne.find_overlapping(self.canne.coords(self.ennemiBonus)[0]-10,self.canne.coords(self.ennemiBonus)[1]-10,self.canne.coords(self.ennemiBonus)[0]+10,self.canne.coords(self.ennemiBonus)[1]+10)!=(1,2):
#                self.exist=False
#        else:
#            self.exist=True
            
            
        if self.exist==True :
    		# Bouge l'alien aux coordonnés x, y 
            self.canne.move(self.ennemiBonus, self.dx, self.dy) 
            # réitère la méthode pour continuer le mouvement  après 5ms
            self.canne.after(5, self.movement) 
            
            #Permet le retour de l'alien quand il touche les bords du canvas
            if self.canne.coords(self.ennemiBonus)[0] >=885 :
                #Lorsque l'alien arrive sur le bord droit du Canva, sa vitesse horizontale et verticale sont modifiées
                self.dx=-2
  
            elif self.canne.coords(self.ennemiBonus)[0]<=25:
                #Lorsque l'alien arrive sur le bord gauche du Canva, sa vitesse horizontale et verticale sont modifiées
                self.dx=2
                
            elif self.canne.coords(self.ennemiBonus)[1]<=25:
                #Lorsque l'alien arrive sur le bord haut du Canva, sa vitesse horizontale et verticale sont modifiées 
                
                self.dy=2
                
            elif self.canne.coords(self.ennemiBonus)[1]>=550:
                #Lorsque l'alien arrive sur le bord bas du Canva, sa vitesse horizontale et verticale sont modifiées
                
                self.dy=-2
                
  
        else:
            self.canne.delete(self.ennemiBonus)
            
            
        
    def tire(self):
        #'''Méthode gérant les tirs de l'ennemi bonus'''
        
         P.ProjectileEnnemiBonus(self.canne, self.canne.coords(self.ennemiBonus)[0],  self.canne.coords(self.ennemiBonus)[1])   #appel de la classe ProjectileEnnemiBonus dans le fichier Projectiles
         self.canne.after(10,self.randomTire)   #Appel de la méthode randomTire après 10 ms pour tirer au bout d'une durée aléatoire
        
        
    def randomTire(self):
        # '''Méthode permettant le tire d'un projectile au bout d'une durée aléatoire entre 1 et 3 secondes'''
        
        tire = rd.randrange(1000,3000) # Choisit un nombre aléatoire entre 1000 et 3000
        self.canne.after(tire, self.tire) #appel de la méthode tire pour réitérer le tire
        
        
        
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
            
class Vaisseau: 
    '''Classe gérant le vaisseau du joueur'''
 
# INITIALISATION DES VARIABLES
    
    def __init__(self, general):      
        
        self.general=general
        self.canne=self.general.canne
        #Position vaisseau
        self.Vax=430
        self.Vay=550
        
        self.image_vaisseau = PhotoImage(file = "vaisseau.png")     # Création de l'image de fond du vaisseau
		# création du vaisseau
        self.vaisseau =  self.canne.create_image((self.Vax+self.Vax+67)/2,(self.Vay+self.Vay+67)/2, image = self.image_vaisseau)

     
# METHODES 		
        
    def Clavier (self,event):
        '''Méthode gérant les évenement liés à l'appui de certaines touches du clavier : flèches pour les déplacements du vaisseau et 
        la barre espace pour le tire de projectiles'''
        
        touche=event.keysym
        
        #déplacement vers la droite
        if touche == 'Right':
            self.Vax = self.Vax +20
        
        #déplacement vers la gauche
        if touche == 'Left':
            self.Vax = self.Vax - 20
        
        #lancement projectile
        if touche =='space':
            P.ProjectileVaisseau(self.Vax, self.general)  # Appel de la classe ProjectileVaisseau du fichier Projectiles
            
        #arret du vaisseau sur les bords du canvas   
        if self.Vax>=850 :
            self.Vax=850
        elif self.Vax<0:
            self.Vax=10    
            
        #on dessine le vaisseau à sa nouvelle position
        self.canne.coords(self.vaisseau,(self.Vax+self.Vax+67)/2,(self.Vay+self.Vay+67)/2)
        