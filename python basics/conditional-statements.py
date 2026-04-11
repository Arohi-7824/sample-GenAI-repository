name_str = input("Hi what is your name?")
age=int(input("Hi "+name_str+", what is your age?"))


#IF Else Condition
password=input("Enter the password: ")

if password=="secret@123":
    print("Access Granted")
else:
    print("Access Denied")
if int(age)  >= 18:
    print("You are a Adult")
    print("You can vote!")
else:
    print("You are a bacha")
    print("Go have some ice cream")

#IF else if 
score=int(input("Enter your Score: "))

if score >= 90:
    grade='A'
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >=60:
    grade='D'
else:
    grade='F'

print("Your Grade is :",grade)


#Nested If Else
has_license=input("Do you have a license? (true/false): ")

if age>=18:
    print("You are old enough to drive")

    if has_license:
        print("You can Drive!")
    else:
        print("But you need a License")
else:
    print("Too Young to drive")

#If else using "AND"

age=20
has_ticket=input("Do you have a ticket? (true/false): ")
if age >= 18 and has_ticket == "true":
    print("You can enter the concert")
else:
    print("Cannot Enter")

#If else using "OR"
day="monday"

if day =="saturday" or day=="sunday":
    print("It's the Weekend! Open the book")
else:
    print("Its a weekday")

is_sunny=True

if not is_sunny:
    print("its Sunny")
else:
    print("Its cloudy")

#Ternary Operator


if age>=18:
    status="adult"
else:
    status="minor"

status = "adult" if age >= 18 else "minor"
print(status)

