import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
'''
# scroll down page by pixel
driver.execute_script("window.scrollBy(0,3000)","")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ",value)
time.sleep(10)

# scroll down to the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("NUmber of pixels moved:",value)
time.sleep(10)

# scroll up to the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)
time.sleep(10)
'''
# scroll down till the element located
flag_india = driver.find_element(By.XPATH,"//img[@src='flags-normal/flag-of-India.png']")
driver.execute_script("arguments[0].scrollIntoView();",flag_india)
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)
time.sleep(10)