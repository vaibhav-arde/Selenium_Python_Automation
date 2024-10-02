import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


# Get the folder name of the current script
script_path = os.path.abspath(__file__)
folder_name = os.path.dirname(script_path)

# Set the download path to a subfolder within the current script's folder
download_path = os.path.join(folder_name, "downloads")

# Set up Chrome options
options = webdriver.ChromeOptions()
prefs = {'download.default_directory': download_path}
options.add_experimental_option('prefs', prefs)

# Create a WebDriver instance
driver = webdriver.Chrome(options=options)

# Navigate to the webpage with the file to download
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
time.sleep(3)
# Find the download link and click it
# Example: Click to trigger file download
driver.find_element(By.ID, "downloadButton").click()

# Wait for the download to complete (you might need to implement a mechanism to check if the download is finished)

# Close the browser
driver.quit()