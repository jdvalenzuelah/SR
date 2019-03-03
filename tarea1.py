# -*- coding: cp1252 -*-
from Render.SR import *
import random

#Creamos el archivo sobre el cual se trabajara
image = SR()
image.glInit()
image.glCreateWindow(200, 200)
image.glViewPort(0,0,199,199)

#Punto random blanco en un fondo negro
image.setFileName("./testResults/randPoint.bmp")
x = random.uniform(-1,1)
y = random.uniform(-1,1)
image.glVertex(x,y)
image.glFinish()
image.glClear()

#Punto blanco en cada esquina
image.setFileName("./testResults/cornerPoints.bmp")
image.glVertex(-1,1)
image.glVertex(-1,-1)
image.glVertex(1,1)
image.glVertex(1,-1)
image.glFinish()
image.glClear()

#Orilla blanca en las orillas de las imagenes
image.setFileName("./testResults/whiteBorder.bmp")
coe = 1/199
for x in range(-199,199):
	image.glVertex((x*coe), -1)
	image.glVertex((x*coe), 1)
	image.glVertex(-1, (x*coe))
	image.glVertex(1, (x*coe))
image.glFinish()
image.glClear()

#Diagonal por el centro dela imagen
image.setFileName("./testResults/diagonal.bmp")
coe = 1/199
for x in range(199):
	image.glVertex((x*coe), (x*coe))
	image.glVertex((x*coe*-1), (x*coe*-1))
image.glFinish()
image.glClear()

#Llenar la imagen de puntos blancos y negros
image.setFileName("./testResults/blackAndwhite.bmp")
for x in range(-199,199):
	for y in range(-199,199):
		color = random.choice([1,0])
		image.glColor(color, color, color)
		image.glVertex(x*coe,y*coe)
image.glFinish()

#Puntos de colores random
image.setFileName("./testResults/randomColor.bmp")
for x in range(-199,199):
	for y in range(-199,199):
		image.glColor(random.random(), random.random(), random.random())
		image.glVertex(x*coe,y*coe)
image.glFinish()

#Cubo en el centro de la imagen
image.setFileName("./testResults/centerCube.bmp")
image.glCreateWindow(500, 500)
image.glViewPort(0,0,499,499)
image.glColor(1,1,1)
coe = 1/499
for x in range(-100,100):
	#first square
	image.glVertex((x*coe), (-100*coe))
	image.glVertex((x*coe), (100*coe))
	image.glVertex((-100*coe), (x*coe))
	image.glVertex((100*coe), (x*coe))
	#second square
	image.glVertex(((x-50)*coe), (-50*coe))
	image.glVertex(((x-50)*coe), (150*coe))
	image.glVertex((-150*coe), ((x+50)*coe))
	image.glVertex((50*coe), ((x+50)*coe))
	#Uniones para darle ilusion de cubo
	if(x >= 50):
		image.glVertex((x*coe), ((-x+200)*coe))
		image.glVertex((x*coe), ((-x*coe)))
		image.glVertex(((x-200)*coe), ((-x+200)*coe))
		image.glVertex(((x-200)*coe), ((-x*coe)))
image.glFinish()
image.glClear()

#cielo con estrellas
image.setFileName("./testResults/stars.bmp")
image.glColor(1,1,1)
for x in range(random.randint(100, 200)):
	x = random.uniform(-1,1)
	y = random.uniform(-1,1)
	image.glVertex(x,y)
image.glFinish()
image.glClear()

#Escena de atari
image.glCreateWindow(200, 200)
image.glViewPort(20,4,160,192)
image.setFileName("./testResults/atariScene.bmp")
coex = 1/160
coey = 1/192
image.glColor(0.83,0.83,0.83)
for x in range(-180,180):
	for y in range(120, 160):
		image.glVertex(x*coex,(y*coey)+coey)

for y in range(-159, 159):
	for x in range(-180, -160):
		image.glVertex((x*coex)+coex, y*coey)
		image.glVertex((x*coex*-1)+coex, y*coey*-1)

image.glColor(0.86,0.08,0.24)
for x in range(-155,160):
	for y in range(70, 80):
		image.glVertex(x*coex,(y*coey)+coey)

image.glColor(1,0.39,0.28)
for x in range(-155,160):
	for y in range(60, 70):
		image.glVertex(x*coex,(y*coey)+coey)

image.glColor(0.98,0.98,0.82)
for x in range(-155,160):
	for y in range(49, 59):
		image.glVertex(x*coex,(y*coey)+coey)

image.glColor(0,1,0)
for x in range(-155,160):
	for y in range(38, 48):
		image.glVertex(x*coex,(y*coey)+coey)

image.glColor(0,0,1)
for x in range(-130,160):
	for y in range(27, 37):
		image.glVertex(x*coex,(y*coey)+coey)

image.glColor(1,0,0)
for x in range(25,75):
	for y in range(-160, -155):
		image.glVertex(x*coex,(y*coey)+coey)

for x in range(90,95):
	for y in range(-130, -125):
		image.glVertex(x*coex,(y*coey)+coey)

image.glFinish()
image.glClear()

