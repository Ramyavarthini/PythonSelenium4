import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.ID,"dob").click()
month_dropdown = driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']")
sel_month_obj=Select(month_dropdown)
sel_month_obj.select_by_visible_text("Aug")
year_dropdown = driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']")
sel_year_obj = Select(year_dropdown)
sel_year_obj.select_by_visible_text("2008")
all_dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td//a")
for ele in all_dates:
    if ele.text == '28':
        ele.click()
        break
time.sleep(10)
