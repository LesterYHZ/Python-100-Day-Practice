from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib

def main():
    message = MIMEMultipart()

    # Text part
    text_content = MIMEText('宋哈娜是我老婆','plain','utf-8')
    message['Subject'] = Header('Love, DVa','utf-8')
    message.attach(text_content)

    # Read file and add it as an attachment
    with open('dva.txt','rb') as f:
        txt = MIMEText(f.read(),'base64','utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment;filename=dva.txt'
        message.attach(txt)

    smtper = SMTP('smtp.126.com')
    sender = '*****@126.com'
    receivers = ['*******@gmail.com']
    smtper.login(sender,'**********')
    smtper.sendmail(sender,receivers,message.as_string())
    smtper.quit()
    print('Email sent')

if __name__ == "__main__":
    main()