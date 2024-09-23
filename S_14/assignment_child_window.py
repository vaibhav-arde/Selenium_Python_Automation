from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

parentWindow = driver.current_window_handle
driver.find_element(By.CSS_SELECTOR, 'body a.blinkingText').click()
windowsOpened = driver.window_handles
print('windowsOpened', windowsOpened)
driver.switch_to.window(windowsOpened[1])
childWindow = driver.current_window_handle
# print('parentWindow', parentWindow)
# print('childWindow', childWindow )
email = driver.find_element(By.CSS_SELECTOR, 'p.red strong').text
print('email', email)
driver.close()
driver.switch_to.window(parentWindow)
driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID, 'password').send_keys('password')
driver.find_element(By.ID, 'signInBtn').click()

print(driver.find_element(By.CSS_SELECTOR, 'div.alert-danger strong').text)
time.sleep(3)