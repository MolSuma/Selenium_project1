import status
from selenium import webdriver
import time
import selenium.webdriver.common.alert
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://automationexercise.com/contact_us')
time.sleep(1)
#Enter name
name1=driver.find_element(By.XPATH,"//input[@data-qa='name']")
name1.click()
name1.send_keys("Suma")
time.sleep(1)
#Enter email
email1=driver.find_element(By.XPATH,"//input[@data-qa='email']")
email1.click()
email1.send_keys("sumamol27@gmail.com")
time.sleep(1)
#Enter subject
subject1=driver.find_element(By.XPATH,"//input[@data-qa='subject']")
subject1.click()
subject1.send_keys("Selenium")
time.sleep(1)
#Enter message
message1=driver.find_element(By.ID,"message")
message1.click()
message1.send_keys("Automating web page")
time.sleep(1)
#upload file:
choose_file=driver.find_element(By.XPATH,"//input[@type='file']")
time.sleep(2)
choose_file.send_keys("D:\\Testing\\Demo_file1.txt")
time.sleep(3)
#Click submit button
submit_button1=driver.find_element(By.XPATH,"//input[@type='submit']")
submit_button1.click()
time.sleep(1)


alert = driver.switch_to.alert.accept()
#confirmation message
confirmation=driver.find_element(By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[1]/div[2]").is_displayed()
time.sleep(3)


