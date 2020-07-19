#first of all we will write speak function so that jarvis can speakp
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import time
import webbrowser
import os
import wolframalpha
engine = pyttsx3.init('sapi5')  # sapi5 - reason why jarvis speaks
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
 engine.say(audio)
 engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Mr. Paras")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Mr. Paras")

    else:
        speak("Good Evening Mr. Paras")

    speak("Sir I am Jarvis . Please tell me how may I help you")

def takecommand():
    #it takes microphone input from user and returns output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        #time.sleep(2)
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio=r.listen(source)

    try:
        print("Recognizing...")
        time.sleep(1)
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

        
    except Exception as e: 
        speak("Pardon Say that again Sir")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
#logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("Acccording to Wikipedia ")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("here you go to youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Well! i know google is one of your good friends")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("opening life of developers")
            webbrowser.open("stackoverflow.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        #elif 'play music' in query:
            #music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            #songs = os.listdir(music_dir)
            #print(songs)    
            #os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'mother' in query:
            print("Born in sarsina. Her date of birth is 5 July.She is a teacher and and a great cook")
            speak("Born in sarsina. Her date of birth is 5 July.She is a teacher and and a great cook")
        elif 'father' in query:
            print("Born in Budhana. His date of birth is 21 December.He is a government servant")
            speak("Born in Budhana. His date of birth is 21 December.He is a government servant")
        elif 'create' in query:
            print("Thanks to Paras who brought me here")
            speak("Thanks to Paras who brought me here")
           
        elif 'stop' in query:
            exit()