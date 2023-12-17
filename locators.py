#Navigating commands: To navigate front, back, refresh
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

option=webdriver.ChromeOptions()
driver=webdriver.Chrome(options=option)
driver.maximize_window()


#driver commands
driver.get('https://www.facebook.com/')

#locators by id:
email=driver.find_element(By.ID, "email") # finding element
# sending value
email.send_keys("sumamol27@gmail.com")


#locators by name
password=driver.find_element(By.NAME, "pass")
email.send_keys("Sumamano")

#class name
password1=driver.find_element(By.CLASS_NAME, "inputtext _55r1 _6luy _9npi")
password1.send_keys("123456")

#link text(https://automationexercise.com/contact_us)
text=driver.find_element(By.LINK_TEXT, "Log in")
text.click()

# partial link text
partial_text=driver.find_element(By.PARTIAL_LINK_TEXT, " Forgotten")
partial_text.click()

#csselector
signup=driver.find_element(By.CSS_SELECTOR, "body._39il._97vt._97vz._97v-._97v_._97w2._97w0._9ax-._9ax_._9ay1.UIPage_LoggedOut._-kb._605a.b_c3pyn-ahh.chrome.webkit.win.x1-5.Locale_en_GB.cores-gte4._19_u:nth-child(2) div._li:nth-child(2) div.uiContextualLayerParent:nth-child(1) div.fb_content.clearfix:nth-child(1) div._4-u5._30ny div._4-u2._1w1t._4-u8._52jv div.login_form_container form:nth-child(1) div:nth-child(4) div._xkv.fsm.fwn.fcg:nth-child(14) > a._97w5:nth-child(3)")
signup.click()

#tagname: applicable for hyperlinks only
tagname_passwrd=driver.find_element(By.TAG_NAME,"https://www.facebook.com/recover/initiate/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzAwNjM4MTY2LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&amp;ars=facebook_login")
tagname_passwrd.click()
#Relative path
login1=driver.find_element(By.XPATH, " //button[@id='u_0_9_Hd']")
login1.click()
password2=driver.find_element(By.NAME, "password")
password2.send_keys("Admin123")
