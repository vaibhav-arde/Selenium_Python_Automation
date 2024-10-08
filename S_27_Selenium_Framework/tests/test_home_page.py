from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from utilities.BaseClass import BaseClass
from pages.home_page import HomePage

class TestHomePage(BaseClass):
        
    def test_e2e(self):
        # driver = webdriver.Chrome()
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        homePage = HomePage(self.driver)
        homePage.name().send_keys("VaibhaV")
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("VaibhaV")

        homePage.email().send_keys("test@g.com")
        # driver.find_element(By.NAME, "email").send_keys("test@g.com")
        
        homePage.checkbox().click()
        # driver.find_element(By.ID, "exampleCheck1").click()
        
        self.select_dropdown((By.ID, "exampleFormControlSelect1"), "Female")
        # dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # dropdown.select_by_visible_text("Female")
        # time.sleep(2)
        # dropdown.select_by_index(0)
        
        homePage.submit().click()
        # driver.find_element(By.XPATH, "//input[@type='submit']").click()

        message = homePage.success_alert_text()
        # message = driver.find_element(By.CLASS_NAME,"alert-success").text
        assert "success" in message
        time.sleep(5)