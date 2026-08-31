correct_password = "python123"
attempts = int(input("How many attempts do you want? : "))

for attempts in range(1, attempts + 1):
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Wrong password.")