import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_auto import *
from News import *
import randfacts
from jokes import *
# from weather import *
import datetime

#gets info of current driver you are using
engine = p.init()
rate = engine.getProperty('rate')   #get the speed of the voice
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

today_date=datetime.datetime.now()


r = sr.Recognizer()      #helps to retrive info from source

speak("Hello sir I am your voice assistant.") 
# speak("Today is" + today_date.strftime("%d")+ "of" + today_date.strftime("%B")+ "And its currently" + (today_date.strftime("%I")) + (today_date.strftime("%AM")) + (today_date.strftime("%PM")))
# speak("Temperature in Kolhapur is"+ str(temp())+ "degree celcius"+ "and with"+ str(des()))
speak("How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000   #increase the spectrum of voice
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("I am having a good day sir")
   
speak("What can I do for you??")

with sr.Microphone() as source:
    r.energy_threshold = 10000   #increase the spectrum of voice
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)

if "information" in text2:
    speak("you need information related to which topic?")

    with sr.Microphone() as source:
       r.energy_threshold = 10000   #increase the spectrum of voice
       r.adjust_for_ambient_noise(source, 1.2)
       print("Listening...")
       audio = r.listen(source)
       infor = r.recognize_google(audio)

    speak("searching {} in wikipedia".format(infor))
    print("searching {} in wikipedia".format(infor))
    
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("you want me to play which video??")
    with sr.Microphone() as source:
       r.energy_threshold = 10000   #increase the spectrum of voice
       r.adjust_for_ambient_noise(source, 1.2)
       print("Listening...")
       audio = r.listen(source)
       vid = r.recognize_google(audio)
    
    speak("Playing {} on youtube".format(vid))
    print("Playing {} on youtube".format(vid))

    assist = music()
    assist.play(vid)

elif "news" in text2:
    speak("Sure sir, Now I will read news for you")
    print("Sure sir, Now I will read news for you")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    x=randfacts.getFact()
    print(x)
    speak("Did you know that," + x)

elif "joke" or "jokes" in text2:
    speak("Sure Sir, get ready for some chuckles")
    print("Sure Sir, get ready for some chuckles")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

