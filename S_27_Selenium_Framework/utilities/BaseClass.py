import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    # def __init__(self, driver) -> None:
    #     self.driver = driver
    
    def explicit_wait(self, time, locator, text):
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((locator, text)))
        
    def select_dropdown(self, locator, text):
        dropdown = Select(self.driver.find_element(*locator))
        dropdown.select_by_visible_text(text)