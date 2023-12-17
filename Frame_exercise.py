from selenium import webdriver
import time
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://the-internet.herokuapp.com/iframe')
time.sleep(1)
fr=driver.find_element(By.XPATH, " //iframe[@id='mce_0_ifr']")
driver._switch_to.frame(fr)

enter_text= driver.find_element(By.ID,"tinymce")
enter_text.clear()
time.sleep(3)
enter_text.send_keys("Suma")