count=0
while count < 5:
    print("Count is ",count)
    count+=1
print("Loop Ended")

for i in range(50,5,-5):
    print("i is ",i)

for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print()

numbers=[1,2,3,4,5,6,7,8,9,10]
num=int(input("Enter a number to search: "))
for n in numbers:
    if n == num:
        print("Number found in the list!")
        break
else:
    print("Number not found in the list.")