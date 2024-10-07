import pytest
from selenium import webdriver


# Adding a custom command-line option to select the browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome",  # Default browser is Chrome
        help="Browser option: chrome or firefox"
    )
    
@pytest.fixture(scope ="class")
def setup(request):
    """
    Sets up the initial configuration or environment for the application.
    
    This function is intended to initialize any necessary settings, 
    configurations, or resources required before the application starts 
    executing its main functionality. It should be called once at the 
    beginning of the application's lifecycle.
    """
    # Accessing the browser option from the command line
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield driver
    driver.quit()
    