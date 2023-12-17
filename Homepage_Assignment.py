from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
#click on home page
home_page=driver.find_element(By.XPATH, " //button[contains(text(),'Home')]").click()
time.sleep(3)
current_url=driver.current_url
print(current_url)
fetch_value=driver.find_element(By.XPATH,"//body/div[1]/div[2]/section[3]/div[1]/div[1]")
text_value=fetch_value.text
time.sleep(3)
print(text_value)