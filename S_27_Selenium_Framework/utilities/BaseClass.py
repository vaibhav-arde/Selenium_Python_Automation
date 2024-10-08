import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import inspect
import logging

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
        
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('/Users/vaibhavarde/Desktop/TestAutomation/Selenium_Python_Automation/S_27_Selenium_Framework/logs/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger