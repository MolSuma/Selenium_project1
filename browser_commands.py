from selenium import webdriver

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()


#deiver commands
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#driver.title() return type is srting
title1= driver.title
print(title1)

# driver.page_source->it will give all html program(whole source code of the displayed page) in that page, output is string
# to check the text is present or not developr will use pagesouce command
pagesource1=driver.page_source
print(pagesource1)

# To get current url in which page we are working
currenturl1=driver.current_url
print(currenturl1)
# It will close current browser we are working,Else laptop will be slow or CPU will get overloaded
#quit-> Close all browsers
driver.close()