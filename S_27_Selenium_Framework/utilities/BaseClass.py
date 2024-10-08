import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import inspect
import logging
import os

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    script_path = os.path.abspath(__file__)
    folder_name = os.path.dirname(os.path.dirname(script_path))

    # Set the download path to a subfolder within the current script's folder
    log_path = os.path.join(folder_name, "logs/logfile.log")
    
    def explicit_wait(self, time, locator, text):
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((locator, text)))
        
    def select_dropdown(self, locator, text):
        dropdown = Select(self.driver.find_element(*locator))
        dropdown.select_by_visible_text(text)
        
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(BaseClass.log_path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger