#Insert data into SQL CE table
import adodbapi

connStr = ("Provider=Microsoft.SQLSERVER.CE.OLEDB.3.5;Data Source={}".format("new.sdf"))
conn = adodbapi.connect(connStr)
dbCursor = conn.cursor()
dbCursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
dbCursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")
conn.commit()
dbCursor.close()
conn.close()

