#   Copyright (c) 2021.
#   Version : 1.0.2
#   Script Author : Sushen Biswas
#
#   Sushen Biswas Github Link : https://github.com/sushen
#
#   !/usr/bin/env python
#   coding: utf-8

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
from dotenv import load_dotenv,find_dotenv
import os
load_dotenv(find_dotenv()) 

# UserCredintials(EmailandPassword)
# make an .env file With your Credintials
Email = os.environ.get("EMAIL")
Password = os.environ.get("PASSWORD")


#TODO: Make a Long List of keyword
all_keys = ["username","password","country","income","funny"]


chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--incognito")
driver = webdriver.Chrome("./chromedriver.exe",chrome_options=chrome_options)
# firefox browser driver added
# driver=webdriver.Firefox(executable_path='./geckodriver.exe')

chrome_options.add_argument("user-data-dir=chrome-data")
driver.implicitly_wait(25)  # seconds



# What will be searched

actions = ActionChains(driver) 

# Time waiting for page

waiting_for_page = 10

driver.get("https://engine.presearch.org")
time.sleep(2)

#TODO: Make a login strong system in environment veriable

print(input("Enter your Username and Password Menually then enter 1: "))
driver.get("https://presearch.org")
print(input("Enter your Username and Password Menually then enter 1: "))

driver.find_element_by_id("search").send_keys(random.choice(all_keys))
driver.find_element_by_id("search").send_keys(Keys.ENTER)

 
time.sleep(2)

actions.send_keys(Keys.TAB * 10)
search_key = random.choice(all_keys)
actions.send_keys(search_key)
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(20)
prev_search_key = search_key

while True :
    for i in range(len(prev_search_key)):
        actions.send_keys(Keys.BACK_SPACE)

    time.sleep(4)
    search_key = random.choice(all_keys)
    print(search_key)
    actions.send_keys(search_key)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    prev_search_key = search_key
    time.sleep(4)
   
#TODO: Click the search resust to make it more human



# driver.find_element_by_id("token-animation").click()
# print(driver.find_element_by_xpath("//button[@type='submit']"))
# driver.find_element_by_xpath("//input[@type='submit']").click();
# print(input("Enter your Username and Password Menually then enter 1: "))

# driver.execute_script("window.open('https://engine.presearch.org');")
# driver.close()
# driver.get("https://presearch.org")
# driver.find_element_by_id("search").send_keys("username")
# driver.find_element_by_id("search").send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()