# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:01:11 2020

@author: Administrator
"""

from selenium import webdriver
import pyttsx3 as p


class movie():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
        
    def movie_review(self,name):
        self.driver.get(url='https://www.google.com/')
        engine = p.init()
        engine.say("opening google")
        engine.runAndWait()
        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        engine.say("searching " + name + "mvie reviews" )
        engine.runAndWait()
        
        search.send_keys(name + " movie reviews")
        submit = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        submit.click()
        engine = p.init()
        engine.say("this the result for " + name + "movie reviews")
        engine.runAndWait()
        
        info_movie = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[1]')
        info_movie = info_movie.text
        engine = p.init()
        engine.say(info_movie)
        engine.runAndWait()
        
        
lisa = movie()
lisa.movie_review("hello world")
        