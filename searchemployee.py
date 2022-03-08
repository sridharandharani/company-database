import sqlite3
connection = sqlite3.connect("company.db")
getid = input("Enter the id :")

result = connection.execute("SELECT * FROM EMPLOYEE WHERE EMPID= " +getid)
for i in result:
    print("EMPId",i[0])
    print("empname",i[1])
    print("designation",i[2])
    print("salary", i[3])
    print("companyname",i[4])
    print("mobno",i[5])