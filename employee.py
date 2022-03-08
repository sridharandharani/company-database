# create a new python project which has employee project for reading employee id employee name designation salary company name mobile number to the data base company
import sqlite3

connection = sqlite3.connect("company.db") #creating a database

connection.execute(''' CREATE TABLE EMPLOYEE(
                       EMPID INTEGER PRIMARY KEY AUTOINCREMENT,
                       EMPNAME TEXT,
                       DESIGNATION TEXT,
                       SALARY INTEGER,
                       COMPANYNAME TEXT,
                       MOBNO INTEGER
);''')
print("table created")

get_empname = input("Enter the name :")
get_designation = input("Enter the designation :")
get_salary = input("Enter the salary :")
get_companyname = input("Enter the company name :")
get_mobno = input("Enter the mobile no :")

connection.execute(" INSERT INTO EMPLOYEE(EMPNAME,DESIGNATION,SALARY,COMPANYNAME,MOBNO) \
 VALUES('"+get_empname+"','"+get_designation+"',"+get_salary+",'"+get_companyname+"',"+get_mobno+")")# inserting values in table
connection.commit()
connection.close()
print("Inserted sucessfully")