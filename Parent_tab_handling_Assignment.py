from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.maximize_window()
# get url
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
# parent window handle
window_name = driver.current_window_handle
print(window_name)
# switch to tab
new_tab = driver.find_element(By.XPATH, "//a[@id='opentab']").click()
time.sleep(3)
# get both window handles
windows = driver.window_handles
for i in windows:
    print(windows)

# switch to parent windows
driver.switch_to.window(windows[0])
# find element:
check_box = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for i in check_box:
    time.sleep(3)
    i.click()
