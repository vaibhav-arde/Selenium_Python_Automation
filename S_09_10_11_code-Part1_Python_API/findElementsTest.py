import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.find_element(By.XPATH, "//div/section/span[@data-cy='closeModal']").click()
# driver.find_element(By.ID, "fromCity").click()
driver.find_element(By.XPATH, "//input[@data-cy='fromCity']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='From']").send_keys("del")
time.sleep(2)
cities =driver.find_elements(By.CSS_SELECTOR, "p[class*='blackText']")
print (len(cities))
for city in cities:
    if city.text =="Del Rio, United States":
        city.click()
        break


driver.find_element(By.XPATH, "//p[text()='Delhi, India']").click()



