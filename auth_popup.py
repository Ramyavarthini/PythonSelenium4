import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# driver.get("http://the-internet.herokuapp.com/basic_auth")
# To handle authendication popup , we have to inject username and password to the url of that webpage
# syntax: http://username:password@test.com
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(10)
driver.close()