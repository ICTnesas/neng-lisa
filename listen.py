import speech_recognition as sr
# from main import *
from speak import speak

r =sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        #  if ask:
        #      speak(ask)
                audio = r.listen(source)  # listen for the audio via source
                voice_data = ''
                try:
                        voice_data = r.recognize_google(audio, language="en-US")  # convert audio to text
                        #voice_data = r.recognize_google(audio, language="su-ID")  # convert audio to text
                except sr.UnknownValueError: # error: recognizer does not understand
                        speak('I did not get that')
                except sr.RequestError:
                        speak('Sorry, the service is down') # error: recognizer is not connected
                        print(f">> {voice_data.lower()}") # print what user said
                        return voice_data.lower()

# record_audio('')
