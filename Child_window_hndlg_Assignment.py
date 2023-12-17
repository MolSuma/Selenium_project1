from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url:
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
#get the parent window handle
window_name=driver.current_window_handle
print(window_name)
# open the child window:
child_window=driver.find_element(By.XPATH,"//button[@id='openwindow']").click()
# get the window handles
windows=driver.window_handles
for i in windows:
    print(i)
driver.switch_to.window(windows[1])
time.sleep(3)
driver.maximize_window()

platform_tab=driver.find_element(By.XPATH,"//a[contains(text(),'Access all our Courses')]")
time.sleep(3)
#scroll to view
driver.execute_script("arguments[0].scrollIntoView()", platform_tab)
time.sleep(3)
platform_tab.click()
time.sleep(5)




