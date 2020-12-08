# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:01:23 2020

@author: Administrator
"""

import speech_recognition as sr
from time import ctime
import os
from gtts import gTTS


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system(" audio.mp3")

