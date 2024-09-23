from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")
print("Title", driver.title)
print("Url", driver.current_url)


# import time
# from selenium import webdriver

# driver = webdriver.Chrome()
# # driver = webdriver.Firefox()
# # driver = webdriver.Edge()

# driver.get("https://google.com")

# print(driver.title)
# print(driver.current_url)

# time.sleep(2)