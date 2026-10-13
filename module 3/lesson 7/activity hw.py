import manager_module as manager

def order_menu():
    print("\n--- Order Management ---")

    order_id = manager.generate_order_id()

    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    discount = float(input("Enter discount percentage: "))

    total = manager.calculate_price(price, quantity, discount)
    delivery_date = manager.calculate_delivery_date(3)

    print("\n--- Order Summary ---")
    print("Order ID:", order_id)
    print("Total Price: tk", total, )
    print("Expected Delivery:", delivery_date)


def booking_menu():
    print("\n--- Event Booking ---")

    booking_id = manager.generate_booking_id()

    event_name = input("Enter event name: ")
    days = int(input("How many days from today? "))

    event_date = manager.calculate_event_date(days)

    print("\n--- Booking Summary ---")
    print("Booking ID:", booking_id)
    print("Event Name:", event_name)
    print("Event Date:", event_date)


def main():
    while True:
        print("\n===== BOOKING AND ORDER SYSTEM =====")
        print("1. Create an Order")
        print("2. Book an Event")
        print("3. Calculate Product Price")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            order_menu()

        elif choice == "2":
            booking_menu()

        elif choice == "3":
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))
            discount = float(input("Enter discount percentage: "))

            total = manager.calculate_price(
                price, quantity, discount
            )

            print("Final Price:", total, "Tk")

        elif choice == "4":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
