contacts = {
    "Amar": "0172222222222",
    "Sharif": "0175645353242",
    "Riaz": "01745443443453"
}

print("Contacts:", contacts)
print("sharif: ", contacts["Sharif"])
print("Riaz: ", contacts.get("Riaz"))
print("Unknown:", contacts.get("Unknown"))

contacts["Nila"] = "014864728768"
print("Contact:", contacts)
contacts["Amar"] = "01753455676"
print("Contacts:", contacts)
contacts.pop("Sharif")
print(contacts)

name = input("Enter your contact research: ")

if name in contacts:
    print("Phone: ",contacts[name])
else:
    print("Contact not found")

print("====Contact Book====")
for name,number in contacts.items():
    print(f"{name} -. {number}")