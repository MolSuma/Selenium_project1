from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
time.sleep(3)
sugestion_box=driver.find_element(By.XPATH,"//input[@id='autocomplete']")
sugestion_box.click()
time.sleep(3)
sugestion_box.send_keys("India")
time.sleep(6)

#enter_data=driver.find_element(By.XPATH,"//div[@id='ui-id-164']")
#enter_data.click()
#time.sleep(6)
