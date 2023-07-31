from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#This will disbale the popup
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj,options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()