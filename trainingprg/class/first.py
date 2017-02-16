
lis=[]
n=int(input("enter the range\n"))#10

for n in range(n):
	n=int(input("enter the no"))
	lis.append(n)
print lis

print max(lis)

lis.remove(max(lis))
sm=max(lis)
print sm
 
