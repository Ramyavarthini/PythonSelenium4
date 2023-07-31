from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
# import time #pyhton provide this 'time' module

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
# driver.implicitly_wait(10)
wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions= [NoSuchElementException,Exception])
driver.get("https://www.google.com/")
driver.maximize_window()
search_txtbox = driver.find_element(By.NAME,'q')
search_txtbox.send_keys("selenium")
search_txtbox.submit()
# time.sleep(10)
searchlink = wait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()


