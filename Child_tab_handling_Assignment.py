from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
#get window handle of parent window
window_name=driver.current_window_handle
print(window_name)
time.sleep(3)
#switch to tab
new_tab=driver.find_element(By.XPATH,"//a[@id='opentab']").click()
time.sleep(3)
#get window handles of both
windows=driver.window_handles
# Move to both windows
# parent window, then child window
for window in windows:
    print(window)
# move to child window
driver.switch_to.window(windows[1])
driver.maximize_window()
time.sleep(3)
#fetch text from new tab:
fetch_text1=driver.find_element(By.XPATH,"/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/h2[1]")
time.sleep(3)
text_value=fetch_text1.text
print(text_value)
time.sleep(3)
#get current url
url1=driver.current_url
print(url1)
#move back
driver.back()
time.sleep(3)
#get current url
url2=driver.current_url
print(url2)