def ticket_cost(price,tickets):
    total = tickets * price
    return total

price = float(input("Enter the price of one ticket: "))
tickets = int(input("Enter the number of tickets: "))

total = ticket_cost(price,tickets)
print(f"Total ticket costs: {total}BDT")
