import pyautogui 
#what is pyautogui?
#used to programmatically control the mouse and key board
import pyttsx3
#what is pyttsx3?
#used for text to speech
import speech_recognition as sr
#what is speechrecognition?
#recogniser records our voice
import pyaudio
#what is pyaudio?
#to play and record audio
import datetime
import os
from AppOpener import open
from AppOpener import close
import wikipedia
import random
import webbrowser
import sys
import subprocess
import time
import requests
import pywikihow
import winsound

#>>..First to  create an base engine -- audio(voice) ---  VOIce ASSistant --- speak --- listen

#N>>create an engine,engine that creates its base of voice 


engine = pyttsx3.init("sapi5") #what is sapi5 = microsoft speech API  voices
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',180)
#>>> to speak defining function

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()




def wish():
    hour = int(datetime.datetime.now().hour)
    time = datetime.datetime.now().strftime("%H:%M")

    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak(f"time is {time}")
    speak("hello BOSS , DICE HERE ,  how can i help you ")


def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is :{head[i]}")

import datetime
import winsound


def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))
    altime=altime[11:-3]
    Horeal=altime[:2]
    Horeal = int(Horeal)
    Mireal= altime[3:5]

    Mireal= int(Mireal)
    print(f"Done, alarm is set for {Timing}")
    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("alarm is running")
                winsound. PlaySound("abc",winsound.SND_LOOP)
            elif Mireal<datetime.datetime.now().minute:
                break




def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.......")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=500, phrase_time_limit=50)

        try:
            print("recognising...")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
        except  Exception as e:

            return "none"
        return query

def start():
        wish()

        while True:

            query = takecommand().lower()

            if "notepad" in query:
                open("notepad")
            if "close notepad" in query:
                close("notepad")
            if "close notepad" in query:
                close("Notepad")
            elif "close word" in query:
                close("Word")
            elif "open whatsapp" in query:
                open("Whatsapp")
            elif "close whatsapp" in query:
                close("whatsapp")
            elif "word" in query:
                open("word")
            if "camera" in query:
                open("camera")
            if "file explorer" in query:
                open("file explorer")
            if "close file explorer " in query:
                close("file explorer")
            if "chrome" in query:
                open("google chrome")
            if "close chrome " in query:
                close("google chrome")
            if "brave" in query:
                open("brave")
            if "close brave" in query:
                close("brave")
            if "pycharm" in query:
                open("pycharm")
            if "close pycharm " in query:
                close("pycharm")
            if "zoom" in query:
                open("zoom")
            if "close zoom " in query:
                close("zoom")
            if "open command prompt" in query or "open cmd" in query:
                open("command prompt")
            if "close cmd " in query or "close command prompt " in query :
                close("command prompt")
            if "bing" in query:
                open("bing")
            if "close bing " in query:
                close("bing")
            if "instagram" in query:
                open("Instagram.exe")
            if "close instagram " in query:
                subprocess.call("Instagram.exe")
            if "open power point " in query:
                open("Powerpoint")
            if "close power point " in query:
                close("Powerpoint")
            if "open Excel " in query:
                open("Excel")
            if "open microsoft store " in query:
                open("Microsoft store")


            if "wikipedia" in query:
                speak("searching wikipedia....")
                query =query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipeia")
                speak(results)
                print(results)
            elif "youtube" in query:
                webbrowser.open("www.youtube.com")
            elif "open google" in query:
                speak("what should i search on google")
                cm = takecommand().lower()
                webbrowser.open(f"{cm}")
            elif "open mail" in query:
                webbrowser.open("www.gmail.com")

            elif "switch the window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
            elif "update news" in query:
                speak("just a sec boss")
                news()
            elif "where am i" in query or "where we are" in query:
                speak("finding............")

                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f'boss i am not sure , but i think we are in{city} city of {country}')
                except Exception as e:
                    speak("due to network issue or locator issue i am not able to find the exact location")
                    pass

            elif "take screenshot" in query or "take a screenshot" in query:
                speak("what is the name of screen should that should be saved")
                name = takecommand().lower()
                time.sleep(2)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done boss")
            elif "activate how to do" in query :
                from pywikihow import search_wikihow
                speak("activated")
                how=takecommand()
                max_results=1
                how_to = search_wikihow(how,max_results)
                assert len(how_to)==1
                how_to[0].print()
                speak(how_to[0].summary)
            elif "Hello Dice" in query or "hello" in query or "hi " in query:
                speak("Hello Boss")
            elif "how are you" in query :
                speak("good,how about you")
            elif "fine" in query:
                speak("that's great")
            elif "i love you" in query:
                speak("me to ....... "
                      "have a great day ...")
            elif "tell me a joke" in query:
                speak("sorry, i am in depression ,i dont have any mood ...... ")



            elif "you can sleep" in query:
                speak("ok boss,just wakeup me if you need...")
                break
            elif "alarm" in query:
                speak("at what time should i fix alarm")
                tt=takecommand()
                tt=tt.replace("set alarm to ","")
                tt = tt.replace(".","")
                alarm(tt)






if __name__ == "__main__":
    speak("I am drunken guys , just wake up me....")
    while True:
        permission = takecommand()
        if "wake up" in permission or "wake up dice" in permission:
                   start()
        elif "exit" in permission:
                sys.exit()





