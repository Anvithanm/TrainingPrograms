#import smtplib
#import getpass
import MySQLdb
#import sys
host = 'localhost'
username = 'root'
passwd = 'ids123'
db = 'mail'
db_con=MySQLdb.connect(host,username,passwd,db)
#db_cur=db_con.cursor()
db_cur=db_con.cursor(MySQLdb.cursors.DictCursor)
sql="select * from info"
db_cur.execute(sql)
sql1=db_cur.fetchall()
print sql1
for i in sql1:
	print i
	a="{id} {name}".format(**i)
	print a
#host = "smtp.gmail.com"
#port = 587
#server = smtplib.SMTP(host,port)
#server.ehlo()
#server.starttls()
#server.ehlo()
#username='anvithanm22@gmail.com'
#password=getpass.getpass()
#server.login(username,password)
#to=sys.argv[1]
#sub=sys.argv[3]
#mes=sys.argv[2]
#with open(mes,'r') as f:
	#f1=f.read()
	#message="subject:%s\n\n%s"%(sub,f1)
	#server.sendmail(username,to,message)

