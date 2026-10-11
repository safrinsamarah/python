import calculator_module as cm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Choose your operator (+,-,*,/): ")

if operator == "+":
    addition = cm.add(a,b)
    print(f"{a} + {b} = {adiition}")

elif operator == "-":
    subtraction= cm.subtract(a,b)
    print(f"{a} - {b} = {subtaction}")

elif operator == "*":
    multiplication = cm.multiply(a,b)
    print(f"{a} x {b} = {multiplication}")

elif operator == "+":
    division = cm.divide(a,b)
    print(f"{a} + {b} = {division}")

else:
    print("Wrong invalid")