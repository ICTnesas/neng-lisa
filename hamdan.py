# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyttsx3 as p
import os

engine = p.init()
volume = engine.getProperty("volume")

browser = 'start'

print("Do you want to start ?")
start = input()

engine.say("Hello, what's your name?")
engine.runAndWait()
nama = input()

while (start != "no"):
    engine.say("What do you want to do now, sir " + nama + " ?")
    engine.runAndWait()
    todo = input()
    if (todo == "open youtube"):
        engine.say("what do you want to watch, sir?")
        engine.runAndWait()
        game = input()
        engine.say("opening youtube")
        search = game.replace(" ", "+")
        youtube = ' https://www.youtube.com/results?search_query=' + search
        os.system(browser + youtube)
    elif (todo == "play music") :
        engine.say("playing music")
        search = game.replace(" ", "+")
        youtube = ' https://www.youtube.com/watch?v=DDK5lXVuALg'
        os.system(browser + youtube)
    elif (todo == "open google"):
        engine.say("what do you want to search, sir?")
        engine.runAndWait()
        search = input()
        game = search.replace(" ", "+")
        google = ' https://www.google.com/search?q=' + game + '&aqs=chrome.0.35i39j69i59j69i57j0i433j0i131i433j69i61j69i60j69i61.672j0j7&sourceid=chrome&ie=UTF-8'
        os.system(browser + google)
    else :
        engine.say("Sorry sir, " + todo + " is not eligable for now")
        engine.runAndWait()
        
    engine.say("Do you want to continue, sir?")
    engine.runAndWait()
    start = input()