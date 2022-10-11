import time
import modules
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import json
import os
import smtplib
import spotipy
import wolframalpha
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Guten Morgen!")

    elif hour>=12 and hour<18:
        speak("Guten Nachmittag!")

    else:
        speak("Guten Abend!")

    speak("Ich bin Ihr persönlicher Sprachassistent. Wie kann ich Ihnen helfen?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='de-DE')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Bitte sagen sie das nochmal")
        speak("Bitte sagen sie das nochmal")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
     if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            wikipedia.set_lang("de")
            speak('Suche in Wikipedia')
            query = query.replace("wikipedia", "")
            print(query)
            results = wikipedia.summary(query, sentences=3)
            speak("Nach Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")
            print("google geöffnet")

        elif 'musik' in query:
            exec(open('general/musicPlayer.py').read())

        elif 'zeit' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, die Zeit ist {strTime}")
            print(f"Sir, Die Zeit ist {strTime} ")

        elif 'Uhr' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, die Zeit ist {strTime}")
            print(f"Sir, Die Zeit ist {strTime} ")

        elif 'danke' in query:
            speak("Kein Problem")
            print("Kein Problem")

        elif 'exit' in query:
            speak(f"Bis bald Sir")
            print("Bis bald Sir")
            time.sleep(5)
            exit()

        elif 'tschüss' in query:
            speak(f"Bis bald Sir")
            print("Bis bald Sir")
            time.sleep(5)
            exit()

        elif 'Maul' in query:
            speak(f"Bis bald Sir")
            print("Bis bald Sir")
            time.sleep(5)
            exit()




# Taking input from user
question = input('Question: ')

# App id obtained by the above steps
app_id = '6J82Y8-44J8G3YGJT'

# Instance of wolf ram alpha
# client class
client = wolframalpha.Client('6J82Y8-44J8G3YGJT')

#Language Doo Doo


while True:
# Stores the response from
  query = str(takeCommand())
  res = client.query(query)
  answer = next(res.results).text
  print(answer)
  speak(answer)

# Includes only text from the response

print(answer)
speak(answer)

res = client.query('Wetter in Rheinfelden')


