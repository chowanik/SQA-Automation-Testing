from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Set up ChromeDriver path
chrome_driver_path = "C:/chromedriver/chromedriver.exe"  # Update this path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Define test cases (username, password, expected result)
test_cases = [
    ("tomsmith", "SuperSecretPassword!", "Success"),  # ✅ Valid login
    ("tomsmith", "WrongPassword", "Fail"),           # ❌ Wrong password
    ("invalidUser", "SuperSecretPassword!", "Fail"), # ❌ Invalid username
    ("", "", "Fail")                                  # ❌ Empty fields
]

for username, password, expected in test_cases:
    driver.get("https://the-internet.herokuapp.com/login")  # Open login page
    time.sleep(2)  # Small delay for page load

    # Enter username & password
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # Click Login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    # Capture message
    try:
        message = driver.find_element(By.CLASS_NAME, "flash").text
    except:
        message = ""

    # Check test result
    if expected == "Success" and "You logged into a secure area!" in message:
        print(f"✅ Test Passed for {username}")
    elif expected == "Fail" and "Your username is invalid!" in message or "Your password is invalid!" in message:
        print(f"✅ Test Passed for {username} (expected fail)")
    else:
        print(f"❌ Test Failed for {username}")

# Close the browser
driver.quit()


