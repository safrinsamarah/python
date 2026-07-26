weather = input("Is it sunny, rainy, or winter? ").lower()
temp = int(input("What is the temperature in Celsius? "))

if weather == "sunny" and temp > 25:
    print("Wear sunscreen")
elif weather == "rainy" or temp < 10:
    print("Wear raincoat")
else:
    print("Have a nice day!")