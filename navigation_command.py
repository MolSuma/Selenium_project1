#Navigating commands: To navigate front, back, refresh
import time

from selenium import webdriver

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()


#driver commands
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(3)
#navigate back
driver.back()
time.sleep(3)
#navigate front
driver.forward()
#for refresh
driver.refresh()
time.sleep(3)




driver.close()