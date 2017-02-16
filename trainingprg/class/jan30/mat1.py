class Matrix:
	def __init__(self):
		self.mat1=[]
		self.mat2=[]
		self.ans=[]
		self.asub=[]
	def matadd(self):
		#if len(self.array) == len(other.array):
		for i in range(num_row):
			row=[]
			for j in range(num_column):
				c=input()
				row.append(c)
			self.mat1.append(row)
		print "the matrix1 is :",self.mat1
			#row_len1=self.array[0]
			#row_len2=other.array[1]
		for i in range(num_row2):
			row2=[]
			for j in range(num_column2):
				c2=input()
				row2.append(c2)
			self.mat2.append(row2)
		print "the matrix2 is:",self.mat2
		if len(self.mat1) == len(self.mat2):
			for i in range(len(self.mat1)):
				row3=[]
				rowa=[]
				for j in range(len(self.mat2[0])):
					row3.append(self.mat1[i][j]+self.mat2[i][j])
					rowa.append(self.mat1[i][j] - self.mat2[i][j])
				self.ans.append(row3)
				self.asub.append(rowa)
			print "addition of matrix",self.ans
			print "substraction of matrix",self.asub
		if len(self.mat1[0]) == len(self.mat2):
			for i in range(len(self.mat1)):
				row4=[]
				for j in range(len(self.mat2[0])):
					row4.append(self.mat1[i][j] * self.mat2[i][j])
				self.ans.append(row4)
			print "multiplication of matrix",self.ans
			
				

	
num_row = input()
num_column = input()
num_row2 = input()
num_column2 = input()
#mat=[]
#a=matrix(num_row)
#b=matrix(num_column)
#print a+b
#for i in range(num_row):
	#row=[]
	#for j in range(num_column):
		#cell=input()
		#row.append(cell)
		#mat.append(row)
a=Matrix()
a.matadd()

