import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import yfinance as yf # to fetch financial data
import ssl
import certifi
import time
import os # to remove created audio files
import pyttsx3

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # initialise a recogniser
#listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en-US")  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak("sorry i can't get it")
        except sr.RequestError:
            speak('sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

def record_audio_sunda(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="su-ID")  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            ngomong('punten, teu ngartos')
        except sr.RequestError:
            ngomong('punten, abdi lelah') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

def speak(audio):
    # get string and make a audio file to be played
    engine = pyttsx3.init('sapi5')
    
    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 150)     # setting up new voice rate
    
    
    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
    
    voices = engine.getProperty('voices') #getting details of the current voice
    engine.setProperty('voice', voices[1].id)
    print(f">> {audio}")
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def ngomong(audio_string):
    tts = gTTS(text=audio_string, lang='su') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    print(f"lisa: {audio_string}") # print what app said
    os.system(audio_file)
    os.remove(audio_file) # remove audio file

def respond(voice_data): 
    # 1: greeting
    if there_exists(['hey','hi','hello',"lisa"]):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        print(greet)
        speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("my name is Lisa")
        else:
            speak("my name is Lisa. what's your name?")

    if there_exists(["call me"]):
        person_name = voice_data.split("me")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    if there_exists(["how are you","how are you doing", "what's up"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}") 

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f"searching {search_term}")
        speak(f'Here is what I found for {search_term} on google')

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    # 7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.lower().split(" of ")[-1].strip() #strip removes whitespace after/before a term in string
        stocks = {
            "apple":"AAPL",
            "microsoft":"MSFT",
            "facebook":"FB",
            "tesla":"TSLA",
            "bitcoin":"BTC-USD"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]
            speak(f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
        except:
            speak('oops, something went wrong')
    if there_exists(["exit", "quit", "goodbye"]):
        speak("going offline")
        exit()
    else:
        speak("pardon me, i can't do it, can you repeat")

def respond_sunda(voice_data): 
    # 1: greeting
    if there_exists(['hey','hi',"lisa"]):
        greetings = [f"aya nu tiasa di bantosan? {person_obj.name}", f"kumaha? {person_obj.name}", f"kah {person_obj.name}", f"peryoi bantosan teu ? {person_obj.name}", f"muhun {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ngomong(greet)
    if there_exists(['assalamualaikum']):
        greetings = [f"wa'alaikumusalam warahmatullahi wabaraktuh"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ngomong(greet)

    # 2: name
    if there_exists(["sareng saha ieu","saha nami na","nami na saha"]):
        if person_obj.name:
            ngomong("nami abdi Lisa")
        else:
            ngomong("nami abdi Lisa. ieu sareng saha?")

    if there_exists(["nami abdi ", "ngaran urang", "urang "]):
        person_name = voice_data.split("urang")[-1].strip()
        ngomong(f"muhun, abdi catatnya {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    if there_exists(["kumaha kabar","keur naon"]):
        ngomong(f"alhamdulillah sae, {person_obj.name} kumaha damang?")

    # 4: time
    if there_exists(["jam","jam sabaraha ayeuna","tingal jam"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        ngomong(time)

    # 5: search google
    if there_exists(["pilarian","pangmilariankeun "]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        ngomong(f'ieu nu kapendak tentang {search_term} di google')

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        ngomong(f'ieu nu kapendak tentang {search_term} di youtube')

    # 7: get stock price
    if there_exists(["harga saham", 'saham']):
        search_term = voice_data.lower().split(" saham ")[-1].strip() #strip removes whitespace after/before a term in string
        stocks = {
            "apple":"AAPL",
            "microsoft":"MSFT",
            "facebook":"FB",
            "tesla":"TSLA",
            "bitcoin":"BTC-USD"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]

            ngomong(f'harga saham {search_term} teh {price} {stock.info["currency"]} {person_obj.name}')
        except:
            ngomong('oops, aya nu lepat')
    if there_exists(["kaluar", "pareum", "dah"]):
        ngomong(f"dadah {person_obj.name} ")
        exit()
    else:
        ngomong('punten, teu tiasa, tiasa ulangi')

# speak('what language you use, say english to english or say bahasa to sunda and bahasa')
pilih = input()
if ('english') in pilih:
    speak("i'm ready")
    person_obj = person()
    while(100):
        voice_data = record_audio() # get the voice input
        respond(voice_data) # respond
if ('bahasa') in pilih:
    ngomong('abdi siap')
    person_obj = person()
    while(1):
        voice_data = record_audio_sunda() # get the voice input
        respond_sunda(voice_data) # respond