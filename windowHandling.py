import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
window_id = driver.current_window_handle
# print(window_id)
time.sleep(10)

# driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowsIDs = driver.window_handles
# parent_window=windowsIDs[0]
# child_window=windowsIDs[1]
# driver.switch_to.window(child_window)
# print(driver.title)
for win in windowsIDs:
    driver.switch_to.window(win)
    print(driver.title)
    if driver.title == "OrangeHRM":
        driver.close()