from selenium import webdriver

chrome_options =  webdriver.ChromeOptions()
chrome_options.add_argument("headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print("Total height of page : ", driver.execute_script("return document.body.scrollHeight"))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0, 0)")

# Get the height of the current window (viewport)
viewport_height = driver.execute_script("return window.innerHeight;")
driver.execute_script(f"window.scrollBy(0, {viewport_height});")
driver.execute_script(f"window.scrollBy(0, {viewport_height});")
driver.execute_script(f"window.scrollBy(0, {viewport_height});")
driver.execute_script("window.scrollTo(0, 0)")
print("Headless mode done!!")