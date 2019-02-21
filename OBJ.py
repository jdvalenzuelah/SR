
class OBJ(object):

	def __init__(self, filename):
		"""
		Constructor de la clase
		"""
		self.__vertexs = []
		self.__faces = []
		self.__filename = filename

	def load(self):
		"""
		Loads the objfile
		"""
		file = open(self.__filename, "r")
		for line in file.readlines():
			 if line[0] == "v" and line[1] != "n":
			 	v = line.strip().split(" ")
			 	v.pop(0)
			 	i = 1 if v[0] == "" else 0
			 	self.__vertexs.append((float(v[i]), float(v[i+1])))
			 if line[0] == "f":
			 	f = line.strip().split(" ")
			 	f.pop(0)
			 	face = []
			 	for i in f:
			 		i = i.split("/")
			 		face.append(int(i[0]))
			 	self.__faces.append(face)
			 	face = []
		file.close()

	def getFaces(self):
		"""
		faces getter
		"""
		return self.__faces

	def getVertexs(self):
		"""
		getVerxtex
		"""
		return self.__vertexs