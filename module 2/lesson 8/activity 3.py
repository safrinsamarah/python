while True:
    password = input("Enter your password: ")
    has_upper = False
    has_numbers = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_numbers = True

    if len(password) < 8:
        print("Too short. Add at least 8 characters.")
        continue
    if not has_upper:
        print("Add at least one upper case.")
        continue
    if not has_numbers:
        print("Add at least one digit.")

    else:
        print("Password accepted.")