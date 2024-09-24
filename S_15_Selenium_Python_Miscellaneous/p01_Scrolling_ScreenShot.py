from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print("Total height of page : ", driver.execute_script("return document.body.scrollHeight"))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0)")
time.sleep(2)
# Get the height of the current window (viewport)
viewport_height = driver.execute_script("return window.innerHeight;")
driver.execute_script(f"window.scrollBy(0, {viewport_height});")
time.sleep(2)
driver.execute_script(f"window.scrollBy(0, {viewport_height});")
time.sleep(2)
driver.execute_script(f"window.scrollBy(0, {viewport_height});")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0)")
time.sleep(2)

driver.save_screenshot('S_15_Selenium_Python_Miscellaneous/screenshot_save.png')
driver.get_screenshot_as_file('S_15_Selenium_Python_Miscellaneous/screenshot_get.png')
driver.find_element(By.CSS_SELECTOR, 'body h1').screenshot("S_15_Selenium_Python_Miscellaneous/screenshot_element.png")