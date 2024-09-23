#Implicit wait  -
#Explicit Wait
import time

from selenium import webdriver
#pause the test for few seconds using Time class
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")
driver.implicitly_wait(5)
list = []
list2 = []
# wait until 5 seconds if object is not displayed
#Global wait
#1.5 second to reach next page- execution will resume in 1.5 seconds
#if object do not show up at all, then max time your test waits for 5 seconds
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)
count =len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")

for button in buttons:
    list.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    button.click()

print(list)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Implicit wait
# driver.implicitly_wait(5)

# Explicit wait
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
veggies =driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for l in veggies:
    list2.append(l.text)

print(list2)
assert list == list2

amount1= driver.find_element(By.CSS_SELECTOR, ".discountAmt").text

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

amount2= driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
print("amount2", amount2)
assert int(amount1) > float(amount2)

veggiesAmount = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0

for v in veggiesAmount:
    print("veggie price : ", int(v.text))
    sum = sum + int(v.text)

print(sum)

# assert sum == int(amount2)

time.sleep(5)




