from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()
# lst_elements = driver.find_elements(By.CLASS_NAME,"homeslider-container")
lst_elements = driver.find_elements(By.TAG_NAME,"a")
print(len(lst_elements))
driver.close()