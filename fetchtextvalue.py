import time

from selenium import webdriver
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/notification_message_rendered')
time.sleep(3)
checkbox=driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/p[1]")
text_value=checkbox.text
time.sleep(3)
print(text_value)
