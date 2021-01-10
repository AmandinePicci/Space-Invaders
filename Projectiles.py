# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 14:52:18 2021

@author: Amand
"""

class ProjectileVaisseau :
    def __init__(self, canne, vax):
        
        self.canne = canne
        
        # direction horizontale du projectile
        self.dx = 0
		#direction verticale du projectile
        self.dy = -1
        
        # position du projectile
        self.Vax=vax+40
        
        #créé projectile
        self.cercle=self.canne.create_rectangle(self.Vax -5, 550, self.Vax +5,560, outline='black', fill="dark violet")
       
        #lance le projectile
        self.move()
        
        #existance du projectile
        self.exist=False
        
        
        
    def move(self):
        self.exist=True
        #Permet la suppression du projectile quand il sort du canevas
        if self.exist==True and self.canne.coords(self.cercle)[1] ==20 :
            self.canne.delete(self.cercle)
            self.exist=False
        else :
            # Bouge le projectile aux coordonnés x, y 
            self.canne.move(self.cercle, self.dx, self.dy) 
            # Changer la vitesse
            self.canne.after(2, self.move)
            
            #supprime le projectile si il touche qqn
            if self.exist==True and self.canne.find_overlapping(self.canne.coords(self.cercle)[0]-10,self.canne.coords(self.cercle)[1]-10,self.canne.coords(self.cercle)[0]+10,self.canne.coords(self.cercle)[1]+10) != (1,self.canne.find_overlapping(self.canne.coords(self.cercle)[0]-10,self.canne.coords(self.cercle)[1]-10,self.canne.coords(self.cercle)[0]+10,self.canne.coords(self.cercle)[1]+10)[1]) :
               self.canne.delete(self.cercle)
               self.exist=False
            
        # if self.canne.find_overlapping(self.canne.coords(self.cercle)[0]-10,self.canne.coords(self.cercle)[1]-10,self.canne.coords(self.cercle)[0]+10,self.canne.coords(self.cercle)[1]+10)[0]==1:
        #     #self.exist=False
        #     print ("coucou")
        #     print(self.canne.find_overlapping(self.canne.coords(self.rectangle)[0]-10,self.canne.coords(self.rectangle)[1]-10,self.canne.coords(self.rectangle)[0]+10,self.canne.coords(self.rectangle)[1]+10))
        #    self.exist=True
    
           
               
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            
            
class ProjectileAlien:
    
    def __init__(self, canne, Hx, Hy):
        
        self.canne = canne
        
        # direction horizontale du projectile
        self.dx = 0
		#direction verticale du projectile
        self.dy = 1
        
        # position du projectile
        self.Hx=Hx
        self.Hy=Hy
        
        #créé projectile
        self.cercle=self.canne.create_oval(self.Hx,self.Hy,self.Hx+10,self.Hy+10, outline='black', fill="lightseagreen")
       
        #lance le projectile
        self.move()
        
        
    def move(self):

        #Permet la suppression du projectile quand il sort du canevas
        if self.canne.coords(self.cercle)[1] ==580 :
            self.canne.delete(self.cercle)
        else :
            # Bouge le projectile aux coordonnés x, y 
            self.canne.move(self.cercle, self.dx, self.dy) 
            # Changer la vitesse
            self.canne.after(2, self.move)
            


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



class ProjectileEnnemiBonus:
    def __init__(self, canne, Hx, Hy):
        
        self.canne = canne
        
        # direction horizontale du projectile
        self.dx = 0
		#direction verticale du projectile
        self.dy = 2
        
        self.dx2=2
        self.dy2=2
        
        self.dx3=-2
        self.dy3=2
        
        # position du projectile
        self.Hx=Hx
        self.Hy=Hy
        
        #créé projectile
        self.cercle1=self.canne.create_oval(self.Hx,self.Hy,self.Hx+20,self.Hy+20, outline='white', fill="red")
        self.cercle2=self.canne.create_oval(self.Hx,self.Hy,self.Hx+20,self.Hy+20, outline='white', fill="red")
        self.cercle3=self.canne.create_oval(self.Hx,self.Hy,self.Hx+20,self.Hy+20, outline='white', fill="red")
       
        #lance le projectile
        self.move()
        self.move2()
        self.move3()
        
        
    def move(self): #gestion projectile1

        #Permet la suppression du projectile quand il sort du canevas
        if self.canne.coords(self.cercle1)[1] ==580 :
            self.canne.delete(self.cercle1)
        else :
            # Bouge le projectile aux coordonnés x, y 
            self.canne.move(self.cercle1, self.dx, self.dy) 
            # Changer la vitesse
            self.canne.after(2, self.move)
            
    def move2(self):#gestion projectile2
        
            
        if self.canne.coords(self.cercle2)[1] ==580 :
            self.canne.delete(self.cercle2)
        else :
            # Bouge le projectile aux coordonnés x, y 
            self.canne.move(self.cercle2, self.dx2, self.dy2) 
            # Changer la vitesse
            self.canne.after(2, self.move2)

    def move3(self): #gestion projectile3
                  
    
        if self.canne.coords(self.cercle3)[1] ==580 :
            self.canne.delete(self.cercle3)
        else :
            # Bouge le projectile aux coordonnés x, y 
            self.canne.move(self.cercle3, self.dx3, self.dy3) 
            # Changer la vitesse
            self.canne.after(2, self.move3)