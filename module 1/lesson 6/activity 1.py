age = int(input("Enter your age: "))
is_student = input("Are you a student (yes/no)? ").lower() == "yes"

if age < 10:
    price = 0
elif age <= 15 or is_student:
    price = 8
else:
    price = 15

print(f"Your ticket price is {price} BDT")
