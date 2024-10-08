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
    
    def test_e2e_logging(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        productsPage = homepage.shopButton()
        log.info("Navigating to products page")
        products = productsPage.product_list()
        productsPage.select_product("Blackberry", products)
        log.info("Added blackberry to buy")
        checkoutPage = productsPage.checkout()
        checkoutPage.checkout().click()
        checkoutPage.search_country().send_keys("ind")
        self.explicit_wait(10, By.LINK_TEXT, "India")
        checkoutPage.select_country().click()
        log.info("Country selected as India")
        checkoutPage.select_checkbox().click()
        checkoutPage.submit().click()
        log.info("Submitted at last")
        successText = checkoutPage.success_alert_text()
        assert "Success! Thank you!" in successText
        log.info("Got success message: " + successText)
        self.driver.close()
