
import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))

pygame.display.flip()



class Cube:
    def __init__(self,c,d,pos,display:pygame.Surface) -> None:
        self.scren=display
        self.pos=pos
        self.cote=c
        self.distance = d
        self.v=0
        self.h=0
        
        self.points=[pos,[pos[0]+c,pos[1]],[pos[0]+c,pos[1]+c],[pos[0],pos[1]+c]]
        
    def draw(self):
        self.scren.fill((0,0,0))
        for n in range(len(self.points)):
            #print(str(self.points[n])+"  "+str(self.points[n-1]))
            pygame.draw.aaline(self.scren,(255,255,255),self.points[n],self.points[n-1])
        backpoints=[]
        for n in self.points:
            temp =  [n[0]+self.h*self.distance,n[1]+self.v*self.distance]
            pygame.draw.aaline(self.scren,(255,255,255),n,temp)
            #print(n,temp)
            backpoints.append(temp)
        for n in range(len(backpoints)):
            pygame.draw.aaline(self.scren,(255,255,255),backpoints[n-1],backpoints[n])
            #print(backpoints[n-1],backpoints[n])
        
        pygame.display.update()





life = True
cube=Cube(100,1,[200,200],screen)
cube.draw()
down = False
up=False
right=False
left=False

t = pygame.time.Clock()
while life:
    t.tick(30)
    for n in pygame.event.get():
        
        if(n.type==pygame.QUIT):
            print("appelle de la fermeture de la fenêtre !")
            life=False
        elif(n.type==pygame.KEYDOWN):
            
            
            if(n.key==pygame.K_DOWN):
                down=True
            elif(n.key==pygame.K_UP):
                up=True
            elif(n.key==pygame.K_LEFT):
                left=True
            elif(n.key==pygame.K_RIGHT):
                right=True
        elif(n.type==pygame.KEYUP):
            
            
            if(n.key==pygame.K_DOWN):
                down=False
            elif(n.key==pygame.K_UP):
                up=False
            elif(n.key==pygame.K_LEFT):
                left=False
            elif(n.key==pygame.K_RIGHT):
                right=False
        
        
            
    
    if(down):
                cube.v+=1
                cube.draw()
    if(up):
                cube.v-=1
                cube.draw()
    if(left):
                cube.h+=1
                cube.draw()
    if(right):
                cube.h-=1
                cube.draw()