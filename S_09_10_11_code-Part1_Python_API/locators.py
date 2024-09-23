from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Chrome()
# driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("VaibhaV")
# driver.find_element(By.NAME, "name").send_keys("VaibhaV")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("VaibhaV")
# driver.find_element_by_css_selector("input[name='name']").send_keys("VaibhaV")
# driver.find_element_by_name("email").send_keys("Shetty")
driver.find_element(By.NAME, "email").send_keys("test@g.com")
# driver.find_element_by_id("exampleCheck1").click()
driver.find_element(By.ID, "exampleCheck1").click()
# #select class provide the methods to handle the options in dropdown
# dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(2)
dropdown.select_by_index(0)

# driver.find_element_by_xpath("//input[@type='submit']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
# message = driver.find_element_by_class_name("alert-success").text
message = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "success" in message
time.sleep(5)