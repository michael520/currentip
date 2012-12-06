#!/usr/bin/python
import pycurl
import re
import cStringIO
import os
import smtplib

ipchecker = 'http://checkip.dyndns.org/'
email = 'youremail@here.com'

def touch_file(file_name):
    if os.path.exists(file_name):
        os.utime(file_name, None)
        return 'old file (ip no change)'
    else:
        open(file_name,'a').close()
        msg = 'new IP :' + file_name
        notify(email,msg)
        return 'new file(ip changed)'

def clear_out_put(out_put):
    return re.sub('<[^<]+?>|[Current IP Check]|[Current IP Address:]|\s','',out_put) 

def notify(email,msg):
    server = 'smtp.gmail.com'
    port = 587

    sender = 'ipchecker@localhost'
    recipient = email
    subject = 'IP has Changed'
    body = msg

    headers = ["From: " + sender,
               "Subject: " + subject,
               "To: " + recipient,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    session = smtplib.SMTP(server, port)
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login('your@gmail', 'YourGmailPassword')

    session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    session.quit()

def getmyip():
    buf = cStringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, ipchecker)
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()
    return clear_out_put(buf.getvalue())
    buf.close()

real_ip = getmyip() 
print real_ip
print touch_file(real_ip)
