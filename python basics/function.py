def hello():
    print("Hello, World!")

for i in range(5):
    hello()

#Function with parameters and return value
def add(a,b):
    return a+b
result=add(5,3)
print("The sum is ",result)

#Function with no parameters and only return value
def get_message():
    return "This is a message from a function with no parameters."

message = get_message()
print(message)

#Function with parameters and no return value
def greet(name):
    print("Hello,",name,"! Welcome to Python Programming.")

greet("Arohi")

#Function with no arguments and no return value
def say_hello():
    print("Hello!")
say_hello()

def add_numbers(**args):
    total=0
    for num in args.values():
        total+=num
    return total
result=add_numbers(a=5,b=10,c=15,d=20,e=25)
print("The total sum is ",result)

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Arohi", age=21, city="New York", profession="Student")
