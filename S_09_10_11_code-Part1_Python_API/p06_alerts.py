from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "VaibhaV"

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
alertText = alert.text
print("alertText : ", alertText)
assert name in alertText
alert.accept()
# alert.dismiss()
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Text2")
time.sleep(5)