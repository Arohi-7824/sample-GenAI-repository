try:
    num=int(input("Enter a number: "))
    res=100/num
    print("The result of 100 divided by", num, "is", res)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print("An unexpected error occurred:", e)

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age > 150:
        raise ValueError("Age cannot be greater than 150.")
    return age
try:
    age = int(input("Enter your age: "))
    valid_age = validate_age(age)
    print("Your age is:", valid_age)
    
    validate_age(-5)

except ValueError as ve:
    print("Invalid age:", ve)

