import sqlite3
connection = sqlite3.connect("company.db")
delempid = input("enter the id :")
connection.execute("SELECT * FROM EMPLOYEE WHERE EMPID="+delempid)
connection.commit()
print("DELETED")