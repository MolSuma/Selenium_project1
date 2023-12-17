from selenium import webdriver
import time
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#sign up into new account:
driver.get('https://automationexercise.com/login')
time.sleep(1)
#Enter email
email=driver.find_element(By.XPATH,"//input[@data-qa='login-email']")
email.send_keys("sumamol27@gmail.com")
time.sleep(1)
# Enter password
new_email=driver.find_element(By.XPATH,"//input[@data-qa='login-password']")
new_email.send_keys("Sanashree@123")
time.sleep(1)
#click signup
sign_up=driver.find_element(By.XPATH,"//button[contains(text(),'Login')]")
sign_up.click()
#current url
current_url1=driver.current_url
print(current_url1)
time.sleep(1)
#Navigate back
driver.back()
#get new url of current page
new_url1=driver.current_url
print("-----------------")
print(new_url1)
driver.close()