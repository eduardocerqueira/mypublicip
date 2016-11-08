import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import requests
import os

"""
Short version for mypublicip
"""

# replace these variables
_mail_from = "my-public-ip@server.com"
_mail_to = ["user1@gmail.com", "user2@gmail.com"]
_mail_subject = "my new public IP"
_server = "smtp.gmail.com"
_port = 587
_username = "username@gmail.com"
_password = "password"


def send_email(ip):
    fromaddr = _mail_from
    toaddr = _mail_to
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = str(toaddr)
    msg['Subject'] = _mail_subject

    body = "%s" % ip
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(_server, _port)
    server.starttls()
    server.login(_username, _password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def get_public_ip():
    url = "http://ipecho.net/plain"
    r = requests.get(url)
    return r.content


def save_ip(ip):
    with open("myip.txt", "w") as myip:
        myip.write(ip)
    return True


def compare(ip):
    with open("myip.txt", "r") as prev_ip:
        prev_ip.read()
    if ip in prev_ip:
        return True
    else:
        return False


if __name__ == '__main__':
    ip = get_public_ip()
    if os.path.exists("myip.txt"):
        if compare(ip) is False:
            send_email(ip)
            save_ip(ip)
    else:
        save_ip(ip)
