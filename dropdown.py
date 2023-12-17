from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://the-internet.herokuapp.com/dropdown')
time.sleep(3)

dropdown = driver.find_element(By.XPATH,"//select[@id='dropdown']")
time.sleep(3)

sel=Select(dropdown)
time.sleep(3)
#slect by value
sel.select_by_value("2")
time.sleep(3)
#selct by index
sel.select_by_index(1)
time.sleep(3)
#select by text
sel.select_by_visible_text("Option 2")
time.sleep(3)