from Render.BMP import BMP

class Texture(object):
	"""
	"""

	def __init__(self, filename):
		"""
		"""
		self.__filename = filename
		self.__text = None
		self.load()

	def load(self):
		"""
		"""
		self.__text = BMP(0, 0)
		try:
			self.__text.load(self.__filename)
		except:
			self.__text = None

	def write(self):
		"""
		"""
		self.__text.write(self.__filename[:len(self.__filename)-4]+"text.bmp")

	def getColor(self, tx, ty, intensity=1):
		"""
		"""
		x = int(ty*self.__text.width)
		y = int(tx*self.__text.height)

		#self.__text.color(int(intensity*self.__text.framebuffer[x][y][0]),int(intensity*self.__text.framebuffer[x][y][1]), int(intensity*self.__text.framebuffer[x][y][2]))
		return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.__text.framebuffer[y][x]))

	def isTextured(self):
		return True if self.__text else False
		