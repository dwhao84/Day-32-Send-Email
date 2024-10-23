import smtplib
from email.mime.text import MIMEText
from random import randint
import linecache
from email.mime.multipart import MIMEMultipart
from mail import yahoo_address, my_email, yahoo_password

# 取得隨機名言
random_num = randint(1, 102)
QUOTES = "quotes.txt"
random_quotes = linecache.getline(QUOTES, random_num)
print(random_quotes)

# 設定郵件
msg = MIMEMultipart()
msg['From'] = yahoo_address
msg['To'] = my_email
msg['Subject'] = "Today's Quote"
msg.attach(MIMEText(random_quotes, 'plain'))

# 發送郵件
try:
    connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    connection.starttls()
    connection.login(user=yahoo_address, password=yahoo_password)
    connection.send_message(msg)
    print("Mail Success！")
    
    connection.quit()
    print("Quit")

except Exception as e:
    print(f"發生錯誤：{e}")