import requests
import random, re, smtplib, os, ssl
from email.mime.text import MIMEText
from email.header import Header

fund1 = "https://www.etmoney.com/mutual-funds/axis-focused-25-direct-plan-growth/15251"

def getnavs(url):
    r = requests.get(url)
    fund1_debug = str(r.content).split(",")
    #fund1_debug_1 = fund1_debug[0].split(" ")
    #print(fund1_debug_1[13])
    previous_navs = [i for i in fund1_debug if "prevNav" in i]
#    print(previous_navs)
    current_navs = [i for i in fund1_debug if "latestNav" in i]
#    print(current_navs)
    previous_navs[0] = previous_navs[0].split(":")
    previous_navs[1] = previous_navs[1].split(':')
    previous_navs[1][2] = previous_navs[1][2].split('"')
    prev_nav = "Previous NAV: "+ previous_navs[0][1] + " Dated: " + previous_navs[1][2][1]
    current_navs[0] = current_navs[0].split(":")
    current_navs[1] = current_navs[1].split(':')
#    print(current_navs[0])
#    print(current_navs[1])
    current_navs[1][2] = current_navs[1][2].split('"')
    current_nav = "Current NAV: " + current_navs[0][2] + " Dated: " + current_navs[1][2][1]
    return str(prev_nav), str(current_nav)

def send_email(data):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "balasankarkn@gmail.com"
    receiver_email = "balasankarkn@gmail.com"
    password = "sorsgnjhjwxpqhol"
    message = data

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


a = getnavs("https://www.etmoney.com/mutual-funds/axis-focused-25-direct-plan-growth/15251")
a = "Axis Focused 25 Direct: " + str(a)
b = getnavs("https://www.etmoney.com/mutual-funds/axis-bluechip-fund-direct-plan-growth/15249")
b = "Axis Bluechip Fund Direct: " + str(b)
c = getnavs("https://www.etmoney.com/mutual-funds/mirae-asset-hybrid-equity-fund-direct-growth/30103")
c = "Mirae Asset Hybrid Equity: " + str(c)

consolidated_output = """\

Subject: Daily Mutual Funds Update from Balu

""" + a + "\n" + b + "\n" + c

print(type(consolidated_output))
print(consolidated_output)

send_email(consolidated_output)
