from selenium import webdriver

def headlessmode_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
    ops=webdriver.ChromeOptions()
    # ops.headless=True                # selenium 3
    ops.add_argument('--headless')     # selenium 4
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

def headlessmode_edge():
    from selenium.webdriver.edge.service import Service
    serv_obj=Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
    ops=webdriver.EdgeOptions()
    # ops.headless=True                # selenium 3
    ops.add_argument('--headless')     # selenium 4
    driver = webdriver.Edge(service=serv_obj,options=ops)
    return driver

def headlessmode_fireFox():
    from selenium.webdriver.firefox.service import Service
    serv_obj=Service("C:\Drivers\geckodriver-v0.33.0-win32\geckodriver.exe")
    ops=webdriver.FirefoxOptions()
    # ops.headless=True                # selenium 3
    ops.add_argument('--headless')     # selenium 4
    driver = webdriver.Firefox(service=serv_obj,options=ops)
    return driver

# driver=headlessmode_chrome()
# driver = headlessmode_edge()
driver=headlessmode_fireFox()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()