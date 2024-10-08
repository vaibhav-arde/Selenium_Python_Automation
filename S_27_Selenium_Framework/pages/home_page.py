from selenium.webdriver.common.by import By
from pages.products_page import ProductsPage


class HomePage:
    shop = (By.CSS_SELECTOR," a[href*='shop']")
    name_input = (By.CSS_SELECTOR, "input[name='name']")
    email_input = (By.NAME, "email")
    checkbox_ele = (By.ID, "exampleCheck1")
    dropdown_ele = (By.ID, "exampleFormControlSelect1")
    submit_btn = (By.XPATH, "//input[@type='submit']")
    success_alert = (By.CLASS_NAME,"alert-success")
    
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def shopButton(self):
        self.driver.find_element(*HomePage.shop).click()
        return ProductsPage(self.driver)
    
    def name(self):
        return self.driver.find_element(*HomePage.name_input)
    
    def email(self):
        return self.driver.find_element(*HomePage.email_input)
    
    def checkbox(self):
        return self.driver.find_element(*HomePage.checkbox_ele)
    
    def submit(self):
        return self.driver.find_element(*HomePage.submit_btn)
    
    def success_alert_text(self):
        return self.driver.find_element(*HomePage.success_alert).text
    
    