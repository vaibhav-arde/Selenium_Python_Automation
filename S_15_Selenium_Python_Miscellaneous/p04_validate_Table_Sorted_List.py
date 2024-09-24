from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browserVeggie = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggieEle = driver.find_elements(By.XPATH, '//tr/td[1]')
for ele in veggieEle:
    browserVeggie.append(ele.text)
    
originalVeggie = browserVeggie.copy()

browserVeggie.sort()

print("originalVeggie", originalVeggie)
print("browserVeggie", browserVeggie)

assert browserVeggie == originalVeggie