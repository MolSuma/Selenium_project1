from selenium import webdriver
import time
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://the-internet.herokuapp.com/checkboxes')
time.sleep(1)
#unlcick chcek box2:
checkbox2=driver.find_element(By.XPATH,"//body/div[2]/div[1]/div[1]/form[1]/input[2]")
checkbox2.click()
#click checkbox1
checkbox1=driver.find_element(By.XPATH,"//body/div[2]/div[1]/div[1]/form[1]/input[1]")
checkbox1.click()
time.sleep(1)