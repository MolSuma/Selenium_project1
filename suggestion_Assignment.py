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
suggestion_box=driver.find_element(By.XPATH,"//input[@id='autocomplete']")
time.sleep(3)
sel=Select(suggestion_box)
time.sleep(3)
