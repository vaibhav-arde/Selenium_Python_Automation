from selenium.webdriver.common.by import By
from pages.products_page import ProductsPage


class HomePage:
    shop = (By.CSS_SELECTOR," a[href*='shop']")
    
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def shopButton(self):
        self.driver.find_element(*HomePage.shop).click()
        return ProductsPage(self.driver)