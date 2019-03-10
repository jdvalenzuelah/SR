# UVG
from Render.SR import SR
from Render.Texture import Texture
from random import random
import sys

def bb8():
	image = SR()
	image.glInit()
	image.glCreateWindow(800, 800)
	image.glViewPort(0,0,800,800)
	image.setFileName("./testResults/bb8.bmp")
	image.loadOBJ("./models/bb8.obj", translate=(0,-0.25,0), scale=(0.47,0.47,0.47), fill=True)
	image.glFinish()

def ico():
	image = SR()
	image.glInit()
	image.glCreateWindow(800, 800)
	image.glViewPort(0,0,800,800)
	image.setFileName("./testResults/ico.bmp")
	image.loadOBJ("./models/test.obj", translate=(0,-0.25,0), scale=(0.47,0.47,0.47), fill=True, textured="./models/text.bmp")
	image.glRenderTextureGrid(filename="./testResults/icoText.bmp").glFinish()
	image.glFinish()

def earth():
	image = SR()
	image.glInit()
	image.glCreateWindow(800, 800)
	image.glViewPort(0,0,800,800)
	image.setFileName("./testResults/earth.bmp")
	image.loadOBJ("./models/earth.obj", translate=(0,-0.25,0), scale=(0.10,0.10,0.10), fill=True,)
	image.glFinish()

def face():
	image = SR()
	image.glInit()
	image.glCreateWindow(800, 800)
	image.glViewPort(0,0,800,800)
	image.setFileName("./testResults/face.bmp")
	image.loadOBJ("./models/model.obj", translate=(0,0,0), scale=(0.95,0.95,0.95), fill=True, textured=False)
	image.glRenderTextureGrid(filename="./testResults/faceTexture.bmp", newfile=True, translate=(-0.5,-0.5), scale=(1.5,1.5)).glFinish()
	image.glFinish()

def face2():
	image = SR()
	image.glInit()
	image.glCreateWindow(800, 800)
	image.glViewPort(0,0,800,800)
	image.setFileName("./testResults/face.bmp")
	image.loadOBJ("./models/model.obj", translate=(0,0,0), scale=(0.95,0.95,0.95), fill=False)
	image.glFinish()

def testBary():
	image = SR()
	image.glInit()
	return image.barycentric((0,0), (2,0), (1,2), 0.5, 0.1)

def testText():
	test = Texture("./models/model.bmp")
	test.load()
	test.write()

def generateText():
	image = SR()
	image.glInit()
	image.glCreateWindow(1024, 1024)
	#image.glViewPort(0,0,1024,1024)
	image.setFileName("./models/text.bmp")
	for i in range(4):
		for x in range(1024):
			if x%1024==0:
				image.glColor(random(), random(), random())
			for y in range(512*i,512*(i+1)):
				image.glVertex(image.norX(x), image.norY(y))
	

	image.glFinish()



if __name__ == "__main__":
	args = sys.argv[1] if len(sys.argv) > 1 else ""
	if args == "bb8":
		bb8()
	elif args == "face":
		face()
	elif args == "text":
		testText()
	elif args == "face2":
		face2()
	elif args == "bary":
		print(testBary())
	elif args == "ico":
		ico()
	elif args == "gen":
		generateText()
	else:
		print("invalid args")
