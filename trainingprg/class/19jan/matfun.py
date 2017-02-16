def matrix(a,b):
	res = []
	for i in range(a):
		row = []
	for k in range(b):
		for j in range(len(a[0])):
			row.append(a[i][j]+b[i][j])
		res.append(row)
		return res
matrix(3,3)
