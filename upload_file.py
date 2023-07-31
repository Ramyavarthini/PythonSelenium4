# https://www.youtube.com/watch?v=NA1uXmBV_BQ
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.foundit.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='heroSection-buttonContainer_secondaryBtn__text']").click()
driver.find_element(By.ID,"file-upload").send_keys("E:\Ramya\Job\Interview\InterviewQuestions.txt")
driver.find_element(By.XPATH,"//span[@class='action-cta']").click()
time.sleep(10)