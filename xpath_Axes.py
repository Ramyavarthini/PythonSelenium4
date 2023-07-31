from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

#text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'Dabur India')]//parent::td").text
#print(text_msg)

# lst_elements = driver.find_elements(By.XPATH,"//a[contains(text(),'Dabur India')]//ancestor::tr//child::td")
# print(len(lst_elements))
# for ele in lst_elements:
#     print(ele.text)

# lst_elements = driver.find_elements(By.XPATH,"//a[contains(text(),'Dabur India')]/ancestor::tr/descendant::*")
# lst_elements = driver.find_elements(By.XPATH,"//a[contains(text(),'Dabur India')]/ancestor::tr/descendant::td[1][a[contains(text(),'Dabur India')]]

# lst_elements = driver.find_elements(By.XPATH,"//a[contains(text(),'Dabur India')]/ancestor::tr/following::*")
# lst_elements = driver.find_elements(By.XPATH,"//a[contains(text(),'Dabur India')]/ancestor::tr/following-sibling::*")

# lst_elements = driver.find_elements(By.XPATH,"//a[contains(text(),'Dabur India')]/ancestor::tr/preceding::*")
#lst_elements = driver.find_elements(By.XPATH,"//a[contains(text(),'Dabur India')]/ancestor::tr/preceding-sibling::*")

driver.close()