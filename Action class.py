import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/')
time.sleep(3)
#dobule click using action class
# Action classs is used to handle mouse related actions
# import the action class

#dobule click
act=ActionChains(driver)
#addrem =driver.find_element(By.XPATH, "//a[contains(text(),'Add/Remove Elements')]")
#time.sleep(3)
#act.double_click(addrem).perform()
#time.sleep(3)
#driver.back()

#context click
contextmenu =driver.find_element(By.XPATH, "//a[contains(text(),'Context Menu')]")
time.sleep(3)
act.context_click(contextmenu).perform()
time.sleep(3)
#driver.back()



