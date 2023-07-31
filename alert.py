import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
driver.implicitly_wait(10)
alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys('This is for practice')
alert_window.accept()
#alert_window.dismiss()
time.sleep(10)