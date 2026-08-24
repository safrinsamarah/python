start_day = 2 # 0=sun, 1=mon, 2=tues
total_days = 30

column = 0

#Print blank padding before day 1
for i in range(start_day):
    print(" ",end="")
    column += 1

#Print the actual dates
for day in range(1, total_days + 1):
    print(f"{day:3}",end="")
    column += 1
    if column == 7:
        print()
        column = 0