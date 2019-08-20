from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText 

def main():
    sender = '*******@126.com'
    receivers = ['***********@hotmail.com','*******@icloud.com']
    message = MIMEText('宋哈娜永远是我老婆o(*￣▽￣*)o','plain','utf-8')
    message['From'] = Header('AyayaPlayer','utf-8')
    message['To'] = Header('D.Va','utf-8')
    message['Subject'] = Header('Love, DVa','utf-8')
    smtper = SMTP('smtp.126.com')
    smtper.login(sender,'***********')
    smtper.sendmail(sender,receivers,message.as_string())
    print('Email sent')

if __name__ == "__main__":
    main()