# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:40:22 2021

@author: Halby
"""
'employ management system'

'importing sys'
import sys

'declration of the guide function'
def Guide():
    print("-----------------------------------")
    print("please press")
    print("1 to Add Employee")
    print("2 to Remove Employee")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")
    print("-----------------------------------")
    Selection= int(input("Enter your choice: "))
    if Selection==1:
        Add()
    elif Selection==2:
        Remove()
    elif Selection==3:
        Promote()
    elif Selection==4:
        Display()
    elif Selection==5:
        print("Thanks for using my program <3 ")
        print("Exitting...")
        sys.exit()
    else:
        print("Enter a valid value!")
        Guide()
    
 
'declration of adding function'
def Add():
    ID= int(input("Enter employee ID: "))
    Name= input("Enter employee name: ")
    Post= input("Enter employee post: ")
    Salary= float(input("Enter employee salary: "))
    Employee= {"ID": ID, "Name": Name, "Post": Post, "Salary": Salary}
    EmployeesArray.append(Employee)    
    print("Employee has been added successfully!")
    Guide()
    
'declration of removing function'  
def Remove():
    ID= int(input("Enter employee ID: "))
    EmployeesArray.pop(Find(ID))
    print("Employee has been removed successfully!")
    Guide()
  
  
'declration of promoting function'
def Promote():
    ID= int(input("Enter employee ID: "))
    i=Find(ID)
    NewPost= input("Enter employee's new post: ")
    EmployeesArray[i]["Post"] = NewPost
    NewSalary= float(input("Enter employee's new salary: "))
    EmployeesArray[i]["Salary"] = NewSalary
    print("Employee has been promoted successfully!")
    Guide()

'declration of displaying function'
def Display():
    if len(EmployeesArray) == 0:
        print("There is no employees")
        Guide()
    else:
        for i in range(0,len(EmployeesArray)):
            print("-----------------------------------")
            print ("ID: ", EmployeesArray[i]["ID"])
            print ("Name: ", EmployeesArray[i]["Name"])
            print ("Post: ", EmployeesArray[i]["Post"])
            print ("Salary: ", EmployeesArray[i]["Salary"])
        Guide()
    
'declration of find function'
def Find(ID):
    if len(EmployeesArray) == 0:
        print("There is no employees")
        Guide()
    else:
        for i in range(0,len(EmployeesArray)):
            if EmployeesArray[i]["ID"] == ID:
                return i
        print("cannot find this ID")
        Guide()
    
'initial data'
EmployeesArray= [{"ID": 1, "Name": "Halby", "Post": "student", "Salary": 1000.0}]

'program starting'
print("This is employ management system")
Guide()


    

    
    

    
    
    
    