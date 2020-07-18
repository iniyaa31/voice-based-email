from email.message import EmailMessage
from difflib import SequenceMatcher
from reg_ import reg
import smtplib
import pyttsx3 as r
engine = r.init()
engine.setProperty('rate',150)
def speak(text):
    engine.say(text)
    engine.runAndWait()
min_=0
# create a dataset
msg=EmailMessage()
msg['From']='#Enter your mail id'# Sender Mail ID
speak("To whom would you like to send the mail")
text=reg()
for i in d:
    if SequenceMatcher(None,text, i).ratio()>min_:
        name=i
        min_=SequenceMatcher(None, text, i).ratio()
msg["To"]=d[name]
speak("would u like to add subject to the mail")
text=reg()
if text=="Yes" or text=="yes":
    speak("please tell me the subject of the mail")
    sub=reg()
    speak("is that "+sub)
    print("is that "+sub)
    text=reg()
    if text=="Yes" or text=="yes":
        msg['Subject']=sub
    else:
        speak("please enter the subject")
        sub=input()
        msg['Subject']=sub
speak("please tell me the content of the mail")
mesg=reg()
speak("is that "+mesg)
print("is that "+mesg)
text=reg()
if text=="Yes" or text=="yes":
    msg.set_content(mesg)
else:
    speak("please enter the content of the mail")
    mesg=input()
    msg.set_content(mesg)
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(msg['From'],'#Enter your password')
    smtp.send_message(msg)
    speak("Message Sent successfully")
    print("Message Sent successfully")
