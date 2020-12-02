# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:48:31 2020

@author: Administrator
"""

import pyttsx3 as p
from speak import *

engine = p.init()

caracter = {"Adrian" : "He is very lazy, that's was why he create me",
            "raka" : "He is ",
            "hamdan" : "he is ",
            "luthfi" : "he is "}

def mean(name):
    if name in caracter:
        res = caracter[name]
        #engine.say(res)
        #engine.runAndWait()
        speak(res)
       
        

