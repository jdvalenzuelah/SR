from SR import SR
image = SR()
image.glInit()
image.glCreateWindow(800, 800)
image.glViewPort(0,0,800,800)
image.setFileName("objTest.bmp")
image.glClear()
image.glFinish()
image.loadOBJ("bb83.obj", translate=(1,0,0), scale=(0.4,0.4,0.4), fill=True)
image.glFinish()

image.glRenderZBuffer(filename="zbuffer.bmp")
