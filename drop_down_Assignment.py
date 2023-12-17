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
#dropdown
dropdown1=driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
time.sleep(3)
sel=Select(dropdown1)
time.sleep(3)
#select from dropdown
sel.select_by_visible_text("Option1")
time.sleep(3)
sel.select_by_index(2)
time.sleep(3)
sel.select_by_visible_text("Option3")
time.sleep(3)