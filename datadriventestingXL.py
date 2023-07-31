#https://www.youtube.com/watch?v=S0WEaFucijs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import excel_utility
import time

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/personal-finance/tools/FD-calculator")
driver.maximize_window()

file ="C:\SeleniumPracticeExcel\FDCalculator.xlsx"
rowcount=excel_utility.get_rowcount(file,"Sheet1")
for row in range(2,rowcount+1):
    xl_amount=excel_utility.read_data(file,"Sheet1",row,1)
    xl_period=excel_utility.read_data(file, "Sheet1", row, 2)
    xl_interest=excel_utility.read_data(file, "Sheet1", row, 3)
    xl_taxRate=excel_utility.read_data(file, "Sheet1", row, 4)
    xl_total_corpus=excel_utility.read_data(file, "Sheet1", row, 5)
    print("xl_total_corpus: ",xl_total_corpus)
    xl_exp_result=excel_utility.read_data(file, "Sheet1", row, 6)

   # driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
    app_investAmt=driver.find_element(By.XPATH,"//input[@id='edulonvalue_1']")
    app_investAmt.clear()
    app_investAmt.send_keys(xl_amount)


    app_period=driver.find_element(By.XPATH,"//input[@id='edulonvalue_2']")
    app_period.clear()
    app_period.send_keys(xl_period)

    app_int=driver.find_element(By.XPATH,"//input[@id='edulonvalue_3']")
    app_int.clear()
    app_int.send_keys(xl_interest)

    app_frq=driver.find_element(By.XPATH,"//span[text()='Monthly']")
    driver.execute_script("arguments[0].click();", app_frq)

    app_taxRate=driver.find_element(By.XPATH,"//input[@id='edulonvalue_4']")
    app_taxRate.clear()
    app_taxRate.send_keys(xl_taxRate)
    time.sleep(5)
    submit=driver.find_element(By.XPATH,"//a[text()='Submit']")
    driver.execute_script("arguments[0].click();", submit)

    app_corpusValue=driver.find_element(By.XPATH,"//div[@class='left_block']/div[3]//span[@class='tc']").text
    print("app_corpusValue",app_corpusValue)
    if float(xl_total_corpus) == float(app_corpusValue):
        print("Test Passed")
        excel_utility.write_data(file,"Sheet1",row,7,"Passed")
        excel_utility.fill_green_colour(file,"Sheet1",row,7)
    else:
        print("Test Failed")
        excel_utility.write_data(file, "Sheet1", row, 7, "Failed")
        excel_utility.fill_red_colour(file,"Sheet1",row,7)
   # app_reset=driver.find_element(By.XPATH,"//a[@id='reset_btn']")
   # driver.execute_script("arguments[0].click()",app_reset)  # to avoid ElementClickInterceptedException, scroll down to the element and click

    driver.close()
