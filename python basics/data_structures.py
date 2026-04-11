#lists
my_list=[1,2,3,4,5]
print(my_list[0])
print(my_list[-1])

lists=[1,True,"Hello",3.14]
print(lists[2])

print(my_list[1:4])
print(my_list[::2])

lists[0]=10
print(lists)

my_list.pop()
print(my_list)

#list operations:
#sum,min,max
print("The sum of all the elements in my_list is:", sum(my_list))
print("The minimum value in my_list is:", min(my_list))
print("The maximum value in my_list is:", max(my_list))
#count
print("The count of 3 in my_list is:", my_list.count(3))
#sort
my_list.sort()
print("my_list after sorting:", my_list)
#reverse
my_list.reverse()
print("my_list after reversing:", my_list)
#check membership
if 3 in my_list:
    print("3 is in the list")
else:
    print("3 is not in the list")

sqaures=[]
for i in range(1,11):
    sqaures.append(i**2)
print("The squares of numbers from 1 to 10 are:", sqaures)

#tuples
coordinates=(10,20)
person=("Arohi",21,"New York")
print(person[0])

name,age,city=person
print(f"I am {name}, I am {age} years old and I live in {city}.")

#dictionaries
student={"name":"Arohi",
        "age":21,
        "city":"New York",
        "grade":"A",
        "courses":["Python","Data Science","Machine Learning"]
    }
print(student.get("phone","Not Found"))
student["phone"]="123-456-7890"
student["age"]=22
print(student)

student.pop("grade")
print(student)
for key,value in student.items():
    print(f"{key}: {value}")


#sets
my_set=set()
numbers=[1,1,2,3,3,4,2,5,5,5,2,3,8,8,7,9]
unique_numbers=set(numbers)
print("Unique numbers:", unique_numbers)

unique_numbers.add(10)
print("Unique numbers after adding 10:", unique_numbers)