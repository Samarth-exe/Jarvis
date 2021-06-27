# Modules Imported
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
# assigning voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Making Jarvis speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#  Wish, Good morning etc. when you run the program
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('I am Jarvis. Please tell me how I may help you')

#  Listen to user(using speech_recognition)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said:{query}\n')
    
    except Exception as e:

        print('Say that again please...')
        return "None"
    return query

# All fucntions
if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        #Search Wikipedia using your voice!
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak('results')

        elif 'open google' in query:
            speak('Opening google')
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "google.com"
            webbrowser.get(browser_path).open(url)

        elif 'open youtube' in query:
            speak('opening youtube')
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "https://www.youtube.com"
            webbrowser.get(browser_path).open(url)

        elif 'open twitch' in query:
            speak('opening twitch')
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "https://twitch.tv"
            webbrowser.get(browser_path).open(url)

        elif 'open spotify' in query:
            speak('Opening spotify')
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "https://open.spotify.com"
            webbrowser.get(browser_path).open(url)

        elif 'play music' in query:
            speak('Playing music')
            music_dir = "" #If you have music tracks downloaded on your device, paste the path of the folder in the string
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'The time is{strTime}')

        elif "send mail" in query:
            speak('Please be patient while i make things ready for you')
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "" #Paste the URL of your Gmail Website here
            webbrowser.get(browser_path).open(url)

        elif "send email" in query:
            speak('Please be patient while i make things ready for you')
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "" #Paste the URL of your Gmail Website here
            webbrowser.get(browser_path).open(url)

        elif "send gmail" in query:
            speak('Please be patient while I make things ready for you')
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "" #Paste the URL of your Gmail Website here
            webbrowser.get(browser_path).open(url)

        elif 'open code' in query:
            speak('Opening Visual Studio Code')
            codePath = '' #Paste Visual Studio Code path in the string
            os.startfile(codePath)

        elif 'open zoom' in query:
            speak('Opening zoom')
            zoomPath = '' #Paste zoom path in the string
            os.startfile(zoomPath)

        #Opens Google Dictionary
        elif "open dictionary" in query:
            speak('Opening google dictionary')
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "https://www.google.com/search?q=google%2Fdictionary&oq=google%2Fdictionary&aqs=chrome..69i57j0i30l6j69i58.6846j0j7&sourceid=chrome&ie=UTF-8"
            webbrowser.get(browser_path).open(url)
        #Opens Google Translate
        elif "open translator" in query:
            speak('Opening google translator')
            browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            url = "https://www.google.com/search?q=google+translator&safe=active&sxsrf=ALeKk03nx-qDr4IAJxB6su_Hb4lb3NfEmw%3A1618299531862&ei=i0p1YI2LNNn99QOs6qCQAw&oq=google+tra&gs_lcp=Cgdnd3Mtd2l6EAMYADIECCMQJzIECCMQJzICCAAyAggAMgIIADIFCAAQsQMyBQgAELEDMgUIABCxAzICCAAyBQgAELEDOgcIIxCwAxAnOgcIABBHELADOg0IABCHAhCxAxCDARAUOgcIABCxAxBDOgQIABBDOgoIABCxAxCDARBDUNiBA1iTiQNgqpIDaAFwAngAgAHxAYgBhwmSAQUwLjQuMpgBAKABAaoBB2d3cy13aXrIAQnAAQE&sclient=gws-wiz"
            webbrowser.get(browser_path).open(url)

        #The program will stop running if you say exit 
        elif "exit" in query:
            exit()
