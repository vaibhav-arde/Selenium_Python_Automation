import pytest
from selenium import webdriver

@pytest.fixture(scope ="class")
def setup(request):
    """
    Sets up the initial configuration or environment for the application.
    
    This function is intended to initialize any necessary settings, 
    configurations, or resources required before the application starts 
    executing its main functionality. It should be called once at the 
    beginning of the application's lifecycle.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield driver
    driver.quit()
    