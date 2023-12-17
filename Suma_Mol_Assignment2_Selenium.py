from selenium import webdriver
import  time
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://www.saucedemo.com/v1/index.html')
time.sleep(1)
#get title
title1=driver.title
print(title1)
#Enter username
username1=driver.find_element(By.ID, "user-name")
username1.send_keys("standard_user")
#Enter password
password1=driver.find_element(By.ID, "password")
password1.send_keys("secret_sauce")
#Click login button
login_button1=driver.find_element(By.ID,"login-button")
login_button1.click()
#ger current url
current_url1=driver.current_url
print(current_url1)
time.sleep(2)
#Navigate back
driver.back()
#get new url of current page
new_url1=driver.current_url
print("-----------------")
print(new_url1)
driver.close()