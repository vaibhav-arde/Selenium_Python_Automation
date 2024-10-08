import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    # def __init__(self, driver) -> None:
    #     self.driver = driver
    
    def explicit_wait(self, time, locator, text):
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((locator, text)))