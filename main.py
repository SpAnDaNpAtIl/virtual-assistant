from Speech import *
from Audio_recognizer import *
from corona_API import *
from weather import *
import wikipedia

if __name__ == "__main__":
    initial_greet()
    while(True):
        query = query_command().lower() #query recieved
        if 'tony' in str(query):
            query.replace('tony ','')
            if 'covid' in str(query):
                query = query.split(" ")[-1]
                speak(corona_func(query))
                
            elif 'time' in str(query):
                time()
            
            elif 'date' in str(query):
                date()
                
            elif 'send email' in query:
                statement_partitions = query.split(" ")
                for i in statement_partitions:
                    if i.find(".com") != -1:
                        to = i
                try:
                    speak("Tell me the content which you want to write in the mail?")
                    message_content = takeCommand()
                    speak("What should be the subject?")
                    subject = takeCommand()    
                    send_email(subject, to, message_content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    
            elif 'wikipedia' in str(query):
                speak("Searching in Wikipedia")
                query = query.replace("wikipedia","")
                query = query.replace("Tony", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
                
            elif 'weather' in str(query):
                if 'complete' in str(query):
                    speak('Temperature in your region is '+str(current_temp()) + 'degree celsius. The current status of weather conditions is:' +status_of_weather())
                    speak('Wind speed is ' + str(wind_speed())+'kilometers per hour. Humidity is ' + str(humidity())
                else:
                    speak('Temperature in your region is '+str(current_temp()) + 'degree celsius. The current status of weather conditions is:' +status_of_weather())
                
            #elif for new functions 
            elif 'offline' in str(query):
                quit()
            query_solved_finally()
        else:
            speak("Can you please repeat again Sir?")
            
            
    
    