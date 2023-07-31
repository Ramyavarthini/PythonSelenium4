import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedrreiver.exe")
driver=webdriver.Chrome(service=serv_obj)
'''
# This is for, right click on an element to open the web page in a new Tab to avoid open in the same page, then we can see both the windows
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
register_link=Keys.CONTROL+Keys.ENTER   # Keys.ENTER or Keys.RETURN both are same but in some browser either one will work
driver.find_element(By.LINK_TEXT,"Register").send_keys(register_link)
time.sleep(10)
'''
'''
# new feature in selenium 4
# To open multiple applications in multiple tabs in a same browser window 
driver.get("https://www.opencart.com/")
driver.maximize_window()
driver.switch_to.new_window("tab")
driver.get("https://www.orangehrm.com/")
driver.maximize_window()
'''
# new feature in selenium 4
# To open multiple applications in multiple windows with the same  kind kind of browser
driver.get("https://www.opencart.com/")
driver.maximize_window()
driver.switch_to.new_window("window")
driver.get("https://www.orangehrm.com/")
driver.maximize_window()