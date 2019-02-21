from SR import SR
image = SR()
image.glInit()
image.glCreateWindow(800, 800)
image.glViewPort(0,0,799,799)
image.loadOBJ("bb8.obj", translate=(0.8,-0.25), scale=(0.5,0.5))
image.setFileName("objTest.bmp")
image.glFinish()
