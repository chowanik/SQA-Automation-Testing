from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your chromedriver
chrome_driver_path = "C:/chromedriver/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the page with checkboxes
driver.get("https://the-internet.herokuapp.com/checkboxes")


# Dynamic Test Function to handle all scenarios
def test_checkbox_scenarios():
    try:
        # Locate the checkboxes by their xpath
        checkbox_1 = driver.find_element(By.XPATH, "//input[1]")  # First checkbox
        checkbox_2 = driver.find_element(By.XPATH, "//input[2]")  # Second checkbox

        # Scenario 1: Check both checkboxes
        if not checkbox_1.is_selected():
            checkbox_1.click()
        if not checkbox_2.is_selected():
            checkbox_2.click()
        print("Scenario 1: Both checkboxes checked.")

        time.sleep(2)  # Wait to observe the result

        # Scenario 2: Uncheck both checkboxes
        if checkbox_1.is_selected():
            checkbox_1.click()
        if checkbox_2.is_selected():
            checkbox_2.click()
        print("Scenario 2: Both checkboxes unchecked.")

        time.sleep(2)  # Wait to observe the result

        # Scenario 3: Check only the first checkbox
        if not checkbox_1.is_selected():
            checkbox_1.click()
        if checkbox_2.is_selected():
            checkbox_2.click()
        print("Scenario 3: Only the first checkbox checked.")

        time.sleep(2)  # Wait to observe the result

        # Scenario 4: Keep the second checkbox checked, uncheck the first one
        if checkbox_1.is_selected():
            checkbox_1.click()
        # Don't touch the second checkbox, leave it checked
        print("Scenario 4: First checkbox unchecked, second checkbox remains checked.")

        time.sleep(2)  # Wait to observe the result

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the test
test_checkbox_scenarios()

# Close the browser after test execution
driver.quit()
