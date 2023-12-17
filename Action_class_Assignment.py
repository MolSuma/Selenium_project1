from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
#impoert action class for mouse related operations
act=ActionChains(driver)
#find locators
mouse_hover=driver.find_element(By.XPATH,"//button[@id='mousehover']")
driver.execute_script("arguments[0].ScrollIntoView", mouse_hover)
act.click(mouse_hover).perform()
time.sleep(3)
