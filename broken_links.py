import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
all_links = driver.find_elements(By.TAG_NAME,'a')
count=0

for link in all_links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)  # requests module will take the url to the server and get the response
    except:
        None

    if res.status_code>=400:    # response contains more information
        print(url,"is a broken link")
        count+=1
    else:
        print(url,"is a valid link")

print('number of broken link is',count)