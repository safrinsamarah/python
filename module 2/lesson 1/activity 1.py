password = input("Enter your password: ")
upper_case = 0

for char in password:
    if char.isupper():
        upper_case += 1

print(f"There are {upper_case} uppercase lesAfSatters.")
