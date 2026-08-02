bill = float(input("Enter your bill: "))

if bill >= 800:
    discount = bill * 0.3
    total_bill = bill - discount
elif bill >= 500:
    discount = bill * 0.2
    total_bill = bill - discount
else:
    discount = 0

print(f"your discunt is {discount} taka.")
print(f"Your total bill is {total_bill} taka")