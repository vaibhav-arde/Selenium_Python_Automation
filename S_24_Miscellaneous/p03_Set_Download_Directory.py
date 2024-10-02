import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

# # Get the current working directory (your project folder)
# project_dir = os.getcwd()
# print("project_dir", project_dir)

# # Set the desired download folder within the project directory
# download_dir = os.path.join(project_dir, "downloads")

# import os

# Get the absolute path of the current script
script_path = os.path.abspath(__file__)

# Get the directory name from the path
project_dir = os.path.dirname(script_path)
print("project_dir", project_dir)
download_dir = os.path.join(project_dir, "downloads")

print("download_dir", download_dir)

# Create the 'downloads' directory if it doesn't exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Configure Chrome options to set the download directory
chrome_options = webdriver.ChromeOptions()

# Set Chrome preferences for file download behavior
prefs = {
    "download.default_directory": download_dir,  # Set the download directory
    # "download.prompt_for_download": False,       # Disable download prompts
    # "directory_upgrade": True,                   # Auto-upgrade the download directory
    # "safebrowsing.enabled": True                 # Enable safe browsing
}

chrome_options.add_experimental_option("prefs", prefs)

# Initialize the WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

# Navigate to the page with the downloadable file
# driver.get("https://example.com/path/to/downloadable/file")
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
time.sleep(5)
# Example: Click to trigger file download
driver.find_element(By.ID, "downloadButton").click()
# download_link = driver.find_element_by_link_text("Download")
# download_link.click()

# Add a sleep or wait mechanism to ensure the download completes
# time.sleep(5) or WebDriverWait can be used as required

# Close the WebDriver
driver.quit()

print(f"Files will be downloaded to: {download_dir}")
