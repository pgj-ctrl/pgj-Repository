from email.mime.text import MIMEText
from email.header import Header
import smtplib

message = MIMEText("python local eamil test\n",'plain','utf8')
message['FROM'] =Header('root','utf8')
message['To'] = Header('zhangsan','utf8')
message['Subject'] = Header('py test','utf8')

smtp = smtplib.SMTP()
smtp.connect('localhost')
smtp.sendmail('root',['root','zhangsan'],message.as_bytes())