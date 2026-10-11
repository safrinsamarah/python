correct_PIN= "1342"
attempts = int(input("How many attempts do you want? : "))

for attempts in range(1, attempts + 1):
    PIN = input("Enter your PIN: ")
    if PIN == correct_PIN:
        print("Access granted!")
        break
    else:
        print("Wrong PIN.")