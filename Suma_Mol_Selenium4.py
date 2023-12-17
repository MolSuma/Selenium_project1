from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers')
time.sleep(3)
Current_url1=driver.current_url
print(Current_url1)
#Enter username
username1=driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(3)
# Enter password
username1=driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(3)
#Click login button
login_button=driver.find_element(By.XPATH, "//button [text()=' Login ']").click()
time.sleep(5)
print("---------------")
Current_url2=driver.current_url
print(Current_url2)
#click admin button
#admin_button=driver.find_element(By.LINK_TEXT, "/web/index.php/admin/viewAdminModule").click()
#time.sleep(3)oxd-icon oxd-main-menu-item--icon


