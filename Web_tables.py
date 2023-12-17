import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)#Cell data for a particular webelement:

driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/tables')
time.sleep(3)
#To fetch table:

table=driver.find_elements(By.XPATH,"//table[@id='table1']")

rows=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr")
print(rows)

columns=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr/td")
print(columns)

#Cell data for a particular webelement:
celldata=driver.find_element(By.XPATH,"//table[@id='table1']/tbody/tr/td")
text=celldata.text
print(text)

