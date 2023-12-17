from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers')
time.sleep(3)
admin_button=driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]/span[1]").click()
time.sleep(3)