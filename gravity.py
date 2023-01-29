#importations de modules
from decimal import DivisionByZero
from tkinter import E
from gpu import *

#Définitions des constantes
RED = pygame.Color(255,0,0)
GREENN = pygame.Color(0,255,0)
BLUE = pygame.Color(0,0,255)
YELLOW = pygame.Color(255,255,0)
CYAN = pygame.Color(0,255,255)
MAGENTA = pygame.Color(255,0,255)
coloreface = [RED,BLUE,GREENN,YELLOW,CYAN,MAGENTA]

G = 6.6742*10**-11#Constante universel




#Declaration des classe
class astre(parallelepipede):
    def __init__(self, surface: pygame.Surface, longueur: int, Largeur: int, profondeur: int, skinsFace, base: Vector = None,masse=0,name="") -> None:
        super().__init__(surface, longueur, Largeur, profondeur, skinsFace, base)
        self.masse = masse
        self.name = name
    def __str__(self) -> str:
        return self.name
        
#initialisation des modules
pygame.init()

#Programme Principale
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN,display=1)
screensize = screen.get_size()
univers = Interface(screen)
t = pygame.time.Clock()
life = True
interation = 0
#Astres initial
univers.append(astre(screen,50,50,50,coloreface,masse=1988900,name='Soleil'))
univers[-1].transform(Vector(screensize[0]/2,screensize[1]/2,0))

univers.append(astre(screen,50,50,50,coloreface,masse=5.9736,name="Terre"))
univers[-1].transform(Vector(screensize[0]/2+150,screensize[1]/2,0))
#Boucle de jeu
while life:
    t.tick(30)
    interation+=1
    for n in pygame.event.get():
        if(n.type == pygame.QUIT):
            print("Fermeture du programme .......")
            life=False
        elif(n.type == pygame.KEYDOWN):
            if(n.key == pygame.K_ESCAPE):
                print("Fermeture du programme .......")
                life=False
        elif(n.type == pygame.MOUSEBUTTONDOWN):
            if(n.button == 3):
                name = input("nom de l'astre >>")
                masse = float(input("masse de l'astre >>"))
                univers.append(astre(screen,100,100,100,coloreface,name = name,masse=masse))
                univers[-1].transform(Vector(n.pos[0],n.pos[1],0))
                
                
    screen.fill((0,0,0))
    for n in univers:
        if(isinstance(n,astre)):
            for i in univers:
                if(isinstance(i,astre) and i!=n):
                    coef = G * i.masse*(10**19)
                    try:
                        x1 = coef/((i.base.x-n.base.x)*1000000)**2
                    except ZeroDivisionError as e:
                        x1 = 0
                    try:
                        y1 = coef/((i.base.y-n.base.y)*1000000)**2
                    except ZeroDivisionError as e:       
                        y1 = 0
                    try:
                        z1 = coef/((i.base.z-n.base.z)*1000000)**2
                    except ZeroDivisionError as e:
                        z1 = 0
                    n.force-=Vector(x1,y1,z1)
        n.update()
        if(interation%30==0):
            print("Update de "+str(n)+" force = "+str(n.force)+" rotation = "+str(n.rotation)+" position = "+str(n.base)) 
        if(n.base.x<0 or n.base.x>univers.screen.get_size()[0] or  n.base.y<0 or n.base.y>univers.screen.get_size()[1]):
            n.force= n.force*(-0.5)
    univers.draw()
    pygame.display.update()

print("Extinction")