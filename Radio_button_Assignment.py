from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
#click on radio button
radio_button=driver.find_elements(By.XPATH," //input[@type='radio']")
for i in radio_button:
    time.sleep(3)
    i.click()
    time.sleep(3)