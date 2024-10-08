import pytest
from selenium import webdriver
driver = None

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
    global driver
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
    
    
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)