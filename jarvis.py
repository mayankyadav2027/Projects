import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')#two voices in my system
print(voices[0].id)# 0 for male voice and 1 for female voice
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#greetings
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Goood Evening")
    
    speak("I am Jarvis. Tell me how can i help you?")

#takes command 
def takeCommand():
    r = sr.recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    # speak("hey there")
    wishMe()
    while(True):
        query = takeCommand().lower() #converting userquery into lowercase
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia", "")#replace wikipedia in query with nothing
            results = wikipedia.summary(query,sentences = 2)##will show two sentences only
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music 'in query:
            music_dir = 'C:\Users\admin\Downloads\New folder\01.mp3'
