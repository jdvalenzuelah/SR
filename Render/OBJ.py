
class OBJ(object):
	"""
	Class representing an .obj file
	"""

	def __init__(self, filename):
		"""
		Constructor de la clase
		"""
		self.__vertex = []
		self.__faces = []
		self.__nvertex = []
		self.__filename = filename
		self.__materials = None

	def load(self):
		"""
		Loads the objfile
		"""
		file = open(self.__filename, "r")
		for line in file.readlines():
			line = line.rstrip().split(" ")
			if line[0] == "mtllib":
				mtlFile = MTL(line[1])
				if mtlFile.isFileOpened():
					mtlFile.load()
					self.__materials = mtlFile.materials
			elif line[0] == "usemtl":
				if self.__materials:
					print(self.__materials[line[1]])
			elif line[0] == "v":
				line.pop(0)
				i = 1 if line[0] == "" else 0
				self.__vertex.append((float(line[i]), float(line[i+1]), float(line[i+2])))
			elif line[0] == "vn":
				line.pop(0)
				i = 1 if line[0] == "" else 0
				self.__nvertex.append((float(line[i]), float(line[i+1]), float(line[i+2])))
			elif line[0] == "f":
				line.pop(0)
				face = []
				for i in line:
					i = i.split("/")
					face.append((int(i[0]), int(i[-1])))
				self.__faces.append(face)
				face = []

	def getMaterials(self):		
		"""
		"""
		return self.__materials

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

class MTL(object):
	"""
	class representing .mtl file
	"""

	def __init__(self, filename):
		self.__filename = filename
		self.__file = None
		self.materials = {}
		self.readMTLFile()

	def readMTLFile(self):
		"""
		Reads an .mtl file if found
		"""
		try:
			self.__file = open(self.__filename, "r")
			self.__mtlFile = True
		except:
			self.__mtlFile = False

	def isFileOpened(self):
		"""
		Verifies that the mtl file was found
		"""
		return self.__mtlFile

	def load(self):
		"""
		Parse the .mtl file and stores the materials
		"""
		if self.isFileOpened():
			currentMat = None
			ac, dc, sc, ec, t, s, i, o = 0, 0, 0, 0, 0, 0, 0, 0
			for line in self.__file.readlines():
				line = line.split(" ")
				if line[0] == "newmtl":
					currentMat = line[1].rstrip()
				elif line[0] == "Ka":
					ac = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "Kd":
					dc = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "Ks":
					sc = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "Ke":
					ec = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "d" or line[0] == "Tr":
					t = (float(line[1]), line[0])
				elif line[0] == "Ns":
					s = float(line[1])
				elif line[0] == "illum":
					i  = int(line[1])
				elif line[0] == "Ni":
					o = float(line[1])
				elif currentMat:
					self.materials[currentMat] = Material(currentMat, ac, dc, sc, ec, t, s, i, o)	
			if currentMat not in self.materials.keys():
				self.materials[currentMat] = Material(currentMat, ac, dc, sc, ec, t, s, i, o)	

class Material(object):
	"""
	"""
	def __init__(self, name, ac, dc, sc, ec, t, s, i, o):
		"""
		Material stores:
			- ambient color
			- difuse color
			- emissive coeficient
			- transparency
			- shininess
			- illumination
			- optical density
		"""
		self.name = name.rstrip()
		self.ambientColor = ac
		self.difuseColor = dc
		self.specularColor = sc
		self.emissiveCoeficient = ec
		self.transparency = t
		self.shininess = s
		self.illumination = i
		self.opticalDensity = o		
