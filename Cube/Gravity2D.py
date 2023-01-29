#==============================================================================#
# Nom du Programme: simulation de la gravité en 2 Dimension
#------------------------------------------------------------------------------------------------------------------------------#
# Auteur:aze
# date:08/10/2022 ~ ......
#==============================================================================#
#----------------------------------------------------------#
# Importation des modules externes #
#----------------------------------------------------------#
import random
import math
import time
import pygame


#.......................................................
#Définition des constantes
#........................................................
G = 6.6742*(10**-11)
T = 60*60*24*10**0
I = 0
DEBUG = False
MS = 1988900 *10**24
MT = 5.9736 * 10**24

SCALE = 150/4*10**8 #1000 -> 4*150 10*9
#---------------------------------------------------
#Definition des fonction constante
#--------------------------------------------------
def randcolor()->pygame.Color:
    return pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#--------------------------------------------------#
# Définition des  classes #
#--------------------------------------------------#
class Vector:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y = y
    def __str__(self) -> str:
        return '('+str(self.x)+';'+str(self.y)+')'
    def __add__(self,u):
        return Vector(self.x+u.x,self.y+u.y )
    def __sub__(self,u):
        return Vector(self.x-u.x,self.y-u.y)
    def __mul__(self,nb:float):
        return Vector(self.x*nb,self.y*nb)
    def __truediv__(self,nb:float):
        return Vector(self.x/nb,self.y/nb)
    def topoint(self):
        """Retourne le vecteur sous la forme d'une paire de coordonnées"""
        return (self.x,self.y)
    def norme(self)->int:
        """Retourne la norme du vecteur"""
        return (self.x**2 + self.y**2)**(1/2)
class Astre:
    def __init__(self,masse:float,position=Vector(0,0),name="corps céleste inconnu",vitesse=Vector(0,0),color=randcolor(),rayon=2) -> None:
        self.m = masse
        self.pos = position
        self.name = name
        self.v = vitesse
        self.color = color
        self.r = rayon
        
    def __str__(self) -> str:
        return self.name
    def avance(self):
        self.pos+=self.v*T
    def draw(self,screen:pygame.display):
        pos = self.pos.topoint()
        fpos = [pos[0]/SCALE,pos[1]/SCALE]
        
        pygame.draw.circle(screen,self.color,fpos,self.r)
    def addforce(self,force):
        self.v+=force*T/self.m
#------------------------------------------------
#Fonctions sur les classes
#----------------------------------------------
def g(a:Astre,b:Astre):
    d = ((a.pos-b.pos).norme())
    f = -G * a.m * b.m /(d**2)
    if(I%60==0 and DEBUG):
        print("Calcule de l'interaction entre "+str(a)+"et"+str(b))
        print("masse de "+str(a)+" = "+str(a.m)+"Kg\tmasse de "+str(b)+" = "+str(b.m)+"Kg")
        print("Distance "+str(a)+"-"+str(b)+" = "+str(d)+" mètres")
    x1 = abs(a.pos.x - b.pos.x)
    x2 = f/d *x1
    y1 = abs(a.pos.y - b.pos.y)
    y2 = f/d *y1
    v = Vector(x2,y2)
    if(I%60==0):
        print("Force = "+str(f)+" soit "+str(v))
    return v
#-------------------------------------------------
#Initialisation de Pygame
#------------------------------------------------



pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN,display=1)
screen.fill((0,0,0))
sizeScreen = screen.get_size()
CENTRE = Vector(sizeScreen[0]/2,sizeScreen[1]/2)
print(sizeScreen)
t = pygame.time.Clock()


life = True
pause = False
univers:list[Astre] = []
Soleil = Astre(MS,Vector(sizeScreen[0]/2*SCALE,sizeScreen[1]/2*SCALE),vitesse=Vector(0,0),name='Soleil',color=pygame.Color(255,255,0))
univers.append(Soleil)
Terre = Astre(MT,Soleil.pos-Vector(-150*10**9,0),vitesse=Vector(0,30000),name="Terre",color=pygame.Color(0,0,255))
univers.append(Terre)
Soleil.draw(screen)
Terre.draw(screen)
pygame.display.update()
time.sleep(1)
while life:
    t.tick(60)
    if(not pause):
        I+=1
        for n in univers:
            for n1 in univers:
                if(n1!=n):
                    n.addforce(g(n,n1))
            n.avance()
            n.draw(screen)
        pygame.display.update()
    for n in pygame.event.get():
        if(n.type==pygame.QUIT):
            life=False
        elif(n.type==pygame.MOUSEWHEEL):
            
            if(n.y!=0):
                temp = []
                for var in univers:
                    temp .append(CENTRE-var.pos/SCALE)
                tscale = SCALE
                if(n.y<0):
                    SCALE*=1.5
                else:
                    SCALE*=0.75
                for var in range(len(univers)):
                    univers[var].pos = (CENTRE-temp[var]*(tscale/SCALE))*SCALE
                screen.fill((0,0,0))
                print("SCALE = "+str(SCALE))
        elif(n.type==pygame.KEYDOWN):
            if(n.key==pygame.K_ESCAPE):
                life = False
            elif(n.key == pygame.K_SPACE):
                pause=True
            elif(n.key == pygame.K_DOWN):
                T*=0.90
                print("Temps pas incrementation : "+str(T)+" secondes")
            elif(n.key == pygame.K_UP):
                T*=1.10
                print("Temps pas incrementation : "+str(T)+" secondes")
        elif(n.type == pygame.KEYUP):
            if(n.key == pygame.K_SPACE):
                pause=False


