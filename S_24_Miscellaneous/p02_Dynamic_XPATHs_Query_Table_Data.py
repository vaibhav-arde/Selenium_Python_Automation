from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
fruit_name = "Apple"

price_xpath = "//div[text()='Price']"
data_column_id = driver.find_element(By.XPATH, price_xpath).get_attribute("data-column-id")
print("data_column_id", data_column_id)

price_value_xpath = "//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+data_column_id+"-undefined']"
# fruit_price = driver.find_element(By.XPATH, "//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-4-undefined']").text
fruit_price = driver.find_element(By.XPATH, price_value_xpath).text
print("fruit_price", fruit_price)

