from selenium import webdriver
from selenium.webdriver.common.by import By
import time
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
# get url
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
data=driver.find_element(By.XPATH,"//input[@id='name']")
data.click()
data.send_keys("Suma")
alert=driver.find_element(By.XPATH,"//input[@id='alertbtn']")
alert.click()
time.sleep(3)

