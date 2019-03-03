# -*- coding: cp1252 -*-
#Universidad del Valle de Guatemala
#Josue Valenzuela 171001

from Render.SR import *

#Creamos el archivo sobre el cual se trabajara
image = SR()
image.glInit()
image.glCreateWindow(800, 800)
image.glViewPort(0,0,800,800)
cx = 1/800
cy = 1/800

"""
File: lineas1.bmp
""" 
image.setFileName("./testResults/lineas1.bmp")
#(10, 10), (510, 10)
image.glLine(10*cx,10*cy,510*cx,10*cy)
#(10, 10), (510, 10)
image.glLine(10*cx,10*cy,462*cx,191*cy)
#(10, 10), (354, 354)
image.glLine(10*cx,10*cy,354*cx,354*cy)
#(10, 10), (191, 462)
image.glLine(10*cx,10*cy,191*cx,462*cy)
#(10, 10), (10, 510)
image.glLine(10*cx,10*cy,10*cx,510*cy)
image.glFinish()
image.glClear()

"""
File: lineas2.bmp
"""
image.setFileName("./testResults/lineas2.bmp")
#(790, 590), (790, 90)
image.glLine(790*cx,590*cy,790*cx,90*cy)
#(790, 590), (609, 138)
image.glLine(790*cx,590*cy,609*cx,138*cy)
#(790, 590), (446, 246)
image.glLine(790*cx,590*cy,446*cx,246*cy)
#(790, 590), (338, 409)
image.glLine(790*cx,590*cy,338*cx,409*cy)
#(790, 590), (290, 590)
image.glLine(790*cx,590*cy,290*cx,590*cy)
image.glFinish()
image.glClear()

"""
File: lineas3.bmp
"""
image.setFileName("./testResults/lineas3.bmp")
#(10, 590), (510, 590)
image.glLine(10*cx,590*cy,510*cx,590*cy)
#(10, 590), (462, 409)
image.glLine(10*cx,590*cy,462*cx,409*cy)
#(10, 590), (354, 246)
image.glLine(10*cx,590*cy,354*cx,246*cy)
#(10, 590), (191, 138)
image.glLine(10*cx,590*cy,191*cx,138*cy)
#(10, 590), (10, 90)
image.glLine(10*cx,590*cy,10*cx,90*cy)
image.glFinish()
image.glClear()

"""
File: lineas4.bmp
"""
image.setFileName("./testResults/lineas4.bmp")
#(790, 10), (790, 510)
image.glLine(790*cx,10*cy,790*cx,510*cy)
#(790, 10), (609, 462)
image.glLine(790*cx,10*cy,609*cx,462*cy)
#(790, 10), (446, 354)
image.glLine(790*cx,10*cy,446*cx,354*cy)
#(790, 10), (338, 191)
image.glLine(790*cx,10*cy,338*cx,191*cy)
#(790, 10), (290, 10)
image.glLine(790*cx,10*cy,290*cx,10*cy)
image.glFinish()
image.glClear()


"""
File: cubo.bmp
"""
image.setFileName("./testResults/cubo.bmp")
#(100, 100), (200, 100)
image.glLine(100*cx,100*cy,200*cx,100*cy)
#(100, 100), (100, 200)
image.glLine(100*cx,100*cy,100*cx,200*cy)
#(200, 100), (200, 200)
image.glLine(200*cx,100*cy,200*cx,200*cy)
#(150, 150), (250, 150)
image.glLine(150*cx,150*cy,250*cx,150*cy)
#(100, 200), (200, 200)
image.glLine(100*cx,200*cy,200*cx,200*cy)
#(150, 150), (150, 250)
image.glLine(150*cx,150*cy,150*cx,250*cy)
#(250, 150), (250, 250)
image.glLine(250*cx,150*cy,250*cx,250*cy)
#(150, 250), (250, 250)
image.glLine(150*cx,250*cy,250*cx,250*cy)
#(100, 100), (150, 150)
image.glLine(100*cx,100*cy,150*cx,150*cy)
#(100, 200), (150, 250)
image.glLine(100*cx,200*cy,150*cx,250*cy)
#(200, 100), (250, 150)
image.glLine(200*cx,100*cy,250*cx,150*cy)
#(200, 200), (250, 250)
image.glLine(200*cx,200*cy,250*cx,250*cy)
image.glFinish()
image.glClear()


"""
File: cuboIsometrico.bmp
"""
image.setFileName("./testResults/cuboIsometrico.bmp")
#(200, 200), (287, 250)
image.glLine(200*cx,200*cy,287*cx,250*cy)
#(200, 200), (113, 250)
image.glLine(200*cx,200*cy,113*cx,250*cy)
#(200, 200), (200, 300)
image.glLine(200*cx,200*cy,200*cx,300*cy)
#(287, 250), (287, 350)
image.glLine(287*cx,250*cy,287*cx,350*cy)
#(113, 250), (113, 350)
image.glLine(113*cx,250*cy,113*cx,350*cy)
#(200, 300), (287, 350)
image.glLine(200*cx,300*cy,287*cx,350*cy)
#(200, 300), (113, 350) 
image.glLine(200*cx,300*cy,113*cx,350*cy)
#(287, 350), (200, 400)
image.glLine(287*cx,350*cy,200*cx,400*cy)
#(113, 350), (200, 400)
image.glLine(113*cx,350*cy,200*cx,400*cy)

image.glFinish()
image.glClear()

"""
File: nes.bmp
"""
image.glCreateWindow(100, 100)
image.glViewPort(34,34,33,33)
image.setFileName("./testResults/nes.bmp")
cx = 1/32
cy = 1/32
#image.glClearColor(1,1,1)

image.glColor(1, 1, 1)
for y in range(2):
	image.glLine(-26*cx, (17-y)*cx, -20*cx, (17-y)*cx)
	image.glLine(20*cx, (17-y)*cx, 26*cx, (17-y)*cx)

	image.glLine(-20*cx, (13-y)*cx, -14*cx, (13-y)*cx)
	image.glLine(14*cx, (13-y)*cx, 20*cx, (13-y)*cx)


	image.glLine(-26*cx, (9-y)*cx, 26*cx, (9-y)*cx)

	image.glLine(-30*cx, (3-y)*cx, -26*cx, (3-y)*cx)
	image.glLine(26*cx, (3-y)*cx, 30*cx, (3-y)*cx)
	image.glLine(-18*cx, (3-y)*cx, 18*cx, (3-y)*cx)

	image.glLine(-30*cx, (7-y)*cx, -26*cx, (7-y)*cx)
	image.glLine(26*cx, (7-y)*cx, 30*cx, (7-y)*cx)
	image.glLine(-18*cx, (7-y)*cx, 18*cx, (7-y)*cx)

	image.glLine(-32*cx, (0-y)*cx, 32*cx, (0-y)*cx)

	image.glLine(-22*cx, (-4-y)*cx, 22*cx, (-4-y)*cx)
	image.glLine(-22*cx, (-7-y)*cx, 22*cx, (-7-y)*cx)


	image.glLine(-32*cx, (-4-y)*cx, -31*cx, (-4-y)*cx)
	image.glLine(31*cx, (-4-y)*cx, 32*cx, (-4-y)*cx)
	image.glLine(-32*cx, (-7-y)*cx, -31*cx, (-7-y)*cx)
	image.glLine(31*cx, (-7-y)*cx, 32*cx, (-7-y)*cx)

	image.glLine(-32*cx, (-10-y)*cx, -31*cx, (-10-y)*cx)
	image.glLine(31*cx, (-10-y)*cx, 32*cx, (-10-y)*cx)
	image.glLine(-22*cx, (-10-y)*cx, -19*cx, (-10-y)*cx)
	image.glLine(19*cx, (-10-y)*cx, 22*cx, (-10-y)*cx)

	image.glLine(-18*cx, (-13-y)*cx, -10*cx, (-13-y)*cx)
	image.glLine(10*cx, (-13-y)*cx, 18*cx, (-13-y)*cx)


image.glFinish()
image.glClear()



