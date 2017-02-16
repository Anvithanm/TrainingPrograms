class matrix:
	def __init__(self,array):
		self.array=array
	def __add__(self,other):
		if len(self.array) == len(other.array):
			row_len1 = self.array[0]
			row_len2 = other.array[1]
			for row in self.array:
				if row_len1 != len(row):
					return none
			for row in other.array:
				if row_len2!=len(row)
					return none
		newmatrix=[]
		for i in range(self.array):
			row = []
			for j in range(self.array[0]):
				row.append(self.array[i][j]+other.array[i][j])
				newmatrix
			
