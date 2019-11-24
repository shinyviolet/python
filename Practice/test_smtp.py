# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# email 用于构建邮件内容

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '55484402@qq.com'
password = 'ishylbzctzizbgge'

# 收信方邮箱
to_addr = ['82026724@qq.com','55484402@qq.com']

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text = '''亲爱的学员，你好！
​    能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
msg = MIMEText(text,'plain','utf-8')
msg['From'] = Header(from_addr)
msg['To'] = Header(','.join(to_addr))
msg['Subject'] = Header('python test2')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()