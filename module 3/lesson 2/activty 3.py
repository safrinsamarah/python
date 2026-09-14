def shopping_calculator(quantity,price,discount):
    total = quantity * price
    discount_amount = total * discount/100
    final_total = total - discount_amount
    return final_total

quantity = int(input("Enter your quantity of product: "))
price = float(input("Enter the price: "))
discount = float(input("Enter the discount: "))

print(shopping_calculator(quantity,price,discount))