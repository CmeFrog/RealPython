#Insert data into SQL CE table
import adodbapi

connStr = ("Provider=Microsoft.SQLSERVER.CE.OLEDB.3.5;Data Source={}".format("new.sdf"))
with adodbapi.connect(connStr) as conn:
    dbCursor = conn.cursor()
    dbCursor.execute("INSERT INTO population VALUES('Chicago', 'IL', 4600000)")
    dbCursor.execute("INSERT INTO population VALUES('Los Angeles', 'CA', 6400000)")

