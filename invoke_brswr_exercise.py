from selenium import webdriver

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/python/index.htm")
title1=driver.title
print(title1)
pagesource1=driver.page_source
print(pagesource1)
current_url1=driver.current_url
print(current_url1)
driver.close()

