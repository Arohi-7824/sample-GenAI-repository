import os
import csv
with open("db.csv","r") as file:
    for line in file:
        data=line.strip().split(",")
        print("Dear ",data[1],", your email is ",data[2],".",sep="")

with open("students.csv","w") as file:
    file.write("Name,Age,Grade\n")
    file.write("Alice,20,A\n")
    file.write("Bob,22,B\n")
    file.write("Charlie,19,C\n")

students=[
    ["name","age","grade"],
    ["Alice",20,"A"],
    ["Bob",22,"B"],
    ["Charlie",19,"C"]
]

with open("new_students.csv","w",newline="") as file:
    writer=csv.writer(file)
    for row in students:
        writer.writerow(row)

with open("new_students.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)