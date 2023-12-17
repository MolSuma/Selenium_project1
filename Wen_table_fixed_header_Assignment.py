from selenium import webdriver
from selenium.webdriver.common.by import By
import time
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
#click on web table with fixed header and get all data
table_header=driver.find_element(By.XPATH,"//body/div[3]/div[2]/fieldset[2]/div[1]")
table_header.click()
driver.execute_script("arguments[0].ScrollIntoView", table_header)
time.sleep(3)
header_text=table_header.text
time.sleep(3)
print(header_text)
time.sleep(3)
print("-------------------------------------------")
# get specified cell data
cell_data=driver.find_element(By.XPATH,"//table[@id='product']/tbody/tr[1]/td[1]")
time.sleep(2)
cell_text=cell_data.text
print(cell_text)