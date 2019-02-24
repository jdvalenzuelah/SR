
class OBJ(object):

	def __init__(self, filename):
		"""
		Constructor de la clase
		"""
		self.__vertex = []
		self.__faces = []
		self.__nvertex = []
		self.__filename = filename

	def load(self):
		"""
		Loads the objfile
		"""
		file = open(self.__filename, "r")
		cont = 0
		for line in file.readlines():
			 cont += 1
			 if line[0] == "v" and line[1] == " ":
			 	v = line.strip().split(" ")
			 	v.pop(0)
			 	i = 1 if v[0] == "" else 0
			 	self.__vertex.append((float(v[i]), float(v[i+1]), float(v[i+2])))
			 if line[0] == "v" and line[1] == "n":
			 	vn = line.strip().split(" ")
			 	vn.pop(0)
			 	i = 1 if vn[0] == "" else 0
			 	self.__nvertex.append((float(vn[i]), float(vn[i+1]), float(vn[i+2])))
			 if line[0] == "f":
			 	f = line.strip().split(" ")
			 	f.pop(0)
			 	face = []
			 	for i in f:
			 		i = i.split("/")
			 		face.append((int(i[0]), int(i[-1])))
			 	self.__faces.append(face)
			 	face = []
		file.close()

	def getFaceList(self):
		"""
		faces getter
		"""
		return self.__faces

	def getVertexList(self):
		"""
		getVerxtex
		"""
		return self.__vertex

	def getVertexNormalList(self):
		"""
		vertex normal getter
		"""
		return self.__nvertex