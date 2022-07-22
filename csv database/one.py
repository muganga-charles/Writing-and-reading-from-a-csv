import csv
def data_entry():
    students = int(input("Enter number of students: "))
    count = 0
    with open("students.csv", "a") as f:
        for i in range(students):
            reader = csv.DictWriter(f, fieldnames=["Reg", "Name", "Proctor"])
            registration = input("Enter your registration number: ")
            name = input("Enter your name: ")
            proctor = input("Enter your proctor: ")
            reader.writerow({"Reg": registration,"Name": name, "Proctor": proctor})
            count += 1
    print("{} students added".format(count))
  