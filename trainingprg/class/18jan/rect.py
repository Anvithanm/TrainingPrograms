class A:
	def __init__(self,l,b):
		self.l=l
		self.b=b
	def area(self):
		c = self.l * self.b
		return c
	def perimeter(self):
		d = 2*(self.l + self.b)
		return d
ar=A(1,2)
print ar.area()
print ar.perimeter()
