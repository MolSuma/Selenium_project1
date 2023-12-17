from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)

driver.maximize_window()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')


Home = driver.find_element(By.XPATH,"//button[contains(text(),'Home')]")
Home.click()
time.sleep(3)

driver.back()
time.sleep(3)

radio = driver.find_element(By.XPATH,"//body/div[1]/div[1]/fieldset[1]/label[2]/input[1]")
radio.click()
time.sleep(3)

country = driver.find_element(By.XPATH,"//input[@id='autocomplete']")
country.send_keys("India")
time.sleep(3)


#Drop Down

dropdown = driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
sel = Select(dropdown)
time.sleep(2)
sel.select_by_visible_text("Option3")
time.sleep(2)

# multiselect checkox

chk_list  = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
time.sleep(2)
for i in chk_list:
    time.sleep(3)
    i.click()


# get the window handle of the parent window

window_name = driver.current_window_handle

print(window_name)

time.sleep(3)

ele1 = driver.find_element(By.XPATH, "//button[@id='openwindow']")
ele1.click()

# get the window handles of both the windows

windows = driver.window_handles

for window in windows:
    print(window)

driver.switch_to.window(windows[1])

driver.maximize_window()

time.sleep(3)



# get the NEW tab

window_name = driver.current_window_handle

print(window_name)

time.sleep(3)

ele2 = driver.find_element(By.XPATH, "//a[@id='opentab']")
ele2.click()

# get the window handles of both the windows

windows = driver.window_handles

for window in windows:
    print(window)

driver.switch_to.window(windows[1])

driver.maximize_window()

time.sleep(3)



name = driver.find_element(By.XPATH,"//input[@name='enter-name']")
name.send_keys("vishal")
time.sleep(3)


#For Alert
simplealert = driver.find_element(By.XPATH,"//input[@id='alertbtn']")
simplealert.click()
time.sleep(3)

alt = driver.switch_to.alert
alt.accept()


#For Confirm
simplealert = driver.find_element(By.XPATH,"//input[@id='confirmbtn']")
simplealert.click()
time.sleep(3)


alt = driver.switch_to.alert
alt.accept()

time.sleep(5)



#Table
table = driver.find_elements(By.XPATH,"//body/div[3]/div[2]/fieldset[2]/div[1]")

rows = driver.find_elements(By.XPATH,"//table[@id = 'product']/tbody//tr[6]//td[2]")

print(rows)
time.sleep(5)

driver.close()