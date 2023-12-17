iframe = driver.find_element(By.XPATH, "//iframe[@id='courses-iframe']")
driver.switch_to.frame(iframe)
time.sleep(2)

element_inside_iframe = driver.find_element(By.XPATH, "//a[contains(text(),'Python SDET- Automation Testing Package')]")
print("Text inside the iframe:", element_inside_iframe.text)
time.sleep(2)

element_to_click = driver.find_element(By.XPATH, "//a[contains(text(),'Python SDET- Automation Testing Package')]")
element_to_click.click()
time.sleep(2)

# Switch back to the default content (outside the iframe)
driver.switch_to.default_content()
time.sleep(2)