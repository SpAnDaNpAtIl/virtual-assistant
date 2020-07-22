import pyttsx3
import smtplib
import datetime
from email.message import EmailMessage

engine = pyttsx3.init() #engine created for speaking

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def current_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(Time) 
    
def date():
    date = datetime.datetime.now().strftime("%d:%B:%Y")
    speak(date)
    
def initial_greet():
    speak("Hello Sir. I am Tony, your personal AI assistant")
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<10:
        speak("Good Morning!")
    elif hour>=12 and hour<14 :
        speak("Good Afternoon!")
    elif hour>=16 and hour<17:
        speak("Good Evening!")
    else:
        None
    speak("How can I help you?")

def query_solved_finally():
    speak("Hope that I was able to help you with this!")
    speak("How can I help you Spandan?")


def send_email(subject, to, message_content):
        msg = EmailMessage()
        msg.set_content(message_content)
        msg['Subject'] =subject
        msg['From'] = 'spandyinstiapp@gmail.com'
        msg['To'] = to
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('spandyinstiapp@gmail.com', 'InstiApp')
        server.send_message(msg)
        server.close()


    
    