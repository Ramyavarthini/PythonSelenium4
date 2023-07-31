import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
wait = WebDriverWait(driver,30,poll_frequency=2,ignored_exceptions=[TimeoutException])
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
# time.sleep(5)
ele_frame = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(ele_frame)
# driver.find_element(By.ID,"datepicker").click()
try:
    txt_date = wait.until(EC.element_to_be_clickable((By.ID,"datepicker")))
    txt_date.click()
except:
    None

exp_month = "April"
exp_year = "2024"
exp_date = "20"
while True:
    act_month = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    act_year = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if act_month == exp_month and act_year == exp_year:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  # Next arrow clicked

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr//a")
for ele in dates:
    if ele.text == exp_date:  # ele.text is important
        ele.click()
        break
time.sleep(10)