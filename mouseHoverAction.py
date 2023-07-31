import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
# move to element
'''
driver.get("https://www.browserstack.com/docs/")
driver.maximize_window()
time.sleep(5)
developers = driver.find_element(By.XPATH,"//a[@id='product-menu-toggle']")
time.sleep(5)
document = driver.find_element(By.XPATH,"(//*[name()='svg'][@alt='Icon for BrowserStack Live'])[1]")

act = ActionChains(driver)
act.move_to_element(developers).move_to_element(document).click().perform()

# drag and drop
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(5)

source_ele = wait.until(EC.presence_of_element_located((By.ID,"box6")))
dest_ele = wait.until((EC.visibility_of_element_located((By.ID,"box106"))))
act=ActionChains(driver)
act.drag_and_drop(source_ele,dest_ele).perform()
time.sleep(5)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
time.sleep(5)

driver.switch_to.frame("iframeResult")
btn_click = driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")
act=ActionChains(driver)
act.double_click(btn_click).click().perform()
time.sleep(5)


driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(5)

lbl_click = driver.find_element(By.XPATH,"//a[text()='Page One']")
act=ActionChains(driver)
act.context_click(lbl_click).click().perform()
time.sleep(5)
'''

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
time.sleep(5)

min_slider = driver.find_element(By.XPATH,"(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")
max_slider = driver.find_element(By.XPATH,"(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]")

print("min_slider: ",min_slider.location)
print("min_slider: ",max_slider.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform() # how many points we need to move from the existing position,We dont want to move y axis
act.drag_and_drop_by_offset(max_slider,-40,0).perform() # move the slider to the left side -x axis
time.sleep(5)
