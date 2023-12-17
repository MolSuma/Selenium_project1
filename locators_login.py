import time

from selenium import webdriver
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
password2=driver.find_element(By.NAME, "password")
password2.send_keys("Admin123")
password2=driver.find_element(By.NAME, "password")
password2.send_keys("Admin123")