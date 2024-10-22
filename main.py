import smtplib
import mail
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from mail import my_email, my_password, yahoo_address, yahoo_password

# 哈哈，來試第一次 pull request
# 哈哈，來試第二次 pull request

# 創建郵件訊息
msg = MIMEMultipart()
msg['From'] = yahoo_address
msg['To'] = my_email
msg['Subject'] = "測試郵件"

內文 = "你好"
msg.attach(MIMEText(內文, 'plain'))

try:
    # 建立連接，使用正確的端口號（587用於TLS）
    # 建立連線的server
    connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    
    # 啟動TLS加密
    connection.starttls()
    
    # 登入
    connection.login(user=yahoo_address, password=yahoo_password)
    
    # 發送郵件
    connection.send_message(msg)
    
    # 關閉連接
    connection.quit()
    
    print("郵件發送成功！")

except Exception as e:
    print(f"發生錯誤：{e}")
    