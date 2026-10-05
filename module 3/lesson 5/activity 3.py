import datetime

day = int(input("Enter your birthday day: "))
month = int(input("Enter your birthday month: "))

today = datetime.date.today()
birthday = datetime.date(today.year, month, day)

if birthday < today: 
    birthday = datetime.date(today.year+1, month, day)

remaining_days = birthday - today

if remaining_days.days == 0:
    print("Happy birthday!")
else:
    print(f"Your birthday is in {remaining_days} days ")