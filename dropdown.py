from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
drp_ele = driver.find_element(By.ID,"input-country")
select_obj = Select(drp_ele)

select_obj.select_by_visible_text('India')
select_obj.select_by_value('10')
select_obj.select_by_index(1)
# To select all options in the dropdown

all_options = select_obj.options
for opt in all_options:
    print(opt.text)

# select options from the dropdown without builtin methods
for opt in all_options:
    if opt.text == 'India':
        opt.click()
        break

# If the node has no select tag,
drp_elements = driver.find_elements(By.XPATH,"//*[@id='input-country']/option")
print(len(drp_elements))