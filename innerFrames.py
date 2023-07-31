import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service = serv_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

# Since id/name is not available, we pass webelement to the frame
parent_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(parent_frame)

inner_frame = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome Ramya")
time.sleep(10)

# If we want to navigate to the parent frame again
driver.switch_to.parent_frame()