import pickle
import sys
import os
import re
sys1=sys.argv[1]
sys2=sys.argv[2]
username="asm"  
password="asm123"
i=1
list1=[]
#list2=[]
#dict1={}
if((username==sys1)&(password==sys2)):
	
	while True:
		data=raw_input("mysql>")
		str1=data
		if str1:
			reg1=re.search(r'(create database.*)',str1,re.I|re.M)
			if reg1:
				dbname=str(reg1.group())
				#print dbname
				l2=dbname.split()
				#print l2	
				#databasename=str(l2[2])
				dbname1=str(l2[2])
				dbname1=dbname1.strip(';')
				#print "table name is",databasename
				path ='/home/anvitha/Documents/picklefolder' 
				if not os.path.exists(dbname1):
    					os.makedirs(dbname1)
					print "query OK, 1 row affected "
				#os.mkdir('databasename')
			#while True:
					#str2 = raw_input("mysql>")
					#if str2:
			reg2=re.search(r'(create table .*)',str1,re.I|re.M)
				#reg2=re.search(r'()')
			if reg2:			
				a=str(reg2.group())
				b=a.split()
				#print b[2]
				c=str(b[2])
				c=c.strip(';') 
				#b=a.strip(create )
				path ="/home/anvitha/Documents/picklefolder/"+str(dbname1)+"/" 
				if not os.path.exists(dbname1):
    					os.makedirs(dbname1)
					filename = c + '.txt'
					f=open(os.path.join(path, filename), 'wb')
					print "query OK, 0 row affected"
			reg3=re.search(r'(insert the values.*)',str1,re.I|re.M)
			if reg3:
				f=open("/home/anvitha/Documents/pickfolder/table.txt",'w')
				inp=input("enter the number of elements you want to insert")
				for i in range(inp):
					data=raw_input("enter the data")
					list1.append(data)
					print list1
					pickle.dump(list1,f)
					f.close()
			reg4=re.match('select',str1,re.I|re.M)
			if reg4:
				f=open("/home/anvitha/Documents/pickfolder/table.txt",'r')
				list1 = pickle.load(f)
				print list1
				f.close()
else:
	print "authorization failed"
			


		
