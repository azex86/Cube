#==============================================================================#
# Nom du Programme: cinematique 3D
#------------------------------------------------------------------------------------------------------------------------------#
# Auteur:aze
# date:06/10/2022 ~ ......
#==============================================================================#
#----------------------------------------------------------#
# Importation des modules externes #
#----------------------------------------------------------#



from gpu import *
pygame.init()

#--------------------------------------------------#
# Définition des fonctions #
#--------------------------------------------------#



#-------------------------------------------------#
# Programme principal #
#-------------------------------------------------#


screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

pa = parallelepipede(screen,200,200,200,[randomColor(),randomColor(),randomColor(),randomColor(),randomColor(),randomColor()])
pb = parallelepipede(screen,100,100,100,[randomColor(),randomColor(),randomColor(),randomColor(),randomColor(),randomColor()])

pc= parallelepipede(screen,50,50,50,[randomColor(),randomColor(),randomColor(),randomColor(),randomColor(),randomColor()])

pb.translate(Vector(600,50,0))
pc.translate(Vector(50,400,0))
pciterator =0

i = Interface(screen)
i.append(pa)
i.append(pb)
i.append(pc)
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

pointer = False
pointerpast = [0,0]

pa.drawLines(screen,(255,255,255))
pygame.display.update()
while life:
    timer.tick(60)
    for n in pygame.event.get():
        #print(n)
        if(n.type == pygame.QUIT):
            print("Fermeture du programme")
            life = False
            break
        
        elif(n.type == pygame.MOUSEBUTTONDOWN):
            if(n.button==1):
                pointer = True
                pointerpast = n.pos
        elif(n.type == pygame.MOUSEMOTION):
            if(pointer):
                
                axey=(n.pos[0]-pointerpast[0])/5000
                axex=(pointerpast[1]-n.pos[1])/5000
                
        elif(n.type == pygame.MOUSEBUTTONUP):
            if(n.button==1):
                pointer = False
                pointerpast = [0,0]
        elif(n.type == pygame.KEYDOWN):
            if(n.key == pygame.K_z):
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
            elif(n.key == pygame.K_ESCAPE):
                life=False

            
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

    if(zpressed):
        force.y-=1
    if(spressed):
        force.y+=1
    if(qpressed):
        force.x-=1
    if(dpressed):
        force.x+=1
    
    if(force!=Vector(0,0,0)):
        pa.transform(force)
        pb.transform(force)
        pc.transform(force)
        change=True
        force.x *=0.95
        force.y *=0.95
        force.z *=0.95
        if(force.x<0.1 and force.x>-0.1):
            force.x=0
        if(force.y<0.1 and force.y>-0.1):
            force.y=0
        if(force.z<0.1 and force.z>-0.1):
            force.z=0

        

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

    if(axex!=0):
        change=True
        pa.rotatex(axex)
        axex*=0.95
        if(axex<0.001 and axex>-0.001):
            axex=0
    if(axey!=0):
        change=True
        pa.rotatey(axey)
        axey*=0.95
        if(axey<0.001 and axey>-0.001):
            axey=0
    if(axez!=0):
        change=True
        pa.rotatez(axez)
        axez*=0.95
        if(axez<0.001 and axez>-0.001):
            axez=0
    pb.base = pa.base
    temp = pc.origin
    pb.rotatey(0.1)
    dif = pb.origin-temp
  
    pc.base=pb.base
    pc.translate(dif+Vector(25,400,0))
    pciterator+=0.2
    pc.rotatex(pciterator)
    change=True

    if(change):
        change=False
        screen.fill((0,0,0))
        #pa.drawLines(screen,(255,255,255))
        i.draw()
        pygame.display.update()
        

