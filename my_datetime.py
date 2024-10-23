from _datetime import datetime as dt

# print out time
now = dt.now()
print(now)

print(type(now))

# print out this year
year = now.year
print(year)

if year == 2024:
    print("Happy life.")
    
day_of_week = now.weekday()
print(day_of_week) # 這一週的禮拜幾

# store my birthday's value.
date_of_birth = dt(year= 1995, month=4, day=2)
print(date_of_birth)

