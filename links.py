from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
all_links = driver.find_elements(By.TAG_NAME,'a')
print(len(all_links))
for link in all_links:
    print(link.text)