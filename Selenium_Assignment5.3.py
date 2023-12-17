from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://www.saucedemo.com/')
time.sleep(3)
Current_url1=driver.current_url
print(Current_url1)
#Enter username
username1=driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
time.sleep(3)

# Enter password
username1=driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
time.sleep(3)
#Click login button
login_button=driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(3)
print("---------------")
Current_url2=driver.current_url
print(Current_url2)
#click on twitter link
twitter_link=driver.find_element(By.XPATH,"//a[contains(text(),'LinkedIn')]").click()
time.sleep(7)
