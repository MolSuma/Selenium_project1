from selenium import webdriver
import time
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://the-internet.herokuapp.com/checkboxes')
time.sleep(3)

driver.get_screenshot_as_file("C:\\Users\\user\\PycharmProjects\\SeleniumProject2\\screenshots\\file3.png")
driver.save_screenshot("file2.png")