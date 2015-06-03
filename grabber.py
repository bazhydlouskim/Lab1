#LAB1 Python starter code
#Based upon manual at http://mysql-python.sourceforge.net/MySQLdb.html

#imports go here
import MySQLdb
#import _mysql

#code goes here

db = MySQLdb.connect(host="localhost",user="root",passwd="FakePassWord",db="wine")
db.query("""SELECT * FROM wine;""")
r = db.store_result()
nR = r.num_rows()
while(nR > 0):
	print(r.fetch_row())
	nR = nR - 1
db.close()