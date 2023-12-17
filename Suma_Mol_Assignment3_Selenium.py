from selenium import webdriver
import time
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#sign up into new account:
driver.get('https://automationexercise.com/login')
time.sleep(1)
#Enter name
new_name=driver.find_element(By.XPATH,"//input[@data-qa='signup-name']")
new_name.send_keys("Suma Mol M S")
time.sleep(1)
# Enter email address
new_email=driver.find_element(By.XPATH,"//input[@data-qa='signup-email']")
new_email.send_keys("sumamol27@gmail.com")
time.sleep(1)
#click signup
sign_up=driver.find_element(By.XPATH,"//button[contains(text(),'Signup')]")
sign_up.click()
#current url
current_url1=driver.current_url
print(current_url1)
time.sleep(1)
#genfer
title=driver.find_element(By.ID,"id_gender2")
title.click()
time.sleep(1)
#password
title=driver.find_element(By.ID,"password")
title.click()
title.send_keys("Sanashree@123")
time.sleep(1)
#first name
firstname1=driver.find_element(By.ID,"first_name")
firstname1.click()
firstname1.send_keys("Suma")
time.sleep(1)
#lastname1
lastname1=driver.find_element(By.ID,"last_name")
lastname1.click()
lastname1.send_keys("Mol M S")
time.sleep(1)
#address1
address1=driver.find_element(By.ID,"address1")
address1.click()
address1.send_keys("SGS Aditiya villa")
time.sleep(1)
#address2
address2=driver.find_element(By.ID,"address2")
address2.click()
address2.send_keys("Hosur")
time.sleep(1)
#state
state1=driver.find_element(By.ID,"state")
state1.click()
state1.send_keys("Tamil Nadu")
time.sleep(1)
#city
city1=driver.find_element(By.ID,"city")
city1.click()
city1.send_keys("Hosur")
time.sleep(1)
#zipcode
zipcode1=driver.find_element(By.ID,"zipcode")
zipcode1.click()
zipcode1.send_keys("635126")
time.sleep(1)
#mobile number
mobile_number1=driver.find_element(By.ID,"mobile_number")
mobile_number1.click()
mobile_number1.send_keys("7708413343")
time.sleep(1)
#create account
create_account=driver.find_element(By.XPATH,"//button[contains(text(),'Create Account')]")
create_account.click()



driver.close()