from selenium import webdriver
import time
import smtplib
import imghdr
from email.message import EmailMessage


def send_screenshots(screenshots):
    if screenshots:
        msg = EmailMessage()
        msg['Subject'] = 'TEST'
        msg['From'] = "test88005553535@mail.ru"
        msg['To'] = "rostislav.bedrin.98@mail.ru"
        for s in screenshots:
            msg.add_attachment(s, maintype='image', subtype=imghdr.what(None, s))
        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.login(msg['From'], "88005553535test")
        server.send_message(msg)
        server.quit()


def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.screenshots = []


def after_all(context):
    send_screenshots(context.screenshots)
    #time.sleep(10)
    context.browser.quit()
