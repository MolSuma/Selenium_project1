import time

from selenium import webdriver
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.forward()
time.sleep(2)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.close()
