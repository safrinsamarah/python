def add(x,y):
    result = x+y
    print(f"{x} + {y} = {result}")

def subtract(x,y):
    result = x-y
    print(f"{x} - {y} = {result}")

def multiply(x,y):
    result = x*y
    print(f"{x} * {y} = {result}")

def divide(x,y):
    result = x/y
    print(f"{x} / {y} = {result}")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number:"))

choice = input("Enter your operation choice (+,-,*,/): ")

if choice == "+":
    add(x,y)

elif choice == "-":
    subtract(x,y)

elif choice == "*":
    multiply(x,y)

elif choice == "/":
    divide(x,y)

else:
    print("invalid number.")