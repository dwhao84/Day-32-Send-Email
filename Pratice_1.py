import smtplib
from _datetime import datetime as dt
from mail import yahoo_address

"""
Objective: Send a motivational quote via email on the current weekday.

Hints:
1. Use the datetime module to obtain the current day of the week.
2. Open the quotes.txt file and obtain a list of quotes.
3. Use the random module to pick a random quote from your list of quotes.
4. Use the smtplib to send the email to yourself.
"""

# Create SMTP(Simple Mail Transfer Protocol)
s = smtplib.SMTP(yahoo_address, 587)
# Start TLS for security
s.starttls()

