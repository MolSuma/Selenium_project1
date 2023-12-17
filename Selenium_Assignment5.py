from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
#get url
driver.get('https://www.saucedemo.com/')
time.sleep(3)
Current_url1=driver.current_url
print(Current_url1)
#Enter username
username1=driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")

time.sleep(3)
# Enter password
username1=driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
time.sleep(3)
#Click login button
login_button=driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(3)
print("---------------")
Current_url2=driver.current_url
print(Current_url2)
#click on add to cart:
product1=driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()
time.sleep(1)
product2=driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
time.sleep(1)
product3=driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']").click()
time.sleep(1)
#click on add to cart button:
add_to_cart_button=driver.find_element(By.XPATH,"//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='header_container']/div[1]/div[3]/a[1]").click()
time.sleep(3)
#click on checkout button:
check_out_button=driver.find_element(By.XPATH,"//button[@id='checkout']").click()
time.sleep(3)
driver.switch_to.default_content()
#click on twitter link
twitter_link=driver.find_element(By.XPATH,"//a[contains(text(),'Twitter')]").click()
time.sleep(7)
driver.switch_to.default_content()
#click on facebook link
facebook_link=driver.find_element(By.XPATH,"//a[contains(text(),'Facebook')]").click()
time.sleep(7)
driver.switch_to.default_content()
#click on LinkedIn link
inkedIn_link=driver.find_element(By.XPATH,"//a[contains(text(),'LinkedIn')]").click()
time.sleep(7)
driver.switch_to.default_content()



