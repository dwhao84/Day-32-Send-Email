from _datetime import datetime as dt
from random import randint
import linecache

"""
Objective: Send a motivational quote via email on the current weekday.

Hints:
1. Use the datetime module to obtain the current day of the week.
2. Open the quotes.txt file and obtain a list of quotes.
3. Use the random module to pick a random quote from your list of quotes.
4. Use the matplotlib to send the email to yourself.
"""

current_time = dt.now() # 2024/10/23

random_num = randint(1, 102)

QUOTES = "quotes.txt"
random_quotes = linecache.getline(QUOTES, random_num)
print(random_quotes)

# Create SMTP(Simple Mail Transfer Protocol)
# https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/




