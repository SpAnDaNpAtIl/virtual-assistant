import pyttsx3 #library for text to speech
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia


engine = pyttsx3.init()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is")
    speak(Time)    
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(day)
    speak(month)
    speak(year)
    
def greetme():
    speak("Welcome back sir!")
    date()
    time()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour< 12:
        speak("Good Morning Sir")
    elif hour >=12 and hour< 17:
        speak("Good Afternoon Sir")
    elif hour >= 17 and hour< 24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")
    speak("Jarvis at your service. How can I help you?")
    

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        #r.pause_threshold = 1 #It will wait for one second to record audio but not preferred
        #or we can also pass a n offset argument in r.listen 
        audio = r.listen(source)

        
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as s:
        print(s)
        speak("Say that again please")
        return "none"
    
    return query
  


if __name__ == "__main__":
    greetme()
    while True:
        query = takecommand().lower() #converting everything in lower case
        #add your commands in here
        if 'time' in str(query):
            time()
            
        elif 'date' in str(query):
            date()
        
        elif 'wikipedia' in str(query):
            speak("Searching in Wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        
        elif 'offline' in str(query):
            quit()
        