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


def lisa(data):
    if "how are you" in data:
        speak("I'm fine")
    if "wikipedia" in data:
        lisa = listen
        lisa.recordAudio()
        
        lisa.get_info()
        

# initialization
speak("Hai, what can i do for you?")
while 1:
    data = listen
    data.recordAudio()
    lisa(data)