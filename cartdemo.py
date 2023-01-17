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
driver.get("http://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count =len(results)
assert count >0
Lista_esperada = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
lista_actual = []
for result in results:
    lista_actual.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert lista_actual == Lista_esperada
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
message = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
totamt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
discamt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert message == "Code applied ..!"
try:
 assert totamt > discamt
except Exception as e:
    print("erro de calculo")

driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
sel = Select(driver.find_element(By.XPATH, "//div[@class='wrapperTwo']//div//select"))
sel.select_by_value("Mozambique")
driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()

#Thank you, your order has been placed successfully You'll be redirected to Home page shortly!!