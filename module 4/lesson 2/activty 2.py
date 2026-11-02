#Step 1 create a restaurent menu
burger = ("Cheese burger", 300, "Main")
pizza = ("Cheese Pizza", 999, "Main")
juice = ("Orange juice", 120, "Beverage")

menu = (burger, pizza, juice)

print("Menu: ", menu)
print("First menu: ", menu[2])
print("First item name: ", menu[0][0])
print("First item type: ", menu[0][2])

#step 2 - slice, unpack and loop
print("First two item: ", menu[:2])

for name, price, category in menu:
    print(f"{name}-{price}-{category}")

# check items and combine menu
print("Is burger available in the menu? ->", burger in menu)
print("Is pizza available in the menu? ->", pizza in menu)

deserts = (
    ("cake", 250, "desert"),
    ("ice cream", 100, "desert")
)

full_menu = menu + deserts
print("Full menu: ", full_menu)