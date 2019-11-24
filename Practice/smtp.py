import smtplib
from email.message import EmailMessage

with open('email_content.txt') as f:
    msg=EmailMessage()
    msg.set_content(f.read())
msg['Subject']='this is the title'
from_addr=input('your email account:')
to_addr=[]
while True:
    addr=input('input your sent to emails:')
    to_addr.append(addr)
    ask=input('Do you want to add more? N or press any key to continue')
    if ask == 'N':
        break
msg['From']=from_addr
msg['To']=','.join(to_addr)

with smtplib.SMTP_SSL('smtp.qq.com') as client:
    password=input('password:')
    client.login(from_addr,password)
    client.send_message(msg)
