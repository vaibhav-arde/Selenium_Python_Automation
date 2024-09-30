import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Chrome driver service - selenium will check current version of browser and same version of chrome driver will be downloaded from net and install in local machine

# In many organisation download of chroem driver is not allowed hence test fails so we can use chromedriver

# service_obj = Service('/Users/vaibhavarde/Desktop/TestAutomation/Selenium_Python_Automation/01_Invoke_chrome_browser/chromedriver-mac-arm64/chromedriver') 
# driver = webdriver.Chrome(service = service_obj)

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()

driver.get("https://google.com")

print(driver.title)
print(driver.current_url)

time.sleep(2)