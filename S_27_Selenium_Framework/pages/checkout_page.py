from selenium.webdriver.common.by import By


class CheckoutPage:
    checkout_btn = (By.XPATH,"//button[@class='btn btn-success']")
    search_country_ele = (By.ID,"country")
    select_country_ele = (By.LINK_TEXT,"India")
    select_checkbox_ele = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    submit_btn = (By.CSS_SELECTOR,"[type='submit']")
    success_alert = (By.CLASS_NAME,"alert-success")
    
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def checkout(self):
        return self.driver.find_element(*CheckoutPage.checkout_btn)
    
    def search_country(self):
        return self.driver.find_element(*CheckoutPage.search_country_ele)
    
    def select_country(self):
        return self.driver.find_element(*CheckoutPage.select_country_ele)
    
    def select_checkbox(self):
        return self.driver.find_element(*CheckoutPage.select_checkbox_ele)
    
    def submit(self):
        return self.driver.find_element(*CheckoutPage.submit_btn)
    
    def success_alert_text(self):
        return self.driver.find_element(*CheckoutPage.success_alert).text