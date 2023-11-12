

from vector import *



def draw_dash(surface:pygame.Surface,color,A,B):
		x1=A[0]
		x2=B[0]
		y1=A[1]
		y2=B[1]
		[pygame.draw.aaline(surface,color,(x1+(x2-x1)/5*i,y1+(y2-y1)/5*i),(x1+(x2-x1)/10*(i*2+1),y1+(y2-y1)/10*(i*2+1))) for i in range(5)]


class pointer:
    def __init__(self,__o) -> None:
        self.o=__o
    def __call__(self):
        return self.o
class Skin:
    def __init__(self,color=pygame.Color(0,0,0),image=pygame.Surface((0,0),masks=(0,0,0))) -> None:
        self.color = color
        self.image = image

        pass

class Sprite:
    def __init__(self):
        pass

class Forme(Sprite):
    def __init__(self,surface:pygame.Surface,base=Vector(0,0,0),origin=Vector(0,0,0),backgroundskin=Skin(),force:Vector=Vector(0,0,0),rotation:Vector=Vector(0,0,0)) -> None:
        """
                base <=> centre des rotations 
                origin <=> centre de l'objet
        """
        super().__init__()
        self.base=base
        self.backskin = backgroundskin
        self.surface = surface
        self.force = force
        self.rotation = rotation
        self.origin = origin
        self.cache = {}
        
    def transform(self,u:Vector):
        """Deplace l'objet(ses points) ainsi que sa base de u"""
        pass
    def update(self):
        pass
    def draw(self,surface:pygame.Surface)->pygame.surface:
        surface.fill(self.backskin.color)
        return surface
    def Draw(self):
        """Dessine dans self.surface le dessin de l'objet"""
        print("appelle de Draw de la class Forme")
        return
    def forepoint(self)->Vector:
        return Vector(0,0,0)
    def backpoint(self)->Vector:
        return Vector(0,0,0)


class parallelepipede(Forme):
    def __init__(self,surface:pygame.Surface,longueur:int,Largeur:int,profondeur:int,skinsFace,base:Vector=None) -> None:
        super().__init__(surface,base if(base!=None)else Vector(longueur/2,Largeur/2,profondeur/2),Vector(longueur/2,Largeur/2,profondeur/2))
        self.l = longueur
        self.L = Largeur
        self.p = profondeur
        self.r = longueur if(longueur>Largeur and longueur>profondeur) else (Largeur if(Largeur>longueur and Largeur>profondeur) else profondeur )
        self.skinFaces:list[pygame.Color] = skinsFace
        self.points:list[Vector]=[]
        self.lines:list[list[Vector,Vector]] = []
        self.faces:list[list[Vector,Vector,Vector,Vector]] = []
        self.initPoints()
        self.cache = {}
    def initPoints(self):
        self.points = []
        self.points.append(Vector(0,0,0))
        self.points.append(Vector(self.l,0,0))
        self.points.append(Vector(self.l,self.L,0))
        self.points.append(Vector(0,self.L,0))
        self.points.append(Vector(0,0,self.p))
        self.points.append(Vector(self.l,0,self.p))
        self.points.append(Vector(self.l,self.L,self.p))
        self.points.append(Vector(0,self.L,self.p))
    def initArretes(self):
        self.lines=[]
        self.lines.append([self.points[0],self.points[1]])
        self.lines.append([self.points[1],self.points[2]])
        self.lines.append([self.points[2],self.points[3]])
        self.lines.append([self.points[3],self.points[0]])
        self.lines.append([self.points[0],self.points[4]])
        self.lines.append([self.points[1],self.points[5]])
        self.lines.append([self.points[2],self.points[6]])
        self.lines.append([self.points[3],self.points[7]])
        self.lines.append([self.points[4],self.points[5]])
        self.lines.append([self.points[5],self.points[6]])
        self.lines.append([self.points[6],self.points[7]])
        self.lines.append([self.points[7],self.points[4]])
    def initFaces(self):
        self.faces=[]
        self.faces.append([self.points[0],self.points[1],self.points[2],self.points[3]])
        self.faces.append([self.points[4],self.points[5],self.points[6],self.points[7]])
        self.faces.append([self.points[0],self.points[1],self.points[5],self.points[4]])
        self.faces.append([self.points[1],self.points[5],self.points[6],self.points[2]])
        self.faces.append([self.points[3],self.points[2],self.points[6],self.points[7]])
        self.faces.append([self.points[0],self.points[4],self.points[7],self.points[3]])
    def centre(self)->Vector:
        retour = Vector()
    def translate(self,u:Vector)->None:
        """Deplace les point de l'objet de u"""
        for n in range(len(self.points)):
            self.points[n]+=u
        self.origin+=u
    def set_pos(self,pos:Vector):
        u = self.origin-pos
        self.translate(u)
    def transform(self,u:Vector)->None:
        
        self.translate(u)
        self.base+=u
    def translateBase(self,u:Vector):
        """Deplace la base de l'objet de u"""
        self.base+=u
    def rotatex(self,angle):
        self.translate(Vector(0,0,0)-self.base)
        Rx.angle=angle
        for n in range(len(self.points)):
            self.points[n] = Rx*self.points[n]
        self.origin = Rx*self.origin
        self.translate(self.base)
    def rotatey(self,angle):
        self.translate(Vector(0,0,0)-self.base)
        Ry.angle=angle
        for n in range(len(self.points)):
            self.points[n] = Ry*self.points[n]
        self.origin = Ry*self.origin
        self.translate(self.base)
    def rotatez(self,angle):
        self.translate(Vector(0,0,0)-self.base)
        Rz.angle=angle
        for n in range(len(self.points)):
            self.points[n] = Rz*self.points[n]
        self.origin = Rz*self.origin
        self.translate(self.base)
    def backpoint(self)->Vector:
        backpoint = self.points[0]
        for n in self.points:
            if(n.z<backpoint.z):
                backpoint=n
        return backpoint
    def forepoint(self)->Vector:
        backpoint = self.points[0]
        for n in self.points:
            if(n.z>backpoint.z):
                backpoint=n
        return backpoint
    def rightpoint(self)->Vector:
        backpoint = self.points[0]
        for n in self.points:
            if(n.x>backpoint.x):
                backpoint=n
        return backpoint
    def leftpoint(self)->Vector:
        backpoint = self.points[0]
        for n in self.points:
            if(n.x<backpoint.x):
                backpoint=n
        return backpoint
    def toppoint(self)->Vector:
        backpoint = self.points[0]
        for n in self.points:
            if(n.y>backpoint.y):
                backpoint=n
        return backpoint
    def bottompoint(self)->Vector:
        backpoint = self.points[0]
        for n in self.points:
            if(n.y<backpoint.y):
                backpoint=n
        return backpoint

    def isinc(self,cube)->bool:
        """Retourne si il y a ou non collision entre le cube self et le cube passer en argument"""
        assert isinstance(cube,parallelepipede)
        assert isinstance(self,parallelepipede)
        v1_self=(self.points[1]-self.points[0])/(self.points[1]-self.points[0]).norme()
        v2_self=(self.points[3]-self.points[0])/(self.points[3]-self.points[0]).norme()
        v3_self=(self.points[4]-self.points[0])/(self.points[4]-self.points[0]).norme()
        v_self=(v1_self,v2_self,v3_self)
        v1_cube=(cube.points[1]-cube.points[0])/(cube.points[1]-cube.points[0]).norme()
        v2_cube=(cube.points[3]-cube.points[0])/(cube.points[3]-cube.points[0]).norme()
        v3_cube=(cube.points[4]-cube.points[0])/(cube.points[4]-cube.points[0]).norme()
        v_cube=(v1_cube,v2_cube,v3_cube)
        C_self=self.origin
        C_cube=cube.origin
        #print(v1_self)
        #C_self = Vector(0,0,0)
        #for n in self.points:
        #    C_self+=n
        #C_self/=8

        #C_cube = Vector(0,0,0)
        #for n in self.points:
        #    C_cube+=n
        #C_cube/=8

        R=(C_self-self.points[0]).norme()
        for i in [0,6]:
            for j in [0,6]:
                for m in range(3):
                    for n in range(3):
                        if (v_self[m]*v_cube[n])!=0:
                            t=(v_self[m]*self.points[i]-v_self[m]*cube.points[j])/(v_self[m]*v_cube[n])
                            X=cube.points[i]+v_cube[n]*t
                            #print((X-C_cube).norme()-R)
                            if (X-C_cube).norme()<=R and (X-C_self).norme()<=R:
                                #print("True")
                                return True
        return False

    def isin(self,point:Vector)->True|False:
        
        #print("appelle de isin : ")
        #print("Test de l'axe x : ",point.x,'>',self.leftpoint().x," = ",point.x>self.leftpoint().x,"   ",point.x,'<',self.rightpoint().x," = ",point.x<self.leftpoint().x )
        if(point.x>self.leftpoint().x and point.x<self.rightpoint().x):

            #print("Test de l'axe y : ",point.y,'>',self.bottompoint().y," = ",point.y>self.bottompoint().y,"   ",point.y,'<',self.toppoint().y," = ",point.y<self.toppoint().y )
            if(point.y>self.bottompoint().y and point.y<self.toppoint().y):

                #print("Test de l'axe z : ",point.z,'>',self.backpoint().z," = ",point.z>self.backpoint().z,"   ",point.z,'>',self.forepoint().z," = ",point.z<self.forepoint().z )
                if(point.z>self.backpoint().z and point.z<self.forepoint().z):

                    #print("Collision detected")
                    return True
        return False
        
    def forepoint(self)->Vector:
        forepoint = self.points[0]
        for n in self.points:
            if(n.z>forepoint.z):
                forepoint=n
        return forepoint

    def calculateSurface(self)->pygame.Surface:
        
        top = self.points[0].y
        bottom = self.points[0].y
        left = self.points[0].x
        right = self.points[0].x
        for n in self.points:
            if(n.y>top):
                top = n.y
            elif(n.y<bottom):
                bottom = n.y
            if(n.x>right):
                right = n.x
            elif(n.x<left):
                left = n.x
        surface = pygame.Surface((right-left,top-bottom))
        return surface
    def drawFaces(self,screen:pygame.surface):
        self.initFaces()
        backpoint = self.backpoint()
        #print("z = ",self.origin.z)
        for n in range(6):
            if(not backpoint in self.faces[n]):
                temp = self.faces[n].copy()
                for i in range(4):
                    temp[i] = (temp[i]).toplane()
                try:
                    rect = pygame.draw.polygon(screen,self.skinFaces[n],temp)
                except Exception as e:
                    print(e)
                    print(temp)
                    
            
        return 
    def update(self):
        self.rotatex(self.rotation.x)
        self.rotatey(self.rotation.y)
        self.rotatez(self.rotation.z)   
        self.transform(self.force)    
    
        
    def drawLines(self,screen:pygame.Surface,color:pygame.Color):
        self.initArretes()
        
        backpoint = self.points[0]
        
        for n in self.points:
            if(n.z>backpoint.z):
                backpoint=n
        
        for n in self.lines:
            if(not backpoint in n):
                pygame.draw.aaline(screen,color,n[0].toplane(),n[1].toplane())
            else:
                draw_dash(screen,color,n[0].toplane(),n[1].toplane())
                #pygame.draw.aaline(screen,color,n[0].toplane(),n[1].toplane())
        return 

    def Draw(self):
        self.drawFaces(self.surface)
        return
        
class Interface:
    def __init__(self,screen:pygame.Surface) -> None:
        self.screen=screen
        self.elements:list[Forme] =[]

    def append(self,form:Forme):
        self.elements.append(form) 

    def draw(self):
        order =self.elements.copy()
           
        #order.sort(key=lambda x: getattr(x, 'forepoint'))
        order.sort(key=lambda x: getattr( x.forepoint(),'z')) 
        for n in order:
            n.Draw()
    def __getitem__(self,index:int):
        if (index>len(self.elements)):
            raise IndexError()
        return self.elements[index]
    def __len__(self):
        return self.elements.__len__()