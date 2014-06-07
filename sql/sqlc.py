#Insert data into SQL CE table
import adodbapi

# insert multiple records using a tuple
cities = [('Boston', 'MA', 600000), ('Houston', 'TX', 2100000), ('Phoenix', 'AZ', 1500000)]
connStr = ("Provider=Microsoft.SQLSERVER.CE.OLEDB.3.5;Data Source={}".format("new.sdf"))
with adodbapi.connect(connStr) as conn:
    dbCursor = conn.cursor()
    for city in cities:
        dbCursor.execute("INSERT INTO population VALUES('{}', '{}', {})".format(city[0], 
        	city[1], city[2]))
