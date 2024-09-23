from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, 'a.ui-corner-all')
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# print("country", driver.find_element(By.ID, "autosuggest").text)
country = driver.find_element(By.ID, "autosuggest").get_attribute('value')
print("country", country)
assert(country == 'India')
