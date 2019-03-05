# UVG
from Render.SR import SR
from random import random
image = SR()
image.glInit()
image.glCreateWindow(800, 800)
image.glViewPort(0,0,800,800)
image.setFileName("./testResults/objTest.bmp")
image.loadOBJ("./models/bb8.obj", translate=(0.15,-0.4,0), scale=(0.4,0.4,0.4), fill=True)
image.glRenderZBuffer(filename="./testResults/zbufferBB8.bmp")
image.glFinish()
