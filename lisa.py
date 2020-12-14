# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:19:54 2020

@author: Administrator
"""

import speech_recognition as sr
import webbrowser
import os
from gtts import gTTS
from speak import *
from listen import *
from wikipedia import *
from movie import *
from youtube import *
import pyttsx3 as p


#initial conversation
r1 = sr.Recognizer()
engine = p.init()
engine.say("Hello , How are you today?")
engine.runAndWait()

with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source)
    print("How Are You today?")
    audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")


#clue for giving intructions
engine.say("what would you like me to do?")
engine.runAndWait()
print("What do you want")

#giving instructions
r2 = sr.Recognizer()
with sr.Microphone() as source:
    r2.adjust_for_ambient_noise(source)
    audio = r2.listen(source)
    try:
        instruction = r2.recognize_google(audio)
        print("")
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e :
        print("")
        
#getting info from wikipedia
r3 = sr.Recognizer()
if "information" in instruction:
    engine.say("information about what")
    engine.runAndWait()
    with sr.Microphone() as source1: 
        audio2 = r3.listen(source1)
        try:
            information = r3.recognize_google(audio2)
            lisa= info()
            lisa.get_info(information)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e :
            print("")