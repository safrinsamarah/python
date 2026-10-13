import random
import math
from datetime import datetime, timedelta


def generate_order_id():
    """Generate a random order ID."""
    number = random.randint(10000, 99999)
    return f"ORD-{number}"


def calculate_price(price, quantity, discount=0):
    """Calculate the final price after discount."""
    subtotal = price * quantity
    discount_amount = subtotal * discount / 100
    total = subtotal - discount_amount

    # Round the final price upward to 2 decimal places
    total = math.ceil(total * 100) / 100

    return total


def calculate_delivery_date(days):
    """Calculate the expected delivery date."""
    today = datetime.now()
    delivery_date = today + timedelta(days=days)
    return delivery_date.strftime("%d-%m-%Y")


def generate_booking_id():
    """Generate a random booking ID."""
    number = random.randint(1000, 9999)
    return f"BOOK-{number}"


def calculate_event_date(days):
    """Calculate the upcoming event date."""
    today = datetime.now()
    event_date = today + timedelta(days=days)
    return event_date.strftime("%d-%m-%Y")
