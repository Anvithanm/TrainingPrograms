class mat:
	def __init__(self,x):
		self.m = []
		for i in range (x):
			self.m.append([1]*x)
matrix = mat(4)
matrix.m
print (matrix.m)
