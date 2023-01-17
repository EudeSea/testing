from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

service_obj = Service(r"C:\Users\Karuna\Desktop\chrome\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME,"blinkingText").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
message =driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.NAME,"username").send_keys(message)
driver.find_element(By.NAME,"password").send_keys("ashwin@99")
driver.find_element(By.CLASS_NAME,"form-control").click()
driver.find_element(By.XPATH,"//option[@value='stud']").click()
driver.find_element(By.NAME,"terms").click()
driver.find_element(By.NAME,"signin").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert")))
print(driver.find_element(By.CLASS_NAME, "alert").text)