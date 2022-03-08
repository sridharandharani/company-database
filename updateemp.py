import sqlite3
connection = sqlite3.connect("company.db")
getempid = input("Enter the id to be updated :")
getname = input("Enter the name :")
getdesignation = input("Enter the designation :")
getsalary = input("Enter the salary :")
getcompanyname = input("Enter the company name :")
getmobno = input("Enter the mobno  :")
connection.execute("UPDATE EMPLOYEE SET \
EMPNAME ='"+getname+"',DESIGNATION = '"+getdesignation+"',SALARY = "+getsalary+",COMPANYNAME = '"+getcompanyname+"',MOBNO = "+getmobno+" \
WHERE EMPID= " +getempid)
connection.commit()
print("updated sucessfully")

