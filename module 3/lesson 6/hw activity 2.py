age = int(input("Enter your age: "))
budget = float(input("Enter your budget: "))
destination = input("Enter destination: ")
passport = input("Valid passport? (yes/no): ").lower()
visa_required = input("Visa required? (yes/no): ").lower()

visa = "yes"
if visa_required == "yes":
    visa = input("Valid visa? (yes/no): ").lower()

ticket = float(input("Ticket cost: "))
hotel = float(input("Hotel cost: "))
food = float(input("Food cost: "))

total = ticket + hotel + food
remaining = budget - total

if age < 18:
    decision = "Not approved: Age requirement."
elif passport != "yes":
    decision = "Not approved: No valid passport."
elif visa_required == "yes" and visa != "yes":
    decision = "Not approved: No valid visa."
elif budget < total:
    decision = "Not approved: Insufficient budget."
else:
    decision = "Approved!"

print("\n--- Travel Summary ---")
print("Destination:", destination)
print("Estimated cost:", total)
print("Remaining budget:", remaining)
print("Decision:", decision)