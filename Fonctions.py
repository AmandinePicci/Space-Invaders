#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:36:25 2020

@author: amandine et sarah
"""

class Alien: 
    def __init__(self, canne): 
        self.canne = canne 

		# direction horizontale de l'alien
        self.dx = 1
		#direction verticale de l'alien
        self.dy = 0

		# crée l'alien
        self.rectangle = self.canne.create_rectangle(5, 5, 25, 25, fill = "SpringGreen2") 
        

		# méthode qui permet de faire bouger l'alien
        self.movement() 
        
	
    def movement(self):
        # if self.x >= 100 :
        #     self.dx=-1
        # elif self.x<=0:
        #     self.dx=1
		# Bouge l'alien aux coordonnés x, y 
        self.canne.move(self.rectangle, self.dx, self.dy) 
        # Changer la vitesse
        self.canne.after(10, self.movement) 
        if self.canne.coords(self.rectangle)[2] >=1000 :
            self.dx=-1
        elif self.canne.coords(self.rectangle)[2]<=25:
            self.dx=1
                                 
	
    # def retour(self):
    #     if self.x >= 100 :
    #         self.dx=-1
    #     elif self.x<=0:
    #         self.dx=1
            
            
    #	# for motion in negative x direction 
    #	def left(self): 
    #		self.dx = -5
    #		self.dy = 0
    #	
    #	# for motion in positive x direction 
    #	def right(self, event): 
    #		print(event.keysym) 
    #		self.dx = 5
    #		self.dy = 0