import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')

driver.find_element(By.LINK_TEXT, 'Click Here').click()

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

print(driver.find_element(By.TAG_NAME, 'H3').text)
assert 'New Window' == driver.find_element(By.TAG_NAME, 'H3').text
time.sleep(3)
driver.close()

driver.switch_to.window(windowsOpened[0])
print(driver.find_element(By.TAG_NAME, 'H3').text)

assert 'Opening a new window' == driver.find_element(By.TAG_NAME, 'H3').text
time.sleep(3)
