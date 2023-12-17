from selenium import webdriver

#Chrome options are used to load the capabitlitesof the chrome browser
#putting in the option variable

option=webdriver.ChromeOptions()
# all options of chrome  are assigned to webdriver
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get('https://chromewebstore.google.com/')