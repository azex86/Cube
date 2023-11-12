
from math import cos, sin


import pygame
from random import randint

def randomColor():
    return pygame.Color(randint(0,255),randint(0,255),randint(0,255))


class Vector:
    def __init__(self,x:int,y:int,z:int) -> None:
        self.x=x
        self.y=y
        self.z=z

    def __lt__(self,__o):  
        raise TypeError()
    def __gt__(self,__o):
        raise TypeError()
    def __mul__(self,v):
        if isinstance(v,float) or isinstance(v,int):
            return Vector(self.x*v,self.y*v,self.z*v)
        elif isinstance(v,self.__class__):
            return self.x*v.x+self.y*v.y+self.z*v.z
    def norme(self)->float:

        return ((self.x)**2+(self.y)**2+(self.z)**2)**(1/2) 

    def toplane(self) :
        return [int(self.x),int(self.y)]
    def __add__(self,element):
        return  Vector(self.x+element.x,self.y+element.y,self.z+element.z)
    def __sub__(self,element):
        return  Vector(self.x-element.x,self.y-element.y,self.z-element.z)
    def __truediv__(self,nb:float):
        if(nb==0):
            raise ZeroDivisionError()
        return Vector(self.x/nb,self.y/nb,self.z/nb)
    def __str__(self) -> str:
        return '('+str(self.x)+";"+str(self.y)+';'+str(self.z)+')'
    def __format__(self, __format_spec: str) -> str:
        return self.__str__()
    def __hash__(self) -> int:
        pass
    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        pass
    def __eq__(self, __o: object) -> bool:
        
        if type(__o)==type(self):
            if(self.x==__o.x and self.y==__o.y and self.z==__o.z):
                return True
            else:
                return False
        else:
            if(__o==None):
                return False
            raise TypeError()
    def __getitem__(self,index:int):
        if(index==0):
            return self.x
        elif(index==1):
            return self.y
        elif(index==2):
            return self.z
        else:    
            raise IndexError()
    def __len__(self)->int:
        return 3


class Matrix:
    def __init__(self,l:list) -> None:
        self.list=l
        self.angle=0
    def __mul__(self,obj):
        temp =[]
        for n in range(3):
            temp.append(self.list[0][n](self.angle)*obj[0] + self.list[1][n](self.angle)*obj[1] + self.list[2][n](self.angle)*obj[2])
        return Vector(temp[0],temp[1],temp[2])

def nul(a):
    return 0
def one(a):
    return 1
def nulsin(a):
    return 0-sin(a)
Rx = Matrix([[one,nul,nul]
            ,[nul,cos,sin]
            ,[nul,nulsin,cos]])
Ry = Matrix([[cos,nul,nulsin]
            ,[nul,one,nul]
            ,[sin,nul,cos]])
Rz = Matrix([[cos,sin,nul]
            ,[nulsin,cos,nul]
            ,[nul,nul,one]])
