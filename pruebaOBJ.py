# UVG
from Render.SR import SR
import sys

def bb8():
	image = SR()
	image.glInit()
	image.glCreateWindow(800, 800)
	image.glViewPort(0,0,800,800)
	image.setFileName("./testResults/bb8.bmp")
	image.loadOBJ("./models/bb8.obj", translate=(0,-0.25,0), scale=(0.47,0.47,0.47), fill=True)
	image.glFinish()

def earth():
	image = SR()
	image.glInit()
	image.glCreateWindow(800, 800)
	image.glViewPort(0,0,800,800)
	image.setFileName("./testResults/earth.bmp")
	image.loadOBJ("./models/earth.obj", translate=(0,-0.25,0), scale=(0.10,0.10,0.10), fill=True)
	image.glFinish()

def face():
	image = SR()
	image.glInit()
	image.glCreateWindow(800, 800)
	image.glViewPort(0,0,800,800)
	image.setFileName("./testResults/face.bmp")
	image.loadOBJ("./models/model.obj", translate=(0,0,0), scale=(0.95,0.95,0.95), fill=True)
	image.glRenderTextureGrid(filename="./testResults/faceTexture.bmp", newfile=True, translate=(-0.5,-0.5), scale=(1.5,1.5)).glFinish()
	image.glFinish()

if __name__ == "__main__":
	args = sys.argv[1] if len(sys.argv) > 1 else ""
	if args == "bb8":
		bb8()
	elif args == "face":
		face()
	else:
		print("invalid args")
