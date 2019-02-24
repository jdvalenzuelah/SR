from SR import SR
image = SR()
image.glInit()
image.glCreateWindow(800, 800)
image.glViewPort(0,0,800,800)
image.setFileName("objTest.bmp")
image.glClear()
image.glFinish()
image.loadOBJ("cc5.obj", translate=(0,0,0), scale=(0.25,0.25,0.25), fill=True)
image.glFinish()

image.glRenderZBuffer(filename="zbuffer.bmp")
