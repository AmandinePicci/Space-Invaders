# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 14:52:18 2021

@author: Amand
"""
'''TP 3 Jeu Space invaders __ Classes des projectiles (du vaisseau, de l'alien et de l'ennemi bonus)
 __ Janvier 2021 __ Amandine Piccinali et Sarah Le Corre'''
 


class ProjectileVaisseau :
    '''Classe gérant les projectiles lancés par le joueur'''
    
# INITIALISATION DES VARIABLES
    
    def __init__(self, vax, general):
        
        self.general = general
        self.canne = self.general.canne         #canvas
        
        # direction horizontale du projectile
        self.dx = 0
		#direction verticale du projectile
        self.dy = -10
        
        # position du projectile
        self.Vax=vax+40
        
        #création projectile
        self.cercle=self.canne.create_rectangle(self.Vax -5, 550, self.Vax +5,560, outline='black', fill="dark violet")
       
        #lance le projectile
        self.move()
        
        
# AUTRES METHODES
    
        
    def move(self):
        ''' Méthodes gérant le déplacement du projectile du vaisseau'''
        exist=True
        
        #supprime le projectile si il touche quelqu'un et supprime l'alien du même coup
        self.collision = self.canne.find_overlapping(self.canne.coords(self.cercle)[0]-10,self.canne.coords(self.cercle)[1]-10,self.canne.coords(self.cercle)[0]+10,self.canne.coords(self.cercle)[1]+10)
        self.collision = self.collision[1:len(self.collision)-1]
        if  len(self.collision) > 0:
            """ Donc on a une collision """
            """ Envoyer l'info à général """
            self.general.MortEnnemi(self.collision)
            exist=False
            
            
        #Permet la suppression du projectile quand il sort du canevas    
        elif self.canne.coords(self.cercle)[1] ==20 :
            exist=False
            
        if exist==False :
            self.canne.delete(self.cercle)
            
        else :
            # Bouge le projectile aux coordonnés x, y 
            self.canne.move(self.cercle, self.dx, self.dy) 
            # Réitère après 2 ms pour continuer le déplacement
            self.canne.after(20, self.move)
            
    def getCollision (self):
        return(self.collision)
            
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
class ProjectileAlien:
    '''Classe gérant les projectiles des aliens simples'''

#INITIALISATION DES VARIABLES
    
    def __init__(self, general, Hx, Hy, root):
        
        self.general = general
        self.canne = self.general.canne         #canvas
        
        self.root = root
        
        # direction horizontale du projectile
        self.dx = 0
		#direction verticale du projectile
        self.dy = 1
        
        # position du projectile
        self.Hx=Hx
        self.Hy=Hy
        
        #création du projectile
        self.cercle=self.canne.create_oval(self.Hx,self.Hy+10+30,self.Hx+10,self.Hy+20+30, outline='black', fill="lightseagreen")
       
        #lance le projectile avec la méthode move
        self.move()
        
        #Vie du vaisseau (Peut etre vue comme le nombre de fois qu'on peut lui tirer dessus avant que le jeu s'arrete)
        self.ptsVie=3
        
    def move(self):
        '''Méthode gérant le déplacement du projectile'''
        exist=True
        #supprime le projectile si il touche quelqu'un
        self.collision = self.canne.find_overlapping(self.canne.coords(self.cercle)[0]-10,self.canne.coords(self.cercle)[1]-10,self.canne.coords(self.cercle)[0]+10+20,self.canne.coords(self.cercle)[1]+10+20)
        self.collision = self.collision[1:len(self.collision)-1]
        if  exist==True and len(self.collision) > 0:
            self.general.MortVaisseau(self.collision, self.root)
            exist=False

        #Permet la suppression du projectile quand il sort du canevas
        elif self.canne.coords(self.cercle)[1] ==580 :
            exist=False
            
        if exist==False:
            self.canne.delete(self.cercle)
             # réitère la fonction move après 2 ms pour continuer le mouvement
            
        else :
            # Bouge le projectile aux coordonnés x, y 
            self.canne.move(self.cercle, self.dx, self.dy) 
            # réitère la fonction move après 2 ms pour continuer le mouvement
            self.canne.after(2, self.move)
            
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class ProjectileEnnemiBonus:
    '''Classe gérant les projectiles des ennemis Bonus'''
    
 # INITIALISATION DES VARIABLES
 
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
        
        #création des 3 projectile
        self.cercle1=self.canne.create_oval(self.Hx,self.Hy+30,self.Hx+20,self.Hy+20+30, outline='white', fill="red")
        self.cercle2=self.canne.create_oval(self.Hx,self.Hy+30,self.Hx+20,self.Hy+20+30, outline='white', fill="red")
        self.cercle3=self.canne.create_oval(self.Hx,self.Hy+30,self.Hx+20,self.Hy+20+30, outline='white', fill="red")
       
        #lancement  des 3 projectiles
        self.move()
        self.move2()
        self.move3()
        
        
    def move(self):
        ''' méthode permettant la gestion du déplacement du projectile1'''
        exist=True
        
        # #supprime le projectile si il touche quelqu'un
        # self.collision = self.canne.find_overlapping(self.canne.coords(self.cercle)[0]-10,self.canne.coords(self.cercle)[1]-10,self.canne.coords(self.cercle)[0]+10,self.canne.coords(self.cercle)[1]+10)
        # self.collision = self.collision[1:len(self.collision)-1]
        # print(self.collision)
        # if  len(self.collision) > 0:
        #     exist=False

        #Permet la suppression du projectile quand il sort du canevas
        if self.canne.coords(self.cercle1)[1] ==580 :
            exist=False
            
        if exist==False:
            self.canne.delete(self.cercle1)
        else :
            # Bouge le projectile aux coordonnés x, y 
            self.canne.move(self.cercle1, self.dx, self.dy) 
            # Changer la vitesse
            self.canne.after(2, self.move)
            
    def move2(self):
         ''' méthode permettant la gestion du déplacement du projectile2'''
         exist=True
        
         # #supprime le projectile si il touche quelqu'un
         # self.collision = self.canne.find_overlapping(self.canne.coords(self.cercle)[0]-10,self.canne.coords(self.cercle)[1]-10,self.canne.coords(self.cercle)[0]+10,self.canne.coords(self.cercle)[1]+10)
         # self.collision = self.collision[1:len(self.collision)-1]
         # if  len(self.collision) > 0:
         #    exist=False
          
         if self.canne.coords(self.cercle2)[1] ==580 :
             exist=False
             
         if exist==False:
             self.canne.delete(self.cercle2)
         else :
            # Bouge le projectile aux coordonnés x, y 
            self.canne.move(self.cercle2, self.dx2, self.dy2) 
            # Changer la vitesse
            self.canne.after(2, self.move2)

    def move3(self): 
        # ''' méthode permettant la gestion du déplacement du projectile3'''
                  
        exist=True
        
        # #supprime le projectile si il touche quelqu'un
        # self.collision = self.canne.find_overlapping(self.canne.coords(self.cercle)[0]-10,self.canne.coords(self.cercle)[1]-10,self.canne.coords(self.cercle)[0]+10,self.canne.coords(self.cercle)[1]+10)
        # self.collision = self.collision[1:len(self.collision)-1]
        # if  len(self.collision) > 0:
        #     exist=False
            
        if self.canne.coords(self.cercle3)[1] ==580 :
            exist=False
            
        if exist==False:
            self.canne.delete(self.cercle3)
        else :
            # Bouge le projectile aux coordonnés x, y 
            self.canne.move(self.cercle3, self.dx3, self.dy3) 
            # Changer la vitesse
            self.canne.after(2, self.move3)