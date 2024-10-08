# from selenium import webdriver
import pytest
#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
from pages.home_page import HomePage
# from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage

# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    
    def test_e2e(self):
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(4)
        # self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        #  //a[contains(@href,'shop')]    a[href*='shop']
        
        homepage = HomePage(self.driver)
        productsPage = homepage.shopButton()
        # self.driver.find_element(By.CSS_SELECTOR," a[href*='shop']").click()
        
        # productsPage= ProductsPage(self.driver)
        products = productsPage.product_list()
        # products = self.driver.find_elements(By.XPATH,"//div[@class='card h-100']")
        
        productsPage.select_product("Blackberry", products)
        # for product in products :
        #     productName = product.find_element(By.XPATH, "div/h4/a").text
        #     if productName == "Blackberry":
        #         product.find_element(By.XPATH, "div/button").click()

        checkoutPage = productsPage.checkout()
        # self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
        
        # checkoutPage = CheckoutPage(self.driver)
        checkoutPage.checkout().click()
        # self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        
        checkoutPage.search_country().send_keys("ind")
        # self.driver.find_element(By.ID,"country").send_keys("ind")
        
        self.explicit_wait(10, By.LINK_TEXT, "India")
        # wait = WebDriverWait(self.driver,10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        
        checkoutPage.select_country().click()
        # self.driver.find_element(By.LINK_TEXT,"India").click()
        
        checkoutPage.select_checkbox().click()
        # self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        
        checkoutPage.submit().click()
        # self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        
        successText = checkoutPage.success_alert_text()
        # successText = self.driver.find_element(By.CLASS_NAME,"alert-success").text
        assert "Success! Thank you!" in successText
        self.driver.close()
