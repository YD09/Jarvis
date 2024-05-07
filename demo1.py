import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import pyautogui as py
import time
import requests

engine = pyttsx3.init('sapi5')#microsoft speech api
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)#0 for david 1 for jira
engine.setProperty('rate',150)#speech rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning!")

    elif hour>=12 and hour <18:
        speak("Good Afternoon")

    else:
        speak(" Good Evening !")

    speak("Ready To Comply.what can i do for you") 


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
        
        except Exception as e:
            print("Say that again please")
            return "None"
        return query
    
if __name__ == "__main__":
        wishMe()
        while True:
            query = takeCommand().lower()
            if 'open chrome' in query:
                os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
                py.moveTo(952,319,1)
                py.click(x=952,y=319,clicks=1,interval=0,button='left')

            elif 'maximize this window' in query:
                py.hotkey('alt','space')
                time.sleep(1)
                py.press('x')

            elif 'google search' in query:
                query = query.replace("google search","")
                py.hotkey('alt','d')
                py.write(f"{query}",0.1)
                py.press('enter')

            elif 'youtube search' in query:
                query = query.replace("Youtube search","")
                py.hotkey('alt','d')
                time.sleep(1)
                py.press('tab')
                py.press('tab')
                py.press('tab')
                py.press('tab')
                time.sleep(1)
                py.write(f"{query}",0.1)
                py.press('enter')

            elif 'open new window' in query:
                py.hotkey('ctrl','n')

            elif 'open incognito ' in query:
                py.hotkey('ctrl','shift','n')

            elif 'minimize this window' in query:
                py.hotkey('alt','space')
                time.sleep(1)
                py.press('n')

            elif 'open history' in query:
                py.hotkey('ctrl','h')

            elif 'open downloads' in query:
                py.hotkey('ctrl','j')

            elif 'previous tab' in query:
                py.hotkey('ctrl','shift','tab')

            elif 'next tab' in query:
                py.hotkey('ctrl','tab')

            elif 'close tab' in query:
                py.hotkey('ctrl','w')

            elif 'close window' in query:
                py.hotkey('ctrl','shift','w')

            elif 'clear browsing history' in query:
                py.hotkey('ctrl','shift','delete')

            elif 'close chrome' in query:
                os.system("taskkill /f /im chrome.exe")

            elif "who are you " in query:
                print("My name is Jarvis")
                speak("My name is Jarvis")
            
            elif "who created you" in query:
                print("I am just a computer programme,Inspired by M.C.U")
                speak("I am just a computer programme,Inspired by M.C.U")

            elif 'what is' in query:
                speak("searching wikipedia")
                query = query.replace("what is","")
                results =wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'who is' in query:
                speak("searching wikipedia")
                query = query.replace("who is","")
                results =wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            #elif 'just open google' in query:
            #    webbrowser.open('google.com')

            #elif 'open google' in query:
            #    speak("What should i search ?")
            #   qry = takeCommand().lower()
            #   webbrowser.open(f"{qry}")
            #   results = wikipedia.summary(qry,sentences=1)
            #    speak(results)

            elif 'just open youtube' in query:
                webbrowser.open('youtube.com')

            elif 'open youtube ' in query:
                speak("what will you like to watch ?")
                qrry = takeCommand().lower()
                wk.playonyt(f"{qrry}")

            elif 'search on youtube' in query :
                query = query.replace("search on youtube","")
                webbrowser.open(f"www.youtube.com/results?search_query={query}")

            elif 'close browser' in query:
                os.system("taskkill /f /im chrome.exe")

            elif "open command prompt" in query:
                os.system("start cmd")

            elif "close command prompt" in query:
                os.system("taskkill /f /im cmd.exe")

            elif 'what is time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, the time is {strTime}")

            elif "shut down the system" in query:
                os.system("shutdown /s /t 5")

            elif "Restart the system" in query:
                os.system("shutdown /r /t 5")

            elif "lock the system" in query:
                os.system("rundll32.exe powrprof.dll,suspend 0,1,0")

            elif "volume up " in query:
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")
                py.press("volumeup")

            elif "volume down " in query:
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")
                py.press("volumedown")

            elif "mute device" in query:
                py.press("volumemute")

            elif "what is my ip address" in query:
                speak("checking...")
                try:
                    ipAdd =requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    speak("your ip address is")
                    speak(ipAdd)
                except Exception as e:
                    speak("Network not available, Try later on")

            




                





            



        