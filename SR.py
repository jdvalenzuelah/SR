#Universidad del Valle de Guatemala
#Josue Valenzuela 171001

from BMP import BMP
from OBJ import OBJ
import math

class SR(object):

	def glInit(self):
		"""
		Inicializa el rendering
		"""
		self.__image = BMP(0,0)
		self.__viewPortStart = (0,0)
		self.__viewPortSize = (0,0)
		self.__color = self.__image.color(255,255,255)
		self.__filename = "output.bmp"

	def glCreateWindow(self, width, height):
		"""
		Define el tamano de la ventana sobre la cual se creara ña imagen
		"""
		self.__image = BMP(width, height)
		self.__viewPortSize = (width, height)

	def glViewPort(self, x, y, width, height):
		"""
		Define el tamano de la imagen qu se utilizara
		"""
		self.__viewPortStart = (x, y)
		self.__viewPortSize = (width,height)

	def glClear(self):
		"""
		Cambia todo el color de la ventana el color predeterminado
		"""
		self.__image.clear()

	def glClearColor(self, r, g, b):
		"""
		Cambia el color de la ventana al color ingresado por medio de rgb
		"""
		self.__image.clear(int(255*r), int(255*g), int(255*b))

	def glVertex(self, x, y):
		"""
		Cambia de color un pixel del viewport
		"""
		viewPortX = int(self.__viewPortSize[0] * (x+1) * (1/2) + self.__viewPortStart[0])
		viewPortY = int(self.__viewPortSize[1] * (y+1) * (1/2) + self.__viewPortStart[1])
		self.__image.point(viewPortX, viewPortY, self.__color)

	def  glColor(self, r, g, b):
		"""
		Cambia el color predeterminado.
		"""
		self.__color = self.__image.color(int(255*r), int(255*g), int(255*b))

	def glFinish(self):
		"""
		Escribe archivo bmp final
		"""
		self.__image.write(self.__filename)

	def glLine(self, xo, yo, xf, yf):
		"""
		Dibuja una linea
		"""
		x1 = int(self.__viewPortSize[0] * (xo+1) * (1/2) + self.__viewPortStart[0])
		y1 = int(self.__viewPortSize[1] * (yo+1) * (1/2) + self.__viewPortStart[1])
		x2 = int(self.__viewPortSize[0] * (xf+1) * (1/2) + self.__viewPortStart[0])
		y2 = int(self.__viewPortSize[1] * (yf+1) * (1/2) + self.__viewPortStart[1])
		dy = abs(y2 - y1)
		dx = abs(x2 - x1)
		steep = dy > dx
		if steep:
			x1, y1 = y1, x1
			x2, y2 = y2, x2
		if (x1 > x2):
			x1, x2 = x2, x1
			y1, y2 = y2, y1
		dy = abs(y2 - y1)
		dx = abs(x2 - x1)
		offset = 0
		threshold = dx
		y = y1
		for x in range(x1, x2 + 1):
			if steep:
				self.__image.point(y, x, self.__color)
			else:
				self.__image.point(x, y, self.__color)

			offset += dy * 2
			if offset >= threshold:
				y +=1 if y1 < y2 else -1
				threshold += 2 * dx
	
	def setFileName(self, filename):
		"""
		Definimos el nombre del donde se guardan los archivos.
		"""
		self.__filename = filename

	def loadOBJ(self, filename, translate=(0, 0), scale=(1, 1)):
		"""
		cargar OBJ file, wireframe
		"""
		obj = OBJ(filename)
		obj.load()
		vertex = obj.getVertexs()
		faces = obj.getFaces()
		for face in faces:
			cooList = []
			for vertexN in face:
				coo = ((vertex[vertexN-1][0] + translate[0]) * scale[0], (vertex[vertexN-1][1] + translate[1]) * scale[1])
				cooList.append(coo)
			self.glPolygon(cooList)
			cooList = []

	def glPolygon(self, vertexList):
		"""
		poligono
		"""
		for i in range(len(vertexList)):
			if i == len(vertexList)-1:
				st = vertexList[i]
				fi = vertexList[0]
			else:
				st = vertexList[i]
				fi = vertexList[i+1]
			self.glLine(st[0], st[1], fi[0], fi[1])

	def glFilledPolygon(self, vertexList, fillColor):
		startX = sorted(vertexList, key=lambda tup: tup[0])[0][0]
		finishX = sorted(vertexList, key=lambda tup: tup[0], reverse = True)[0][0]

		startY = sorted(vertexList, key=lambda tup: tup[1])[0][1]
		finishY = sorted(vertexList, key=lambda tup: tup[1], reverse=True)[0][1]

		startX = int(self.__viewPortSize[0] * (startX+1) * (1/2) + self.__viewPortStart[0])
		finishX = int(self.__viewPortSize[0] * (finishX+1) * (1/2) + self.__viewPortStart[0])

		startY = int(self.__viewPortSize[0] * (startY+1) * (1/2) + self.__viewPortStart[0])
		finishY = int(self.__viewPortSize[0] * (finishY+1) * (1/2) + self.__viewPortStart[0])

		self.glPolygon(vertexList)

		for x in range(startX, finishX+1):
			for y in range(startY, finishY+1):
				isInside = self.glPointInPolygon(self.norX(x), self.norY(y), vertexList)
				if isInside:
					self.__image.point(x, y, self.__color)


	def norX(self, x):
		"""
		Normalizar coor
		"""
		norX = ((2*x)/self.__viewPortSize[0]) - self.__viewPortStart[0] - 1
		return norX

	def norY(self, y):
		"""
		Normalizar coor
		"""
		norY = ((2*y)/self.__viewPortSize[1]) - self.__viewPortStart[1] - 1
		return norY

	def glPointInPolygon(self,x, y, vertexList):
		"""
		Verifica si un punto (x, y) se encuentra dentro de un poligono (basado en sus vertices)
		Algoritmo obtenido de: http://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html
		"""
		counter = 0
		p1 = vertexList[0]
		n = len(vertexList)
		for i in range(n+1):
			p2 = vertexList[i % n]
			if(y > min(p1[1], p2[1])):
				if(y <= max(p1[1], p2[1])):
					if(p1[1] != p2[1]):
						xinters = (y-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1])+p1[0]
						if(p1[0] == p2[0] or x <= xinters):
							counter += 1
			p1 = p2
		if(counter % 2 == 0):
			return False
		else:
			return True
