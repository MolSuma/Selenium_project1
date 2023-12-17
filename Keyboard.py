from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://www.facebook.com/login/')
driver.implicitly_wait(10)

email = driver.find_element(By.XPATH, "//input[@id='email']")

act = ActionChains(driver)

act.click(email).key_down(Keys.SHIFT).send_keys("hello").perform()


time.sleep(5)


driver.quit()