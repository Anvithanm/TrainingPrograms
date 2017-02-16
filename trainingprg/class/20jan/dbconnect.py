import MySQLdb
host = 'localhost'
username = 'root'
passwd = 'ids123'
db = 'mail'
db_con=MySQLdb.connect(host,username,passwd,db)
db_cur=db_con.cursor()
sql="select * from info"
print db_cur.execute(sql)

