# **🚀 Mastering Selenium, Pytest, Logging, and HTML Reporting**

Welcome! This repository contains detailed notes and practical examples on key topics that every test automation engineer should know. Whether you're a beginner or looking to brush up on your skills, these notes are designed to help you practice and learn.

---

## 📘 Topics Covered

1. **[Selenium](#selenium)**
2. **[Pytest](#pytest)**
3. **[Logging in Python Tests](#logging-in-python-tests)**
4. **[HTML Reporting with Pytest](#html-reporting-with-pytest)**

---

### 🔍 **Selenium**

Learn how to automate browser interactions with Selenium WebDriver. We'll go over everything from setting up WebDriver, performing basic actions, and executing JavaScript within the browser.

#### 📂 **File Path**:

- `./Notes/Automation_Selenium_Notes.pdf`

#### Topics Covered:

- **Setting up Selenium WebDriver**
- **Navigating to Web Pages**
- **Interacting with Web Elements** (clicking buttons, entering text)
- **Scrolling through Web Pages**
- **Handling JavaScript Pop-ups**
- **Running Tests in Headless Mode**

#### 🛠️ **Example**:

```python
from selenium import webdriver

# Setup Chrome WebDriver with headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Open a practice page and interact with elements
driver.get("https://example.com")
button = driver.find_element_by_id("submit-button")
button.click()

driver.quit()
```

---

### ⚙️ **Pytest**

Pytest is a powerful testing framework for Python. Learn how to write and organize tests, use fixtures, and run specific tests from the command line.

#### 📂 **File Path**:

- `./Notes/Automation_PyTest_Notes.pdf`

#### Topics Covered:

- **Writing Your First Test**
- **Using `assert` for Validations**
- **Organizing Tests in Files and Directories**
- **Test Naming Conventions**
- **Running Tests from Command Line**
- **Using Markers (`@pytest.mark`)**
- **Fixtures for Test Setup and Teardown**

#### 🛠️ **Example**:

```python
import pytest

@pytest.fixture
def setup():
    # Code for setting up test environment
    return "setup complete"

def test_example(setup):
    assert setup == "setup complete"
```

---

### 🧾 **Logging in Python Tests**

Logging is essential for understanding test execution flow and debugging failures. Learn how to add logging into your test suites and capture important information.

#### 📂 **File Path**:

- `./Notes/Automation_Logging_and_HTML_Reports_Notes.pdf`

#### Topics Covered:

- **Introduction to Logging**
- **Configuring Logging Levels** (`INFO`, `DEBUG`, `ERROR`)
- **Capturing Logs During Test Runs**
- **Using `inspect.stack()` for Dynamic Logger Names**

#### 🛠️ **Example**:

```python
import logging
import inspect

def log_message():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.info("This is an info log.")

def test_logging_example():
    log_message()
```

---

### 📊 **HTML Reporting with Pytest**

Generate easy-to-read HTML reports for your test runs with `pytest-html`. This allows you to share test results and logs with your team in a visually appealing format.

#### 📂 **File Path**:

- `./Notes/Automation_Logging_and_HTML_Reports_Notes.pdf`

#### Topics Covered:

- **Generating Basic HTML Reports**
- **Customizing HTML Reports with Metadata**
- **Integrating Logs into HTML Reports**

#### 🛠️ **Example**:

```bash
pytest --html=report.html --self-contained-html
```

---

## 🎯 **How to Use These Notes**

Each topic is designed to be self-contained and includes both theoretical notes and code examples. You can:

- **Browse the Notes**: Read the detailed explanations in each section.
- **Run Code Examples**: Try out the provided examples in your IDE or terminal.
- **Practice on Pages**: Use the suggested practice websites to test your automation scripts.

## 📚 **Resources**

Below are the file paths for the notes on each topic:

- **Selenium Notes**:
  - `./Notes/Automation_Selenium_Notes.pdf`
- **Pytest Notes**:
  - `./Notes/Automation_PyTest_Notes.pdf`
- **Logging, HTML Reporting with Pytest**:
  - `./Notes/Automation_Logging_and_HTML_Reports_Notes.pdf`

## 📝 **Practice**:

**Note that practical example with code are available in folder starting with "S_", refer those with notes and execute simultanously with notes for better understanding**

## 📝 **Practice pages**:

- https://rahulshettyacademy.com/practice-project
- https://rahulshettyacademy.com/angularpractice/
- https://login.salesforce.com/
- https://rahulshettyacademy.com/seleniumPractise/#/
- https://rahulshettyacademy.com/AutomationPractice/
- https://rahulshettyacademy.com/dropdownsPractise/
- https://drive.google.com/file/d/1Pj-9Zg06UiQIpqUi88TrrtMtFe9VPr1S/view
- https://drive.google.com/file/d/18FC3jDnsOol9zn3_KGSrjg35a4unpiSG/view
- https://drive.google.com/file/d/1A3Q_HX8A_GtamXs5kpdZ_7jM8W-OajKS/view

---

Feel free to contribute to the repository by adding more examples, improving the notes, or creating more practice challenges. Happy learning! 🎉

---
