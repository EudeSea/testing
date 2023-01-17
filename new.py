import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/Eudyy/Videos/geckodriver.exe")
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options, service=service_obj)
driver.get("http://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggieWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")
browserList = []
for ele in veggieWebElement:
    browserList.append(ele.text)

originalList = browserList.copy()
browserList.sort()

assert originalList == browserList
