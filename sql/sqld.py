# Create SQL CE database
# First create 0 byte file (new.sdf) with UlttraEdit

import adodbapi
import csv

connStr = ("Provider=Microsoft.SQLSERVER.CE.OLEDB.3.5;Data Source={}".format("new.sdf"))
with adodbapi.connect(connStr) as conn:
    dbCursor = conn.cursor()
    dbCursor.execute("""CREATE TABLE employees
	    (firstname NVarchar(255), lastname NVarchar(255))
	    """)
    csvFile = open(r"E:\Code\__Python\RealPython\book2-exercises-master\sql\employees.csv",
     "rU")
    csvReader = csv.reader(csvFile)
    for firstName, lastName in csvReader:
        dbCursor.execute("INSERT INTO employees VALUES('{}', '{}')".format(firstName, 
        	lastName))
    csvFile.close()