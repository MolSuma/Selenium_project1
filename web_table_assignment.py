import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
#find table
table=driver.find_elements(By.XPATH,"//table[@name='courses']")
rows=driver.find_elements(By.XPATH,"//table[@name='courses']/tbody/tr")
time.sleep(3)
print(rows)
columns=driver.find_element(By.XPATH,"//table[@name='courses']/tbody/tr/td")
time.sleep(3)
print(columns)
#cell data
cell_data=driver.find_element(By.XPATH,"//table[@name='courses']/tbody/tr[3]/td[2]")
#scroll to view
driver.execute_script("arguments[0].ScrollIntoView", cell_data)
cell_data.click()
time.sleep(3)
text_value=cell_data.text
time.sleep(3)
print(text_value)
