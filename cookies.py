from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
'''
# get cookies information
cookies=driver.get_cookies()
print(len(cookies))
for c in cookies:
    print(c)

# add cookie
driver.add_cookie({"name":"ramya","value":"223234"})
new_cookies = driver.get_cookies()
print(len(new_cookies))
for c in new_cookies:
    print(c)

# delete a specific cookie
driver.delete_cookie('_ga')  #'name'='_ga'
cookies=driver.get_cookies()
print(len(cookies))
for c in cookies:
    print(c)
'''
#delete all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))