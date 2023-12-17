from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
#checkbox:
checklist1=driver.find_elements(By.XPATH," //input[@type='checkbox']")
time.sleep(3)
for i in checklist1:
    time.sleep(3)
    i.click()
    time.sleep(3)

driver.close()
