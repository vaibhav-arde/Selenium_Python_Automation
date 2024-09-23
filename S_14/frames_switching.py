import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/iframe')
time.sleep(2)
try:
    driver.find_element(By.CSS_SELECTOR, 'div.tox-icon').click()
except Exception as e:
    print(e)

driver.switch_to.frame('mce_0_ifr')
# driver.find_element(By.ID, 'tinymce').clear()
driver.find_element(By.ID, 'tinymce').send_keys('I am able to automate frames')
driver.switch_to.default_content()
time.sleep(3)
print(driver.find_element(By.CSS_SELECTOR, 'h3').text)