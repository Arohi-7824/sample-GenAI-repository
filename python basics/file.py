file=open("test.txt","r")
content=file.read()
print(content)
file.close()

with open("test.txt","r") as file:
    content=file.readlines()
    for line in content:
        print(line.strip())


with open("output.txt","w") as file:
    file.write("This is a sample output file.")

try:
    with open("students_new.csv","r") as file:
        content=file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to read the file.")
except Exception as e:
    print("An unexpected error occurred:", e)
