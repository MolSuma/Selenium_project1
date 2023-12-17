import time

from selenium import webdriver
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/')
time.sleep(3)
infinite_tab=driver.find_element(By.XPATH,"//a[contains(text(),'Infinite Scroll')]")
time.sleep(3)
#
driver.execute_script("arguments[0].scrollIntoView()", infinite_tab)
time.sleep(3)
infinite_tab.click()