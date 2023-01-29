

import time


import pygame
import random
from gpu import *
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((0,0,0))

pygame.display.flip()

cube = Cube(100,Vector(300,300,0),Vector(50,50,50))

life=True

down =0
up=0
right=0
left=0
zup = False
zdown=False
change = False

forward=False
backward=False
forwardleft=False
forwardright=False

t = pygame.time.Clock()
while life:
    t.tick(60)
    for n in pygame.event.get():
        
        if(n.type==pygame.QUIT):
            print("appelle de la fermeture de la fenêtre !")
            life=False
        elif(n.type==pygame.KEYDOWN):
            if(n.key==pygame.K_DOWN):
                down=0.01
            elif(n.key==pygame.K_UP):
                up=0.01
            elif(n.key==pygame.K_LEFT):
                left=0.01
            elif(n.key==pygame.K_RIGHT):
                right=0.01
#            elif(n.key==pygame.K_KP_8):
                
 #               zdown=True
  #          elif(n.key==pygame.K_KP_2):
   #             zup=True
            elif(n.key==pygame.K_z):
                forward=True
            elif(n.key==pygame.K_s):
                backward=True
            elif(n.key==pygame.K_q):
                forwardleft=True
            elif(n.key==pygame.K_d):
                forwardright=True
        elif(n.type==pygame.KEYUP):
            if(n.key==pygame.K_DOWN):
                down=0
            elif(n.key==pygame.K_UP):
                up=0
            elif(n.key==pygame.K_LEFT):
                left=0
            elif(n.key==pygame.K_RIGHT):
                right=0
   #         elif(n.key==pygame.K_KP_8):
    #            zdown=False
    #        elif(n.key==pygame.K_KP_2):
    #            zup=False
            elif(n.key==pygame.K_z):
                forward=False
            elif(n.key==pygame.K_s):
                backward=False
            elif(n.key==pygame.K_q):
                forwardleft=False
            elif(n.key==pygame.K_d):
                forwardright=False
    if(right>0):
            cube.rotatey(0-right)
            print(right)
            right*=1.02
            change=True
    if(left>0):
            cube.rotatey(left)
            left*=1.02
            change=True
    if(down>0):
            cube.rotatex(-down)
            down*=1.02
            change=True
    if(up>0):
            cube.rotatex(up)
            up*=1.02
            change=True
    if(zdown):
            cube.rotatez(-0.05)
            change=True
    if(zup):
            cube.rotatez(0.05)
            change=True
    if(forwardright):
        cube.translate(Vector(1,0,0))
        cube.translateBase(Vector(1,0,0))
        change=True
    if(forwardleft):
        cube.translate(Vector(-1,0,0))
        cube.translateBase(Vector(-1,0,0))
        change=True
    if(forward):
        cube.translate(Vector(0,-1,0))
        cube.translateBase(Vector(0,-1,0))
        change=True
    if(backward):
        cube.translate(Vector(0,1,0))
        cube.translateBase(Vector(0,1,0))
        change=True

    if(change):
        screen.fill((0,0,0))
        cube.draw(screen)
        change=False

        