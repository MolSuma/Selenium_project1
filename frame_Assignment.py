from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
#find frame
frame=driver.find_element(By.XPATH,"//iframe[@id='courses-iframe']")
frame.click()
driver.execute_script("arguments[0].scrollIntoView", frame)
driver.switch_to.frame(frame)
time.sleep(6)
mentorship=driver.find_element(By.TAG_NAME("mentorship"))
mentorship.click()
time.sleep(3)

