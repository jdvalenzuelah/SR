from SR import SR
from random import random
image = SR()
image.glInit()
image.glCreateWindow(800, 800)
image.glViewPort(0,0,800,800)
image.setFileName("objTest.bmp")
image.glClear()
image.glFinish()
image.loadOBJ("bb8.obj", translate=(0.15,0,0), scale=(0.45,0.45,0.45), fill=True)
image.glFinish()
