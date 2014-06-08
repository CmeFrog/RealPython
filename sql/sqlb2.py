# Insert data into SQL CE table
# error in table name should be population
# first run with blank except only
# this returns error class to make specific exception
import adodbapi
import sys

connStr = ("Provider=Microsoft.SQLSERVER.CE.OLEDB.3.5;Data Source={}".format("new.sdf"))
conn = adodbapi.connect(connStr)
dbCursor = conn.cursor()
try:
    dbCursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
    dbCursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")
# specific error class 
except adodbapi.apibase.DatabaseError:
	print "Oops"
# prints error class
except:
	print "Unexpected error:", sys.exc_info()[0]
conn.commit()
dbCursor.close()
conn.close()

