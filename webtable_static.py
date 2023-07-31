# 1) find number of rows & columns
# 2) Read specific row and column
# 3) Read all the rows and columns data
# 4) Read data based on condition [List books name whose author is Mukesh]
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# no of columns
no_columns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(no_columns)

# no of rows
no_rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print(no_rows)
'''
# 2) Read specific row and column
author_name = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[4]/td[2]").text
print(author_name) '''

# 3) Read all the rows and columns data
for r in range(2,no_rows+1):  #first row is the header
    for c in range(1,no_columns+1):
        table_data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(table_data,end="          ")  # to create a space in each column
    print()

# 4) Read data based on condition [List books name and price whose author is Mukesh]
for r in range(2,no_rows+1):
    author_name = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if author_name == 'Mukesh':
        book_name = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        print(book_name,'   ',author_name,'    ',price)
