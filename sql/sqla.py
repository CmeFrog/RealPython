# Create SQL CE database
# First create 0 byte file (new.sdf) with UlttraEdit

import adodbapi

connStr = ("Provider=Microsoft.SQLSERVER.CE.OLEDB.3.5;Data Source={}".format("new.sdf"))
conn = adodbapi.connect(connStr)
dbCursor = conn.cursor()
dbCursor.execute("""CREATE TABLE population
	(city NVarchar(255), state NVarchar(255), population Integer)
	""")
conn.commit()
dbCursor.close()
conn.close()

