from math import cos 
from math import sinh
import time
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((0,0,0))

pygame.display.flip()

class Vector:
    def __init__(self,x:int,y:int,z:int) -> None:
        self.x=x
        self.y=y
        self.z=z

    def toplane(self) :
        return [self.x,self.y]
    def __add__(self,element):
        return  Vector(self.x+element.x,self.y+element.y,self.z+element.z)
    def __sub__(self,element):
        return  Vector(self.x-element.x,self.y-element.y,self.z-element.z)

    def __str__(self) -> str:
        return '('+str(int(self.x))+";"+str(int(self.y))+';'+str(int(self.z))+')'
    def __format__(self, __format_spec: str) -> str:
        return self.__str__()
    def __hash__(self) -> int:
        pass
    def __repr__(self) -> str:
        return self.__str__()
def D3to2D(co):
    return [co[0],co[1]]



class Cube:
    def __init__(self,cote) -> None:
        self.cote = cote
        self.angle = [0,0,0]
        self.start=Vector(1.5*cote,1.5*cote,0)
        self.points:list[Vector] =[]
        self.create_sommet()
        self.faces = [None] * 6 
        self.color :list[pygame.Color]=[]
        for n in range(6):
            self.color.append(pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        print(self.color)
        self.arretes :list[list[Vector,Vector]]=[]
        self.surface = pygame.Surface((cote*3,cote*3))
        print(len(self.points))
        print(len(self.arretes))
        print(len(self.faces))
        self.create_sommet()
        self.create_face()
        self.create_arrete()

    def create_sommet(self):

    #defenitions des sommets:
        print("calcul des points ....",end='')
        self.points=[]
        """
            self.points[0] = [0,0,0]
            self.points[1] = [self.cote,0,0]
            self.points[2] = [0,self.cote,0]
            self.points[3] = [self.cote,self.cote,0]
            self.points[4] = [0,0,self.cote]
            self.points[5] = [self.cote,0,self.cote]
            self.points[6] = [0,self.cote,self.cote]
            self.points[7] = [self.cote,self.cote,self.cote]
        """
        
        """
        self.points[0] = [0+self.cote,0+self.cote,0+self.cote]
        self.points[1] = [math.cos(self.angle[0]+90)*self.cote+self.cote,math.cos(self.angle[1])*self.cote+self.cote,math.cos(self.angle[2])*self.cote+self.cote]
        self.points[2] = [math.cos(self.angle[0])*self.cote+self.cote,math.cos(self.angle[1]+90)*self.cote+self.cote,math.cos(self.angle[2])*self.cote+self.cote]
        m =  [ (self.points[1][0]+self.points[2][0])/2,(self.points[1][1]+self.points[2][1])/2]
        self.points[3] = [ (2*m[0])-self.points[0][0],(2*m[1])-self.points[0][1],math.cos(self.angle[2])*self.cote+self.cote]
        self.points[4] = [math.cos(self.angle[0])*self.cote+self.cote,math.cos(self.angle[1])*self.cote+self.cote,math.cos(self.angle[2]+90)*self.cote+self.cote]
        self.points[5] = [math.cos(self.angle[0]+90)*self.cote+self.cote,math.cos(self.angle[1])*self.cote+self.cote,math.cos(self.angle[2]+90)*self.cote+self.cote]
        self.points[6] = [math.cos(self.angle[0])*self.cote+self.cote,math.cos(self.angle[1]+90)*self.cote+self.cote,math.cos(self.angle[2]+90)*self.cote+self.cote]
        self.points[7] = [math.cos(self.angle[0]+90)*self.cote+self.cote,math.cos(self.angle[1]+90)*self.cote+self.cote,math.cos(self.angle[2]+90)*self.cote+self.cote]
        """
        
        
        

        x = Vector(cos(self.angle[0])*self.cote,cos(self.angle[1]+1.5)*self.cote,cos(self.angle[2]+1.5)*self.cote)
        y = Vector(cos(self.angle[0]+1.5)*self.cote,cos(self.angle[1])*self.cote,cos(self.angle[2]+1.5)*self.cote)
        z = Vector(cos(self.angle[0]+1.5)*self.cote,cos(self.angle[1]+1.5)*self.cote,cos(self.angle[2])*self.cote)

        self.points.append(Vector(0,0,0))
        self.points.append(x)
        self.points.append(x+y)
        self.points.append(y)
        self.points.append(z)
        self.points.append(x+z)
        self.points.append(x+y+z)
        self.points.append(y+z)
        

        for n in range(len(self.points)):
            self.points[n] = self.points[n]+self.start
      
    def create_face(self):
        #defenitions des faces:
        self.faces=[]
        self.faces.append  ([self.points[0],self.points[1],self.points[2],self.points[3]])
        self.faces.append ([self.points[2],self.points[6],self.points[5],self.points[1]])
        self.faces.append ( [self.points[0],self.points[3],self.points[7],self.points[4]])
        self.faces.append ([self.points[0],self.points[1],self.points[5],self.points[4]])
        self.faces.append ([self.points[3],self.points[2],self.points[6],self.points[7]])
        self.faces.append ([self.points[4],self.points[5],self.points[6],self.points[7]])

    def create_arrete(self):
        #defenitions des arretes
        self.arretes=[]
        self.arretes.append([self.points[0],self.points[1]])
        self.arretes.append  ([self.points[1],self.points[2]])
        self.arretes.append  ([self.points[2],self.points[3]])
        self.arretes.append  ([self.points[0],self.points[4]])
        self.arretes.append  ([self.points[1],self.points[5]])
        self.arretes.append  ([self.points[2],self.points[6]])
        self.arretes.append  ([self.points[3],self.points[7]])
        self.arretes.append  ([self.points[7],self.points[4]])
        self.arretes.append  ([self.points[6],self.points[7]])
        self.arretes.append ([self.points[4],self.points[5]])
        self.arretes.append  ([self.points[6],self.points[5]])
        self.arretes.append ([self.points[0],self.points[3]])
    def rect(self,face) ->pygame.Rect:
        
        top =0 
        left=face[0].x
        height=0
        width  = face[0].y

        for n in face:
            if(not n.x>left):
                left = n.x
            if(n.y>top):
                top = n.y
            if(n.x>width):
                width = n.x
            if(not n.y>height):
                height = n.y
        width =  width -  left
        height = top  -height
        print("top : ",top," left : ",left," largeur : ",width, " hauteur : ",height )
        
        return pygame.Rect(left,top,width,height)
    def poligone(self,face):
        temp=[]
        for n in range(len(face)):
            temp.append([face[n].x,face[n].y])
        
        return temp
    def orderfacebyz(self):
        
        temp =[]
        for n in self.faces:
            maxz=n[0].z
            for m in n:
                if m.z>maxz:
                    maxz=m.z
            temp.append([maxz,n])
        
        


    def draw(self,screen:pygame.Surface,pos):
        
        self.surface.fill((0,0,0))
        self.create_sommet()
        self.create_arrete()
        self.create_face()
        print("Début du tracé du cube avec angle : "+str(self.angle))
        x=0
        self.orderfacebyz()
        for n in self.faces:
            pygame.draw.polygon(self.surface,self.color[x],self.poligone(n))
            x+=1
        for n in self.arretes:      
            pygame.draw.aaline(self.surface,(255,255,255),n[0].toplane() ,n[1].toplane() )
        
            
        screen.blit(self.surface,pos)
        pygame.display.update()
        print(self.points)

       

life = True
cube = Cube(100)
cube.draw(screen,[100,100])



down = False
up=False
right=False
left=False
zup = False
zdown=False
change = False
t = pygame.time.Clock()
while life:
    t.tick(60)
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
            elif(n.key==pygame.K_KP_8):
                zdown=True
            elif(n.key==pygame.K_KP_2):
                zup=True
        elif(n.type==pygame.KEYUP):
            
            
            if(n.key==pygame.K_DOWN):
                down=False
            elif(n.key==pygame.K_UP):
                up=False
            elif(n.key==pygame.K_LEFT):
                left=False
            elif(n.key==pygame.K_RIGHT):
                right=False
            elif(n.key==pygame.K_KP_8):
                zdown=False
            elif(n.key==pygame.K_KP_2):
                zup=False
    if(right):
            cube.angle[0]+=0.05
            change=True
    if(left):
            cube.angle[0]-=0.05
            change=True
    if(down):
            cube.angle[1]-=0.05
            change=True
    if(up):
            cube.angle[1]+=0.05
            change=True
    if(zdown):
            cube.angle[2]-=0.05
            change=True
    if(zup):
            cube.angle[2]+=0.05
            change=True
    if(change):
        cube.draw(screen,[100,100])
        change=False
        print("changement !")
  