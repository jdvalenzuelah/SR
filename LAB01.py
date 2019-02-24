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
poligono1  = [(image.norX(165), image.norY(380),0), (image.norX(185), image.norY(360),0), (image.norX(180), image.norY(330),0), (image.norX(207), image.norY(345),0), (image.norX(233), image.norY(330),0), (image.norX(230), image.norY(360),0), (image.norX(250), image.norY(380),0), (image.norX(220), image.norY(385),0), (image.norX(205), image.norY(410),0), (image.norX(193), image.norY(383),0)]
image.glFilledPolygon(poligono1, (random(), random(), random()))

#Poligono 2:
poligono2  = [(image.norX(339), image.norY(251),0), (image.norX(374), image.norY(302),0), (image.norX(321), image.norY(335),0), (image.norX(288), image.norY(286),0)]
image.glFilledPolygon(poligono2, (random(), random(), random()))

#Poligono 3:
poligono3  = [(image.norX(377), image.norY(249),0), (image.norX(436), image.norY(249),0), (image.norX(411), image.norY(197),0)]
image.glFilledPolygon(poligono3, (random(), random(), random()))

#Poligono 5
poligono5  = [(image.norX(682), image.norY(175),0), (image.norX(708), image.norY(120),0), (image.norX(735), image.norY(148),0) ,(image.norX(739), image.norY(170),0)]
image.glFilledPolygon(poligono5, (0,0,0))

#Poligono 4:vertexList)
poligono4  = [(image.norX(413), image.norY(177),0), (image.norX(448), image.norY(159),0), (image.norX(502), image.norY(88),0), (image.norX(553), image.norY(53),0), (image.norX(535), image.norY(36),0), (image.norX(676), image.norY(37),0), (image.norX(660), image.norY(52),0), (image.norX(750), image.norY(145),0), (image.norX(761), image.norY(179),0), (image.norX(672), image.norY(192),0), (image.norX(659), image.norY(214),0), (image.norX(615), image.norY(214),0), (image.norX(632), image.norY(230),0), (image.norX(580), image.norY(230),0), (image.norX(597), image.norY(215),0), (image.norX(552),image.norY(214),0), (image.norX(517),image.norY(144),0), (image.norX(466),image.norY(180),0)]
image.glFilledPolygon(poligono4, (random(), random(), random()))


image.glFinish()
image.glClear()
