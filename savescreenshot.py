from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
location = os.getcwd()

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# the following both are same
driver.save_screenshot(location+"\\practice_screenshot.png")
#driver.get_screenshot_as_file(location+"\\practice_screenshot.png")

'''
# the following both will store the screenshots in the binary format. we need to decode to read the file
driver.get_screenshot_as_png(location+"\\practice_screenshot.png")
driver.get_screenshot_as_base64(location+"\\practice_screenshot.png")
'''