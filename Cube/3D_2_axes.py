import pygame
import math
import numpy as np

def draw_dash(A,B):
		x1=A[0]
		x2=B[0]
		y1=A[1]
		y2=B[1]
		[pygame.draw.line(surface,'#111111',(x1+(x2-x1)/5*i,y1+(y2-y1)/5*i),(x1+(x2-x1)/10*(i*2+1),y1+(y2-y1)/10*(i*2+1))) for i in range(5)]

def draw_line(A,B):
	pygame.draw.line(surface,'white',A,B)
	
pygame.init()
surface = pygame.display.set_mode((1920, 1080))
centre=(1920//2,1080//2)
c0=centre[0]
c1=centre[1]
ay=200
ax=np.sqrt(2)*ay
pi=math.pi
theta=0
beta=0
phi=0
deltax=0
deltay=0
pos=(0,0)
pos1=(0,0)
touched=False

life = True
while life:
	for ev in pygame.event.get():
		if(ev.type == pygame.QUIT):
			life=False
		elif ev.type==pygame.MOUSEBUTTONDOWN and not touched:
			pos=pygame.mouse.get_pos()
			touched=True
		elif ev.type==pygame.MOUSEBUTTONUP:
			touched=False
		elif touched:
			pos1=pygame.mouse.get_pos()
			deltax=pos[0]-pos1[0]
			deltay=pos[1]-pos1[1]
	surface.fill((0, 0, 0))
	doigt=pygame.mouse.get_pos()
	theta-=(deltax)*pi/360
	phi+=(deltay)*pi/740
	beta=phi
	mattheta=np.array(((np.cos(theta),0,np.sin(theta)),(0,1,0),(-np.sin(theta),0,np.cos(theta))))
	matbeta=np.array(((1,0,0),(0,np.cos(beta),-np.sin(beta)),(0,np.sin(beta),np.cos(beta))))
	pos=pos1
	
	pt=matbeta.dot(mattheta.dot((ax,ay,0)))
	x=pt[0]
	y=pt[1]
	z=pt[2]
	A1=(x+c0,y+c1,z)
	B1=(-x+c0,-y+c1,-z)
	
	pt=matbeta.dot(mattheta.dot((ax,-ay,0)))
	x=pt[0]
	y=pt[1]
	z=pt[2]
	C1=(x+c0,y+c1,z)
	D1=(-x+c0,-y+c1,-z)
	
	pt=matbeta.dot(mattheta.dot((0,ay,ax)))
	x=pt[0]
	y=pt[1]
	z=pt[2]
	A2=(x+c0,y+c1,z)
	B2=(-x+c0,-y+c1,-z)
	
	pt=matbeta.dot(mattheta.dot((0,-ay,ax)))
	x=pt[0]
	y=pt[1]
	z=pt[2]
	C2=(x+c0,y+c1,z)
	D2=(-x+c0,-y+c1,-z)
	
	
	#pygame.draw.line(surface,'red',A1,B1)
#	pygame.draw.line(surface,'yellow',B1,C1)
#	pygame.draw.line(surface,'blue',C1,D1)
#	pygame.draw.line(surface,'green',D1,A1)
#	
#	pygame.draw.line(surface,'white',A2,B2)
#	pygame.draw.line(surface,'grey',B2,C2)
#	pygame.draw.line(surface,'sky blue',C2,D2)
#	pygame.draw.line(surface,'purple',D2,A2)
	
	zmin=min(A1[2],A2[2],B1[2],B2[2],C1[2],C2[2],D1[2],D2[2])
	
	if A1[2]<=zmin or A2[2]<=zmin:
		draw_dash((A1[0],A1[1]),(A2[0],A2[1]))
	else: draw_line((A1[0],A1[1]),(A2[0],A2[1]))
	if D1[2]<=zmin or A2[2]<=zmin:
		draw_dash((D1[0],D1[1]),(A2[0],A2[1]))
	else: draw_line((D1[0],D1[1]),(A2[0],A2[1]))
	if D1[2]<=zmin or D2[2]<=zmin:
		draw_dash((D1[0],D1[1]),(D2[0],D2[1]))
	else: draw_line((D1[0],D1[1]),(D2[0],D2[1]))
	if A1[2]<=zmin or D2[2]<=zmin:
		draw_dash((A1[0],A1[1]),(D2[0],D2[1]))
	else: draw_line((A1[0],A1[1]),(D2[0],D2[1]))
	if C1[2]<=zmin or C2[2]<=zmin:
		draw_dash((C1[0],C1[1]),(C2[0],C2[1]))
	else: draw_line((C1[0],C1[1]),(C2[0],C2[1]))
	if B1[2]<=zmin or C2[2]<=zmin:
		draw_dash((B1[0],B1[1]),(C2[0],C2[1]))
	else: draw_line((B1[0],B1[1]),(C2[0],C2[1]))
	if B1[2]<=zmin or B2[2]<=zmin:
		draw_dash((B1[0],B1[1]),(B2[0],B2[1]))
	else: draw_line((B1[0],B1[1]),(B2[0],B2[1]))
	if A1[2]<=zmin or C1[2]<=zmin:
		draw_dash((A1[0],A1[1]),(C1[0],C1[1]))
	else: draw_line((A1[0],A1[1]),(C1[0],C1[1]))
	if B1[2]<=zmin or D1[2]<=zmin:
		draw_dash((B1[0],B1[1]),(D1[0],D1[1]))
	else: draw_line((B1[0],B1[1]),(D1[0],D1[1]))
	if B2[2]<=zmin or D2[2]<=zmin:
		draw_dash((B2[0],B2[1]),(D2[0],D2[1]))
	else: draw_line((B2[0],B2[1]),(D2[0],D2[1]))
	if A2[2]<=zmin or C2[2]<=zmin:
		draw_dash((A2[0],A2[1]),(C2[0],C2[1]))
	else: draw_line((A2[0],A2[1]),(C2[0],C2[1]))
	if B2[2]<=zmin or C1[2]<=zmin:
		draw_dash((B2[0],B2[1]),(C1[0],C1[1]))
	else: draw_line((B2[0],B2[1]),(C1[0],C1[1]))
	
	deltax=deltax/1.01
	deltay=deltay/1.01
	pygame.display.flip()
	
	