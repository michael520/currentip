#!/usr/bin/python
import ConfigParser
import pycurl
import re
import cStringIO
import os
import smtplib

Config = ConfigParser.ConfigParser()
currentpath = os.path.dirname(os.path.realpath(__file__))
ini_file = os.path.join(currentpath,'base_setting.ini')
Config.read(ini_file)
ipchecker = 'http://checkip.dyndns.org/'
email = Config.get('baseinfo','notify_to_email')

def touch_file(file_name,workdir):
    fullpath = os.path.join(workdir,'IPs',file_name)
    if os.path.exists(fullpath):
        os.utime(fullpath, None)
        return 'old file (ip no change)'
    else:
        open(fullpath,'a').close()
        msg = 'new IP :' + file_name
        notify(email,msg)
        return 'new file(ip changed)'

def clear_out_put(out_put):
    return re.sub('<[^<]+?>|[Current IP Check]|[Current IP Address:]|\s','',out_put)

def notify(email,msg):
    server = Config.get('smtplogin','server')
    port = Config.get('smtplogin','port')

    sender = Config.get('baseinfo','sender')
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
    session.ehlo()
    session.login(Config.get('smtplogin','name'), Config.get('smtplogin','password'))

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
print touch_file(real_ip,currentpath)
