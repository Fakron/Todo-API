from datetime import date, datetime

deadline = datetime.date('2022-10-24')

today = date.today()
print(type(today))

if deadline == today:
    print("yes")