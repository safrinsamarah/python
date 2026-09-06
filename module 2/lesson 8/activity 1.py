balance = 1000

while True:
    print("Please Pick your choice: \n 1. Withdraw \n 2. Deposit \n 3. Check Balance \n 4. Exit")
    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        amount = float(input("Please write the amount of withdraw: "))
        if amount > balance:
            print("Insuficient Funds!")
        else:
            balance = balance - amount
            print("Withdraw successful!")

    elif choice == 2:
        amount = float(input("Please write your amount to deposit: "))
        balance = balance + amount
        print("Deposit successful")

    elif choice == 3:
        print(f"Current balance: {balance}")

    elif choice == 4:
        print("Thank you for banking with us.")
        break
    else:
        print("Invalid number.")
