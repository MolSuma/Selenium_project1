import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)

driver.maximize_window()

# implicit wait
driver.implicitly_wait(3)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

# explicit wait
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'username']")))

element.click()

name = driver.find_element(By.NAME, "username")
name.send_keys("Admin")

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

login_button = driver.find_element(By.XPATH, "//button[@type = 'submit']")
login_button.click()

driver.close()