# Import Area Modules

from ast import Break, Return
from email.mime import audio

from importlib.abc import Traversable
#from ossaudiodev import SOUND_MIXER_SPEAKER
from threading import currentThread
from tokenize import Special
from unicodedata import name
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from datetime import date
import webbrowser
import calendar

#Use Python Text To Speech

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



#Set speak rate here

engine.setProperty('rate',200)


#----------- Functions Area -----------------#

#Speak Function

def speak(audio):
    engine.say(audio)
    
    
    engine.runAndWait()
    
    
#Greeting Function   
def wishme():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello sir Good Morning I am your personal voice assistance and how i can i help you")
    elif hour>=12 and hour <18:
        speak("helo sir Good Afternoon I am your personal voice assistance and how i can i help you")
    else:
        speak("hello sir Good Evening I am your personal voice assistance and how i can i help you")

#------------This Functions Takes Command from microphone and return text-----------#

def takeCommand():
    r = sr.Recognizer()
    print("Listening...")

    with sr.Microphone() as source:
        input_voice =  r.listen(source)
        
    
        
    try:
        audio_input = r.recognize_google(input_voice)
        r.pause_threshold =1
        audio_input = audio_input.lower()
        
        
    except:
        speak("Sorry I cant hear you Please Say it again")    
        return 'none'

    #-----------------Intro Area-----------#
    if 'yourself' in audio_input:
        speak("Myself mamba and , I am your personal voice assistence , version one point one and , baaghhel made me")
    elif 'your name' in audio_input:
        speak("Myself mamba and , I am your personal voice assistence , How can i help you sir")
    elif 'who are you' in audio_input:
        speak("Myself mamba and , I am your personal voice assistence , How can i help you sir")
    elif 'how are you' in audio_input:
        speak("I am absolutely fine sir , how are you ")
    elif 'made you' in audio_input:
        speak("mister Shivam Singh baaghhel made me and , it's my first vrsion")

    elif 'Do you know me' in audio_input:
        speak("Yes Sir, I know You, You are a legend and it's my hounour to talk with you ")

    elif 'can do' in audio_input:
        speak("Sir I can do a lot of things for you like , I can send emails and open youtube , and play music and i can set reminders for you , and many more cool things sir")
    #--------------- Time Date And Day ---------------------#
    current_time_date = date.today()
    #current_time_day = calendar.weekday(current_time)
    current_time_hour = datetime.datetime.now().hour
    current_time_min = datetime.datetime.now().minute
    if 'current time' in audio_input:

        speak(f"current time is:{current_time_hour} o clock and {current_time_min} minutes")
    elif 'time now' in audio_input:

        speak(f"current time is:{current_time_hour} o clock and {current_time_min} minutes")
    elif 'the time' in audio_input:

        speak(f"current time is:{current_time_hour} o clock and {current_time_min} minutes")
    
    elif 'date' in audio_input:
        speak(f"Todas date is {current_time_date}")
    #elif 'day' in audio_input:
      #  speak(f"todays day is {current_time_day}")
      #  print(current_time_day)


    
#-----------Wikipedia Search Area----------------
    
    elif 'wikipedia' in audio_input:
        speak("Searching From Wikipedia...")
        audio_input  = audio_input.replace("wikipedia","")
        results = wikipedia.summary(audio_input, sentences=1)
        speak("Acording To Wikipedia")
        speak(results)

    elif 'who is' in audio_input:
        speak("Searching From Wikipedia...")
        audio_input  = audio_input.replace("wikipedia","")
        results = wikipedia.summary(audio_input, sentences=1)
        speak("Acording To Wikipedia")
        speak(results)

    elif 'kaun' in audio_input:

        speak("Searching From Wikipedia...")
        audio_input  = audio_input.replace("wikipedia","")
        results = wikipedia.summary(audio_input, sentences=1)
        speak("Acording To Wikipedia")
        speak(results)
        

#-------------- Open Links Area--------#


    elif 'youtube' in audio_input:
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com")
        

    elif 'google' in audio_input:
        speak("Opening Google")
        webbrowser.open('https://www.google.com')
    elif 'facebook' in audio_input: 
        speak("Opening Facebook")
        webbrowser.open("https://www.fb.com")

    elif 'thank you' in audio_input:
        speak ("Thank You Sir And enjoy your day")
    elif 'play music'   in audio_input:
        speak("Playing Your favourite Song ,Sir")
        speak("Sorry Sir I can't find any song please check your internet connection")
    
    elif 'music' in audio_input:
        speak("Playing Your favourite Song ,Sir")
        speak("Sorry Sir I can't find any song , please check your internet connection")
    


    #--------------Bad Words Handeling----------_#
    
    elif 'madharchod' in audio_input:
        speak("Sir I am not like you , and i think you are not deserve me , please go and watch reels on Instagram")
    
    elif 'bahanchod' in audio_input:
        speak("Sir I am not like you , and i think you are not deserve me , please go and watch reels on Instagram")

    elif 'bahinchod' in audio_input:
        speak("Sir I am not like you , and i think you are not deserve me , please go and watch reels on Instagram")
    elif 'madarchod' in audio_input:
        speak("Sir I am not like you , and i think you are not deserve me , please go and watch reels on Instagram")

    elif 'bhaduachod' in audio_input:
        speak("Sir I am not like you , and i think you are not deserve me , please go and watch reels on Instagram")

    elif 'bhosdike' in audio_input:
         speak("Sir I am not like you , and i think you are not deserve me , please go and watch reels on Instagram")

#------------------ Main Area ----------------#

if __name__== "__main__": 
    wishme()

    while True:
        takeCommand()
        

    
    
   
