import adodbapi

connStr = ("Provider=Microsoft.SQLSERVER.CE.OLEDB.3.5;Data Source={}".format(r"E:\Code\__C#\Projects\Testing\Testing.sdf"))
conn = adodbapi.connect(connStr)
dbCursor = conn.cursor()
sql = "SELECT * FROM AutoInc"
#sql = "SELECT * FROM AutoInc WHERE RecordID = 2"
# RecordID = 1, TextVal = "Identity Test"
# RecordID = 2, TextVal = "Identity Test2"
# RecordID = 3, TextVal = "Identity Test3"
# RecordID = 4, TextVal = "Identity Test3"
dbCursor.execute(sql)
results = dbCursor.fetchall()
for r in results:
    print r
