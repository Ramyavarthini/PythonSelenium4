# https://www.youtube.com/watch?v=NA1uXmBV_BQ
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location =os.getcwd()  # to get current working directory, it will dynamicaly get the path


# To download a file in Chrome browser
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

    # If we want to download into desired location, key value pair
    # preferences = {"download.default_directory":"C:\Users\Ramya\PycharmProjects\selenium4Project\practice_downloads"}

    # to download into the current working directory, key value pair
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions() # bracket is important
    ops.add_experimental_option("prefs",preferences)

    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

#   -------------------------------------------------------------------------------------------------

# To download a file in Edge browser
def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")

    # If we want to download into desired location, key value pair
    # preferences = {"download.default_directory":"C:\Users\Ramya\PycharmProjects\selenium4Project\practice_downloads"}

    # to download into the current working directory, key value pair
    preferences = {"download.default_directory": location}
    ops = webdriver.EdgeOptions() # bracket is important
    ops.add_experimental_option("prefs",preferences)

    driver = webdriver.Edge(service=serv_obj,options=ops)
    return driver

# ----------------------------------------------------------------------------------------

# To download a file in Firefox browser
def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\Drivers\geckodriver-v0.33.0-win32\geckodriver.exe")
    ops = webdriver.FirefoxOptions() # bracket is important

    #To disable the 'File Download' option window
    # "application/msword" is MIME Type, to which type the document should be downloaded, to find more MIME Types list
    # https://www.sitepoint.com/mime-types-complete-list/
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    # To download the file in the desired location
    ops.set_preference("browser.download.folderList",2) # 0-desktop, 1-downloads, 2-desired location
    ops.set_preference("browser.download.dir",location)

    driver = webdriver.Firefox(service=serv_obj,options=ops)
    return driver


# Automation to download the file - start from here only, we have to call any browser setup method
# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(15) # must need to wait to complete the download