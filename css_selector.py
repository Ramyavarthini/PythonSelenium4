from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.get("https://en-gb.facebook.com/")
driver.maximize_window()
#Tag ID
#driver.find_element(By.CSS_SELECTOR,"input#email").clear()
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("weerrt")

#Tag Class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").clear()
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("weerrt")

#Tag Attribute
#driver.find_element(By.CSS_SELECTOR,"input[placeholder=Password]").clear()
#driver.find_element(By.CSS_SELECTOR,"input[placeholder=Password]").send_keys("rrrrr")

#Tag class attribute
driver.find_element(By.CSS_SELECTOR,"input[placeholder=Password]").clear()
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("fgfhfhfh")

driver.close()