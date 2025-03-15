import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

# Set up Chrome driver
chrome_driver_path = "C:/chromedriver/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)  # Wait for the page to load

# Select dropdown element
dropdown = Select(driver.find_element(By.ID, "dropdown"))

# Test case 1: Select "Option 1" from dropdown
dropdown.select_by_visible_text("Option 1")
time.sleep(1)
print("Test Case 1: Selected Option 1 -", driver.find_element(By.ID, "dropdown").get_attribute("value"))

# Test case 2: Select "Option 2" from dropdown
dropdown.select_by_visible_text("Option 2")
time.sleep(1)
print("Test Case 2: Selected Option 2 -", driver.find_element(By.ID, "dropdown").get_attribute("value"))

# Test case 3: Check the default (no option selected)
# Just check if the value is empty (default state)
default_value = driver.find_element(By.ID, "dropdown").get_attribute("value")
time.sleep(1)
print("Test Case 3: No option selected (default) -", default_value)

# Close the browser
driver.quit()
