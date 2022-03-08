import sqlite3
connection = sqlite3.connect("company.db")

result = connection.execute("SELECT * FROM EMPLOYEE ")
for i in result:
    print("EMPId",i[0])
    print("empname",i[1])
    print("designation",i[2])
    print("salary", i[3])
    print("companyname",i[4])
    print("mobno",i[5])