import random
import math

def generate_booking_id():
    return "CW" + str(random.randint(1000, 9999))

def get_ticket_price(ticket_type):
    if ticket_type == "student":
        return 20
    elif ticket_type == "regular":
        return 30
    else:
        return 0

def calculate_service_charge(price):
    return math.ceil(price*0.10)

def calculate_discount(price):
    if price >= 30:
        return price*0.10
    else:
        return 0

def calculate_final_bill(price,vat,discount):
    return price + vat - discount

def display_booking_info(name,booking_id,price,vat,discount,total):
    print("\n-----BOOKING SUMMERY-----\n")
    print("NAME:",name)
    print("BOOKING ID: ", str(price))
    print("TICKET PRICE: $", str(price))
    print("SERVICE FEE: $", str(vat))
    print("FINAL PRICE: $", str(int(total)))
    print("\n Booking confirmed!")

print("\n ======CODING WORKSHOP BOOKING======\n")
name = input("Enter your name: ")
ticket_type = input("Enter your ticket type (student/regular): ").lower()

if ticket_type not in ["student","regular"]:
    print("Invalid input. Please choose student or regular")
else:
    booking_id = generate_booking_id()
    price = get_ticket_price(ticket_type)
    vat = calculate_service_charge(price)
    discount = calculate_discount(price)
    total = calculate_final_bill(price,vat,discount)
    display_booking_info(name,booking_id,price,vat,discount,total)
