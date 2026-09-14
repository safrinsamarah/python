def travel_cost(distance,fuel_use,fuel_price):
    cost = distance / fuel_use * fuel_price
    return cost

distance = float(input("Enter distance in km: "))
fuel_use = float(input("Enter fuel used in litre: "))
fuel_price = float(input("Enter the price of fuel: "))

print(travel_cost(distance, fuel_use, fuel_price))