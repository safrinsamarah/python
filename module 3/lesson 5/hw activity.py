import datetime

name = input("Enter the name of event: ")
day = int(input("Enter event day: "))
month = int(input("Enter event month: "))
year = int(input("Enter event year: "))

today = datetime.date.today()
event = datetime.date(today.year, month, day)

if event < today: 
    event = datetime.date(today.year+1, month, day)

remaining_days = event - today

if remaining_days.days == 0:
    print(f"Happy {name} day!")
else:
    print(f"the event is in {remaining_days} days ")