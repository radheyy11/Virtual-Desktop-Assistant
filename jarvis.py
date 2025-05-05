import pyttsx3
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys
import re
import tkinter
import cv2
import PIL.Image, PIL.ImageTk

# SET_WIDTH = 498
# SET_HEIGHT = 511

# window = tkinter.Tk()
# window.title("Jarvis - A Virtual Assistant")
# path = r"C:\Users\Deepak\OneDrive\Desktop\Python\Jarvis\jarvisbg.png"
# src=cv2.imread(path)
# cv_img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)
# photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
# img_on_canvas = canvas.create_image(0, 0, ancho = tkinter.NW, image = photo)
# canvas.pack()

# window.mainloop()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    htime = time.strftime('%H')

    if int(htime) >= 4 and int(htime) < 12:
        speak("GOOD MORNING")

    elif int(htime) >= 12 and int(htime) < 16:
        speak("GOOD AFTERNOON")

    elif int(htime) >= 16 and int(htime) < 19:
        speak("GOOD EVENING")

    else:
        speak("Hey") 
    

def has_integer(l):
    for item in l:
        try:
            n = int(item)
            v = n/100
        except:
            pass
    return v

def takeCommand():
    # It takes microphone input from the user and returns the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-in")
        print(f"User said: {query}")
    
    except Exception as e:
        speak("Couldn't recognize, please say that again")
        return "None"
    
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-password")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()
    
if __name__ == "__main__":
    wishme()
    speak("I am Jarvis, how may I help you?")
        
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if "what is" in query:
            speak("Searching...")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences = 5)
            speak("According to wikipedia...")
            print(results)
            speak(results)

            speak("do you want more info?")
            query1 = takeCommand().lower()
            if "yes" in query1:
                webbrowser.open(f"https://www.google.com/search?q={query}&rlz=1C1VDKB_enIN1118IN1119&oq=python+in+pro&gs_lcrp=EgZjaHJvbWUqBwgDEAAYgAQyBwgAEAAYgAQyBwgBEAAYgAQyBggCEEUYOTIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDINCAkQABiGAxiABBiKBdIBCTc3MTVqMGoxNagCCLACAQ&sourceid=chrome&ie=UTF-8")
            elif "no" in query1:
                speak("okay, no problem, thankyou!")

        elif "volume" in query:
            volume = engine.getProperty('volume')
            l = query.split(" ")
            number = has_integer(l)
            if ["low", "down"] in query:
                r = round(random.randrange(0.0, volume), 1)
                engine.setProperty('volume', volume-r)
                speak(f"volume changed to {r}")
            elif ["high", "up"] in query:
                r = round(random.randrange(volume, 1.0), 1)
                engine.setProperty('volume', volume-r)
                speak(f"volume changed to {r}")
            else:
                engine.setProperty('volume', volume-number)
                speak(f"volume changed to {number}")

        elif "open youtube" in query:
            speak("whatdo you want to search")
            queryyt = takeCommand().lower()
            speak("okay, opening")
            webbrowser.open_new(f"https://www.youtube.com/results?search_query={queryyt}")

        elif "open google" in query:
            speak("okay, opening")
            webbrowser.open("google.com")

        elif "open github" in query:
            speak("okay, opening")
            webbrowser.open("github.com")

        elif "play music" in query:
            music_dir = "D:\\musicdirectory"
            songs = os.listdir(music_dir)
            
            n = len(songs)
            i = random.randint(0, (n-1))
            os.startfile(os.path.join(music_dir, songs[i]))
            print(f"Currently playing...{songs[i]}")

        elif "time" in query:
            timestamp = time.strftime('%H:%M:%S')
            speak(f"the time is {timestamp}")

        elif "open code" in query:
            speak("okay, opening")
            codepath = "C:\\Users\\Deepak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "email to radhika" in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "radheyyyy11@gmail.com"
                sendemail(to, content)
                speak("Email has been sent")
            
            except Exception as e:
                print(e)
                speak("Sorry, failed to send the Email")

        elif "stop" in query:
            speak("huh, okay Bye")
            sys.exit()

        elif "open whatsapp" in query:
            speak("okay, opening")
            webbrowser.open("whatsappweb.com")
        
        elif "open amazon" in query:
            speak("what item do you want to search for")
            queryamazon = takeCommand().lower()
            speak("okay, opening")
            webbrowser.open_new(f"https://www.amazon.in/s?k={queryamazon}&crid=246RS73KVYY2P&sprefix={queryamazon}%2Caps%2C320&ref=nb_sb_noss_1")
        
        elif "open flipkart" in query:
            speak("what item do you want to search for")
            queryflipkart = takeCommand().lower()
            speak("okay, opening")
            webbrowser.open_new(f"https://www.flipkart.com/search?q={queryflipkart}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

        elif "open instagram" in query:
            webbrowser.open("instagram.com")

        
      
