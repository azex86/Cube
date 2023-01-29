#importations de modules

import random
from gpu import *

#Définitions des constantes
RED = pygame.Color(255,0,0)
GREENN = pygame.Color(0,255,0)
BLUE = pygame.Color(0,0,255)
YELLOW = pygame.Color(255,255,0)
CYAN = pygame.Color(0,255,255)
MAGENTA = pygame.Color(255,0,255)
GRIS = pygame.Color(200,200,200)
coloreface = [RED,BLUE,GREENN,YELLOW,CYAN,MAGENTA]
coloreselected = [(200,200,200),(220,200,200),(200,220,200),(200,200,220),(220,220,200),(200,220,220)]
#Definitions des fonctions
def collision(a:parallelepipede,b:parallelepipede):
    """Retourne la force à exerce sur a en cas de collision avec b"""
    #print("Appelle de colision sur "+str(a.origin)+" "+str(b.origin))
    #return (a.origin-b.origin)/100 
    return (a.origin-b.origin)/10
    #a.force,b.force=b.force,a.force

def rand(a:float=-1,b:float=1)->float:
    """Retourne une valeur aléatoire comprise entre a et b"""
    signe =1 if(random.randint(0,1)==1)else -1
    value = random.random()*(b-a) + a
    return signe*value


#initialisation des modules
pygame.init()
di = pygame.display.get_num_displays()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN,display=di-1)
univers = Interface(screen)
L,H = screen.get_size()

t = pygame.time.Clock()

axex = 0
axey = 0
axez = 0
force =  Vector(0,0,0)

timer = pygame.time.Clock()
life = True
change = True

qpressed = False
dpressed = False
zpressed = False
spressed = False

axexpressed = False
axemxpressed = False
axeypressed = False
axemypressed = False
axezpressed = False
axemzpressed = False

pause = False
main = 0

click = False
posclick = []
objectposclick:parallelepipede = None

life = True
while life:
    if(not pause):
        screen.fill((0,0,0))
        if(click and isinstance(objectposclick,parallelepipede)):
            objectposclick.Draw()
    t.tick(30)
    for n in pygame.event.get():
        if(n.type == pygame.QUIT):
            print("Fermeture du programme .......")
            life=False
        elif(n.type == pygame.KEYDOWN):
            if(n.key == pygame.K_ESCAPE):
                print("Fermeture du programme .......")
                life=False
            elif(n.key == pygame.K_z):
                zpressed=True
                
            elif(n.key == pygame.K_s):
                spressed=True
            elif(n.key == pygame.K_q):
                qpressed=True
            elif(n.key == pygame.K_d):
                dpressed=True

            elif(n.key == pygame.K_UP):
                axexpressed=True
            elif(n.key == pygame.K_DOWN):
                axemxpressed=True
            elif(n.key == pygame.K_LEFT):
                axeypressed=True
            elif(n.key == pygame.K_RIGHT):
                axemypressed=True
            elif(n.key == pygame.K_KP8):
                axezpressed=True
            elif(n.key == pygame.K_KP2):
                axemzpressed=True
            elif(n.key == pygame.K_SPACE):
                pause=True
        elif(n.type==pygame.KEYUP):
            if(n.key == pygame.K_z):
                zpressed=False
            elif(n.key == pygame.K_s):
                spressed=False
            elif(n.key == pygame.K_q):
                qpressed=False
            elif(n.key == pygame.K_d):
                dpressed=False

            elif(n.key == pygame.K_UP):
                axexpressed=False
            elif(n.key == pygame.K_DOWN):
                axemxpressed=False
            elif(n.key == pygame.K_LEFT):
                axeypressed=False
            elif(n.key == pygame.K_RIGHT):
                axemypressed=False
            elif(n.key == pygame.K_KP8):
                axezpressed=False
            elif(n.key == pygame.K_KP2):
                axemzpressed=False
            elif(n.key == pygame.K_TAB):
                univers[main].skinFaces = coloreface
                main+=1
                if(main==len(univers)):
                    main=0
                univers[main].skinFaces = coloreselected
                print("Force de l'objet = ",univers[main].force," position de l'objet",univers[main].origin)
            elif(n.key == pygame.K_SPACE):
                pause=False

        elif(n.type == pygame.MOUSEBUTTONDOWN):
            if(n.button == 1):
                click = True
                posclick = n.pos
                
        elif(n.type == pygame.MOUSEMOTION):
            if(click):
                size = Vector(n.pos[0]-posclick[0],n.pos[1]-posclick[1],100)
                objectposclick = parallelepipede(screen,size.x,size.y,size.z,coloreselected)
                objectposclick.transform(Vector(posclick[0],posclick[1],0))
                objectposclick.Draw()

        elif(n.type == pygame.MOUSEBUTTONUP):
            if(n.button == 1 and click):
                size = Vector(n.pos[0]-posclick[0],n.pos[1]-posclick[1],100)
                print(size)
                univers.append(parallelepipede(screen,size.x,size.y,size.z,coloreface))
                univers[-1].transform(Vector(posclick[0],posclick[1],0))
                univers[-1].force = Vector(0,1,0)
                univers[-1].rotation = Vector(0.01,0.01,0)
                univers[-1].cache['bordure']=False
                click = False



    if(not pause):
        
        for n in univers:
                n.update()
                if(n.cache["bordure"]==False):
                    
                    if(n.origin.x<0):
                        n.force=Vector(n.force.x*-0.75,rand(-n.force.y,n.force.y),0)
                        n.cache["bordure"]= True
                    if(n.origin.y<0):   
                        n.force=Vector(rand(-n.force.x,n.force.x),n.force.y*-0.75,0)
                        n.cache["bordure"]= True
                    if(n.origin.x>L):
                        n.force=Vector(n.force.x*-0.75,rand(-n.force.y,n.force.y),0)
                        n.cache["bordure"]= True
                    if(n.origin.y>H):
                        n.force=Vector(rand(-n.force.x,n.force.x),n.force.y*-0.75,0)
                    
                        n.cache["bordure"]= True
                    #elif(n.origin.z>100):
                    #    n.force.z=0
                    #    n.force+=Vector(random.random()/10,random.random()/10,0)
                    #elif(n.origin.z<0):
                    #    n.force.z=0
                    #    n.force+=Vector(random.random()/10,random.random()/10,0)
                    if(n.cache["bordure"]== False):
                        for var in univers:
                                if(n!=var and var.cache['bordure']==False):
                                    colision =False
                                    #for an in n.points:
                                    #    if(var.isin(an)):
                                    #        colision=True
                                    if((var.origin-n.origin).norme()<var.r+n.r ):
                                        if(var.isinc(n)):
                                            colision=True
                                    if(colision):
                                        n.force=collision(n,var)
                else:
                    if(n.origin.x>0 and n.origin.x<L and n.origin.y>0 and n.origin.y<H):
                        n.cache['bordure'] = False
                
                
        univers.draw()
        police = pygame.font.SysFont('monospace',15)
        txt = police.render(str(len(univers)),1,(255,255,255))
        screen.blit(txt,(0,0))
        pygame.display.update()
        """
            force.x *=0.95
            force.y *=0.95
            force.z *=0.95
        """
        if(force.x<0.1 and force.x>-0.1):
            force.x=0
        if(force.y<0.1 and force.y>-0.1):
            force.y=0
        if(force.z<0.1 and force.z>-0.1):
            force.z=0

        if(zpressed):
            force.y-=1
        if(spressed):
            force.y+=1
        if(qpressed):
            force.x-=1
        if(dpressed):
            force.x+=1
        

        if(axexpressed):
            axex+=0.010
        if(axemxpressed):
            axex-=0.010
        if(axeypressed):
            axey+=0.010
        if(axemypressed):
            axey-=0.010
        if(axezpressed):
            axez+=0.010
        if(axemzpressed):
            axez-=0.010

        if(len(univers)>0):
                n = univers[main]
                if(force!=Vector(0,0,0)):
                    n.force+=force
                    force = Vector(0,0,0)
                    
                if(axex!=0):
                    change=True   
                    n.rotatex(axex)
                    axex*=0.95
                    if(axex<0.001 and axex>-0.001):
                        axex=0
                if(axey!=0):
                    change=True      
                    n.rotatey(axey)
                    axey*=0.95
                    if(axey<0.001 and axey>-0.001):
                        axey=0
                if(axez!=0):
                    change=True    
                    n.rotatez(axez)
                    axez*=0.95
                    if(axez<0.001 and axez>-0.001):
                        axez=0



print("Extinction")