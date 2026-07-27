temp = float(input("Enter the temparature: "))
people = int(input("Enter the number of people: "))

if temp > 25:
    if people > 3:
        print("MAX AC: Crowded room")
    else:
        print("ECO AC Mode ON")
elif temp > 18:
    print("Heating ON!")
else:
    print("Invalid input.")