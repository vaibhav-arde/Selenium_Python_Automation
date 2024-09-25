import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
# time.sleep(5)
action = ActionChains(driver)
action.context_click(driver.find_element(By.ID, "opentab")).perform()
action.move_to_element(driver.find_element(By.ID, "name")).click().perform()
action.click_and_hold(driver.find_element(By.ID, "openwindow")).perform()
time.sleep(3)
action.double_click(driver.find_element(By.ID, "hide-textbox")).perform()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Top")).click().perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(3)