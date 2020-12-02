# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:35:51 2020

@author: Administrator
"""

from selenium import webdriver
import pyttsx3 as p

engine = p.init()


class youtube():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
        
    def play(self,name):
        engine.say("searching video " + name)
        engine.runAndWait()
        self.name = name
        self.driver.get(url='https://www.youtube.com/results?search_query=' + name)
        
        
        
        play = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        play.click()
        engine.say("playing first video for " + name)
        engine.runAndWait()
        

        
        
lisa = youtube()
lisa.play("python")
        

