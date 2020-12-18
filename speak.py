import pyttsx3
from gtts import gTTS
import random
import os

    
engine = pyttsx3.init('sapi5')

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

voices = engine.getProperty('voices') #getting details of the current voice
engine.setProperty('voice', voices[1].id)

def speak(audio):
   engine.say(audio) 
   engine.runAndWait() #Without this command, speech will not be audible to us.
      
# speak("Hello raka") 
def ngomong(audio_string):
    tts = gTTS(text=audio_string, lang='su') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    print(f"lisa: {audio_string}") # print what app said
    os.system(audio_file)
    os.remove(audio_file) # remove audio file

