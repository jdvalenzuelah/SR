#Lab 01
#Universidad del Valle de Guatemala
#Josue Valenzuela 171001
#git testd
from SR import *
from random import random

image = SR()
image.glInit()
image.glCreateWindow(800, 800)
image.glViewPort(0,0,800,800)
image.setFileName("LAB01.bmp")
image.glColor(0,0,0)
#Poligono 1:
poligono1  = [(image.norX(165), image.norY(380)), (image.norX(185), image.norY(360)), (image.norX(180), image.norY(330)), (image.norX(207), image.norY(345)), (image.norX(233), image.norY(330)), (image.norX(230), image.norY(360)), (image.norX(250), image.norY(380)), (image.norX(220), image.norY(385)), (image.norX(205), image.norY(410)), (image.norX(193), image.norY(383))]
image.glFilledPolygon(poligono1, (random(), random(), random()))

#Poligono 2:
poligono2  = [(image.norX(339), image.norY(251)), (image.norX(374), image.norY(302)), (image.norX(321), image.norY(335)), (image.norX(288), image.norY(286))]
image.glFilledPolygon(poligono2, (random(), random(), random()))

#Poligono 3:
poligono3  = [(image.norX(377), image.norY(249)), (image.norX(436), image.norY(249)), (image.norX(411), image.norY(197))]
image.glFilledPolygon(poligono3, (random(), random(), random()))

#Poligono 4:vertexList)
poligono4  = [(image.norX(413), image.norY(177)), (image.norX(448), image.norY(159)), (image.norX(502), image.norY(88)), (image.norX(553), image.norY(53)), (image.norX(535), image.norY(36)), (image.norX(676), image.norY(37)), (image.norX(660), image.norY(52)), (image.norX(750), image.norY(145)), (image.norX(761), image.norY(179)), (image.norX(672), image.norY(192)), (image.norX(659), image.norY(214)), (image.norX(615), image.norY(214)), (image.norX(632), image.norY(230)), (image.norX(580), image.norY(230)), (image.norX(597), image.norY(215)), (image.norX(552),image.norY(214)), (image.norX(517),image.norY(144)), (image.norX(466),image.norY(180))]
image.glFilledPolygon(poligono4, (random(), random(), random()))
poligono5  = [(image.norX(682), image.norY(175)), (image.norX(708), image.norY(120)), (image.norX(735), image.norY(148)) ,(image.norX(739), image.norY(170))]
image.glFilledPolygon(poligono5)

image.glFinish()
image.glClear()
