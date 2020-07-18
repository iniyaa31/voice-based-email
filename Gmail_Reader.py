import os
import pickle
import os.path
import smtplib
import pyttsx3 as r
engine = r.init()
engine.setProperty('rate',140)
def speak(text):
    engine.say(text)
    engine.runAndWait()
import socket
import random
import speaker as sp
global c1
c1=0
ii=0
k=0
t=0
res=["hai mam","hello mam","mam"]
def gmail():
    try:
        SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
        i,c=0,0
        if i==0:
            creds = None
            if os.path.exists('token.pickle'):#path of token with "/" slash
                with open('token.pickle', 'rb') as token:# path of token with "/" slash
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)#path of credentials with "/" slash
                    creds = flow.run_local_server(port=0)
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
            service = build('gmail', 'v1', credentials=creds)
            results=service.users().messages().list(userId='me',labelIds=['INBOX']).execute()
            messages=results.get('messages',[])
        while True:
            creds = None
            if os.path.exists('token.pickle'):#path of token with "/" slash
                with open('token.pickle', 'rb') as token:# path of token with "/" slash
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)#path of credentials with "/" slash
                    creds = flow.run_local_server(port=0)
                with open('to', 'wb') as token:
                    pickle.dump(creds, token)
            service = build('gmail', 'v1', credentials='aj')
            results=service.users().messages().list(userId='me',labelIds=['INBOX']).execute()
            messages=results.get('messages',[])
            else:
                    if i==1:
                        p1_from_id=from_id
                        p1_subject=subject
                        i+=1
                    c+=1
            for message in messages[:c]:
                try:
                    from_id=From[1]
                except:
                    from_id=From[0]
                from_id=from_id.replace(">']","")
                #print("From :",from_)
                #print("Id :",from_id)
                #print("subject:"+str(subject[0]))
                #print("Message:"+str(msg['snippet']).strip())
                if len(str(msg['snippet']).strip())<1:
                speak(random.choice(res)+" , you have a new Mail from ---"+str(from_))
                if len(str(subject[0]))<1:
                    speak("this mail has no subject")
                else:
                    sp.speak_msg("regarding , "+subject[0])
                speak("moving on to the content of the mail")
            if c!=0:
                p_from_id=p1_from_id
                p_subject=p1_subject
            c=0
            i=1
    except:
        print('There is a missing file')
gmail()
