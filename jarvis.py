import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
#sapi5 is voice api by microsoft
voices=engine.getProperty('voices')
# print(voices)
# i have 2 voice......now we set voices
# print(voices[1])
engine.setProperty('voice',voices[0].id)
 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am Anony. How can I help You")


def takeCommand():
    # it takes microphone input from user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recoginizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user Said: {query}\n")
    except Exception as e:
        # speak("Say that again Please")
        print("Say that again Please")

        return "None"
    return query



if __name__=="__main__":
    # speak("I am Anony")
    wishMe()
    while True:
        query=takeCommand().lower()


        # Logic for executing task based Queries
        if 'wikipedia' in query:
            speak('Searching Wiipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            #for opening query we will import webbrowser
            chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
            
            webbrowser.get(chrome_path).open('youtube.com')
        elif 'open google' in query:
            #for opening query we will import webbrowser
            chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
            
            webbrowser.get(chrome_path).open('google.com')
            # webbrowser.open("google.com")
        elif 'open gfg' in query:
            #for opening query we will import webbrowser
            
            chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
            
            webbrowser.get(chrome_path).open("https://practice.geeksforgeeks.org/explore?page=1&curated[]=1&sortBy=submissions&curated_names[]=SDE%20Sheet")
        elif 'open whatsapp' in query:
            #for opening query we will import webbrowser
            
            chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
            
            webbrowser.get(chrome_path).open('https://web.whatsapp.com/')
        elif 'open leetcode' in query:
            #for opening query we will import webbrowser
            
            chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
            
            webbrowser.get(chrome_path).open('https://leetcode.com/study-plan/leetcode-75/?progress=x5gc6p5s')
        elif 'open codechef' in query:
            
            chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
            
            webbrowser.get(chrome_path).open("https://www.codechef.com/ide?itm_medium=navmenu&itm_campaign=ide")
        elif 'play music' in query:
            #we will import os module for using in chrome application
            music_dir='F:\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\vaman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            
            os.startfile(chrome_path)
        # elif 'open file explorer' in query:
        #     os.startfile("This PC")



        if "quit" or "exit" in query:
            speak("GoodBye")
            break