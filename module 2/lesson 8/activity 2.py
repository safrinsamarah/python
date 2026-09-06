total_bill = 0
total_count = 0

while True:
    item = input("Enter your item price (or done): ")

    if item.lower() == "done":
        break

    price = float(item)
    total_bill = total_bill + price
    total_count += 1

print(f"Total Bill: {total_bill}BDT")
print(f"Total count: {total_count}")