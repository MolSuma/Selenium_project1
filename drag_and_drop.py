import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/drag_and_drop')
time.sleep(3)
src=driver.find_element(By.XPATH, "//div[@id='column-a']")
dest=driver.find_element(By.XPATH,"//div[@id='column-b']")
#action class is used to do mouse related operations
act=ActionChains(driver)
#drag & drop from source to destination
time.sleep(3)
act.drag_and_drop(src,dest).perform()
time.sleep(3)
driver.close()