#https://www.youtube.com/watch?v=NxTHamJK-UI
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
wait = WebDriverWait(driver,10,poll_frequency=2)
driver.find_element(By.XPATH,"//span[@aria-labelledby='select2-reasondummy-container']").click()
# driver.find_element(By.XPATH,"//li[text()='Visa extension']").click()  or
lst_visareasons= driver.find_elements(By.XPATH,"//ul[@id='select2-reasondummy-results']/li")
for ele_reason in lst_visareasons:
    if ele_reason.text=='Visa extension':
        ele_reason.click()
        break
time.sleep(10)