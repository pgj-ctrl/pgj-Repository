from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def inet_mail(body,sender,receivers,subject,host,passwd):
    message = MIMEText(body,'plain','utf8')
    message['FROM'] =Header(sender,'utf8')
    message['To'] = Header(receivers[0],'utf8')
    message['Subject'] = Header(subject,'utf8')

    smtp = smtplib.SMTP()
    smtp.connect(host)
    # smtp.starttls()
    smtp.login(sender,passwd)
    smtp.sendmail(sender,receivers,message.as_bytes())

if __name__ == '__main__':
    body = "python发送互联网邮件测试\n昂鸠怡！！！\n"
    sender = '1729687833@qq.com'
    receivers = ['1729687833@qq.com','465560122@qq.com']
    subject = "py test"
    host = 'smtp.qq.com'
    passwd = getpass.getpass()
    inet_mail(body,sender,receivers,subject,host,passwd)