import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup():
    global driver
    ser_obj=Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(10)
    yield
    driver.quit()

@allure.description("Validate OrangeHRM with valid login credentials")
@allure.severity(severity_level="CRITICAL")
def test_validlogin(test_setup):
    driver.find_element(By.XPATH,"//input[@name='username']").clear()
    enter_username("Admin")
    driver.find_element(By.XPATH,"//input[@name='password']").clear()
    enter_password("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    try:
        assert "dashboard" in driver.current_url
    finally:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(),name="Invalid Credentials",attachment_type=allure.attachment_type.PNG)

@allure.description("Validate OrangeHRM with invalid login credentials")
@allure.severity(severity_level="NORMAL")
def test_invalidlogin(test_setup):
    driver.find_element(By.XPATH,"//input[@name='username']").clear()
    enter_username("xyz")
    driver.find_element(By.XPATH,"//input[@name='password']").clear()
    enter_password("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    try:
        assert "dashboard" in driver.current_url
    finally:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(),name="Invalid Credentials",attachment_type=allure.attachment_type.PNG)

@allure.step("Enter username as {0}")
def enter_username(username):
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)

@allure.step("Enter password as {0}")
def enter_password(password):
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
