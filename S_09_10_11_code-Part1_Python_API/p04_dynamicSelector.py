import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
try:
    driver.find_element(By.XPATH, "//div/section/span[@data-cy='closeModal']").click()
except Exception as e:
    print("Error is : ",e)
# driver.find_element(By.ID, "fromCity").click()
driver.find_element(By.XPATH, "//input[@data-cy='fromCity']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='From']").send_keys("New Del")
time.sleep(2)
cities =driver.find_elements(By.CSS_SELECTOR, "span.makeFlex span")
# cities =driver.find_elements(By.CSS_SELECTOR, "p[class*='blackText']")
print(len(cities))
for city in cities:
    if city.text =="New Delhi":
        city.click()
        break

time.sleep(5)
driver.find_element(By.XPATH, "//input[@ID='fromCity']").click()
# driver.find_element(By.XPATH, "//input[contains(text(), 'Delhi')]").click()



