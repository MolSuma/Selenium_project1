from selenium import webdriver
import time
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://jqueryui.com/checkboxradio/')
time.sleep(1)
#unlcick chcek box2:
radiobutton=driver.find_element(By.ID,"//input[@id='radio-1']")
radiobutton.click()