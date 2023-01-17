from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/Eudyy/Videos/geckodriver.exe")
options = Options()
#options.add_argument("headless")
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox(options=options, service=service_obj)
driver.get("http://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowOpened = driver.window_handles

driver.switch_to.window(windowOpened[1])

allText = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
mailx = allText.split()
mail = mailx[4]

driver.switch_to.window(windowOpened[0])

driver.find_element(By.XPATH,"//input[@id='username']").send_keys(mail)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Passw0rd")
driver.find_element(By.CSS_SELECTOR, ".checkmark").click()
driver.find_element(By.XPATH, "//input[@id='terms']").click()
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()

