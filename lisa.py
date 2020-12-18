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
from speak import speak
from listen import record_audio
from person import person
from main import *

        

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
        
def respond(voice_data): 
    #def respond(voice_data):
        #greeting
    if there_exists(['hey', 'hi', 'hello']):
            greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
            greet = greetings[random.randint(0,len(greetings)-1)]
            speak(greet)
            ngomong('kah')
    if there_exists(['assalamualaikum']):
            greetings = [f"Waalaikumusalam warrahmatullahi wabarakatuh {person_obj.name}"]
            greet = greetings[random.randint(0,len(greetings)-1)]
            speak(greet)
    if there_exists(["how are you","how are you doing"]):
            speak(f"I'm very well, thanks for asking {person_obj.name}")
        
        # 2: name
    if there_exists(["what is your name","what's your name","tell me your name", "ngaran maneh saha", "kamu siapa"]):
            if person_obj.name:
                speak("my name is lisa")
            else:
                speak("my name is lisa. what's your name?")
        
    if there_exists(["my name is", "ngaran urang ", "nami simkuring", "nama saya"]):
            person_name = voice_data.split("is")[-1].strip()
            speak(f"okay, i will remember that {person_name}")
            person_obj.setName(person_name) # remember name in person object
            
        # 4: time
    if there_exists(["what's the time","tell me the time","what time is it", "jam sabaraha ayeuna", "jam berapa sekarang"]):
            time = ctime().split(" ")[3].split(":")[0:2]
            if time[0] == "00":
                hours = '12'
            else:
                hours = time[0]
            minutes = time[1]
            time = f'{hours} {minutes}'
            speak(time)
        
        # 5: search google
    if there_exists(["search for", "tolong cari","pilarian"]) and 'youtube' not in voice_data:
            search_term = voice_data.split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on google')
        
        # 6: search youtube
    if there_exists(["youtube", "buka youtube"]):
            search_term = voice_data.split("for")[-1]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on youtube')
        
        # 7: get stock price
    if there_exists(["price of", "harga saham"]):
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
    if there_exists(["exit", "quit", "goodbye", "dah", "mati"]):
            speak("going offline")
            exit()
