from selenium.webdriver.common.by import By
from pages.checkout_page import CheckoutPage

class ProductsPage:
    products = (By.XPATH,"//div[@class='card h-100']")
    product_names = (By.XPATH, "div/h4/a")
    add_btn = (By.XPATH, "div/button")
    checkout_btn = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    
    
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def product_list(self):
        return self.driver.find_elements(*ProductsPage.products)
    
    def select_product(self, product_name, products):
        for product in products :
            productName = product.find_element(*ProductsPage.product_names).text
            if productName == product_name:
                product.find_element(*ProductsPage.add_btn).click()
                
    def checkout(self):
        self.driver.find_element(*ProductsPage.checkout_btn).click()
        return CheckoutPage(self.driver)
    