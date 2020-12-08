# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:01:56 2020

@author: Administrator
"""

from selenium import webdriver
import pyttsx3 as p


class info():
    
    #opening wikipedia
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
    
        
    # search in wikipedia
    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        #find = self.driver.
        search.click()
        search.send_keys(query)
        
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()   
        
        info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[3]')
        readable_text = info.text
        engine = p.init()
        engine.say(readable_text)
        engine.runAndWait()
        
#lisa = info()
#lisa.get_info("elon musk")