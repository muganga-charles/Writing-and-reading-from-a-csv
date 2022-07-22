
from csv import DictReader
def add_student():  
    registration = input("Enter your registration number: ")
    file = open("students.csv", "r", encoding="utf-8")
    reader = DictReader(file)
    for row in reader:
        if registration in row['Reg_no']:
            print("You are logged in")
            print("Welcome to the Student Portal")
            print("Name: {} \n" "Registration Number: {}".format(row['Name'],row['Reg_no']))
    if registration not in row['Reg_no']:
        print("You are not logged in")
        print("Please try again")
        add_student()     
    file.close()
    
