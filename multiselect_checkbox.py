from selenium import webdriver
import time
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://the-internet.herokuapp.com/checkboxes')
time.sleep(3)
#unlcick chcek box2:
checkbox2=driver.find_element(By.XPATH,"//body/div[2]/div[1]/div[1]/form[1]/input[2]")
checkbox2.click()
time.sleep(3)
#multiselect use for loop
check_list=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
time.sleep(3)
for i in check_list:
    time.sleep(3)
    i.click()

driver.close()
