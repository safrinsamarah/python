drink = input("What would you like? Coffee or tea? -> ").lower()

if drink == "coffee":
    size = input("What size will you like to take? (S/M/L) -> ").upper()
    if size == "S":
        print("You have selected small size. You have to pay 30 BDT.")
    elif size == "M":
        print("You have selected medium size. You have to pay 150 BDT.")
    elif size == "L":
        print("You have selected large size. You have to pay 200 BDT.")
    else:
        print("INVALID INPUT")

elif drink == "tea":
    sugar_level = int(input("What is the sugar level? (0 - 2) -> "))
    if sugar_level == 0:
        print("You chose level 0 sugar tea.")
    elif sugar_level == 1:
        print("You chose level 1 sugar tea.")
    elif sugar_level == 2:
        print("You chose level 2 sugar tea.")
    else:
        print("Invalid Input.")
