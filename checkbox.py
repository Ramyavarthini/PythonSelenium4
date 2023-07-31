from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation/")
driver.maximize_window()
'''
# To find a specific chekbox
driver.find_element(By.ID,"wednesday").click()
time.sleep(10)'''

# To select all checkbox
checkboxes = driver.find_elements(By.XPATH,"//input[contains(@id,'day')]")
print(len(checkboxes))
time.sleep(5)

#To select multiple textboxes
'''
# Approach 1
for checkbox in checkboxes:
    checkbox.click()'''
'''
# Approach 2
for i in range(len(checkboxes)):
    checkboxes[i].click()'''
'''
# Approach 3 - To select multiple specific checkboxes by choice
for checkbox in checkboxes:
    weekname = checkbox.get_attribute("id")
    if weekname == 'tuesday' or weekname == 'thursday':
        checkbox.click()
time.sleep(10)'''
'''
#Approach 4  - select last 2 check boxes
for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()
time.sleep(5)'''
'''
#Approach 5  - select first 2 check boxes
for i in range(0,2):
    checkboxes[i].click()
time.sleep(5)'''

#Approach 6  - clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()