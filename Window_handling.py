import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('http://www.dummypoint.com/Windows.html')

# get the window handle of the parent window

window_name = driver.current_window_handle

print(window_name)

time.sleep(3)

ele = driver.find_element(By.XPATH, "//input[@value='Open a Popup Window']")
ele.click()

# get the window handles of both the windows

windows = driver.window_handles
# Move to both windows
# parent window, then child window
for window in windows:
    print(window)
# move to child window
driver.switch_to.window(windows[1])

driver.maximize_window()

time.sleep(3)
#switch to frame
fr = driver.find_element(By.ID, "f2")

driver.switch_to.frame(fr)
# Click on element in child window
prmt = driver.find_element(By.XPATH, "//button[@name = 'promtalert'][1]")

prmt.click()

time.sleep(3)