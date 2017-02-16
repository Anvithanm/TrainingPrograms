inp_put = []
while True:
	b = raw_input()
	inp_put.append(b)
	a='\t'.join(inp_put)
	#a.swapcase()
	if b == 'exit':
		break
c=a.swapcase()
print c
	

