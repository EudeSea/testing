import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/Eudyy/Videos/geckodriver.exe")
#driver = webdriver.Chrome(service=service_obj)

#caminho da instalacao do firefox, colocar o option no webdriver como parametro
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox(options=options, service=service_obj)
#driver.get("https://rahulshettyacademy.com/angularpractice")
driver.get("http://nuvem.jembi.org:11080/")

driver.find_element(By.XPATH, '//a[@href="/User/Login"]').click()
driver.find_element(By.NAME,"UserName").send_keys("conservador1")
driver.find_element(By.ID, "Password").send_keys("Passw0rd")
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()= 'Conecte-Se']").click() #igual a linha 21
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME, "fa-users").click()
driver.implicitly_wait(6)
driver.find_element(By.XPATH, '//a[@href="/Birth/Create"]').click()
driver.implicitly_wait(5)
driver.find_element(By.NAME,"othernames")
#driver.implicitly_wait(5)
nome = driver.find_element(By.XPATH, "//input[@id='othernames']")
nome.click()
nome.clear()
nome.send_keys("Olinda Alfiado")
apelido = driver.find_element(By.NAME,"surname")
apelido.click()
apelido.clear()
apelido.send_keys("Zunguze")
#driver.execute_script("document.getElementsByName('q')[0].value='Zunguze'")
driver.find_element(By.ID, "dateofbirth").click()
ano = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
ano.select_by_value("2019")
mes = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
mes.select_by_value("9")
dia = driver.find_element(By.XPATH, "//a[normalize-space()='11']")
dia.click()
driver.implicitly_wait(10)
provincia = driver.find_element(By.CSS_SELECTOR, "#provinceid")
try:

    assert provincia.text[0] == "-"
    
except Exception as e:
    print(e)

try:
    assert apelido =="Zunguze"
except Exception as e:
    print(e)





#//a[normalize-space()='10']
#var=driver.find_element(By.XPATH, "//button[@type='submit']").text()
#assert "sss" in var
#driver.find_element(By.NAME,"name").send_keys("eude")
#driver.find_element(By.NAME,"email").send_keys("eudeeliascumbe@gmail.com")
#driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
#driver.find_element(By.ID, "exampleCheck1").click()










#driver.maximize_window()
#driver.get("https://jw.org")
#driver.back()
#driver.set_window_size(720,540)
#driver.close()
#print(driver.current_url)
#assert (driver.title == "Rahul Shetty Academy")
