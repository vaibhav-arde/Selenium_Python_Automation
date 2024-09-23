from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://login.salesforce.com/")
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("Vaibhav")
driver.find_element(By.CSS_SELECTOR,".password").send_keys("Arde")
driver.find_element(By.CSS_SELECTOR,".password").clear()
driver.find_element(By.LINK_TEXT, "Forgot Your Password?").click()
#//tagname[text()=’xxx’]
# driver.find_element_by_xpath("//a[text()='Cancel']").click()
driver.find_element(By.XPATH, "//input[@name='cancel']").click()
print(driver.find_element(By.XPATH, "//form[@name='login']/div[1]/label").text)
print(driver.find_element(By.CSS_SELECTOR,"form[name='login'] label:nth-child(3)").text)





