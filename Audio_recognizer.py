import speech_recognition as sr
import pyaudio

def query_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        #r.pause_threshold = 1 #It will wait for one second to record audio but not preferred
        #or we can also pass a n offset argument in r.listen 
        audio = r.listen(source)
        
    try:
        print("Recognizing")
        query = r.recognize_google(audio, key=None, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        query_command()
        
        
    return query


        