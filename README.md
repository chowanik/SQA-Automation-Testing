#SQA Testing Project
Project Overview
This project showcases Software Quality Assurance (SQA) Testing performed on the The Internet Herokuapp website. It includes both manual testing and automation testing for key functionalities: Login Authentication, Checkboxes, and Dropdown.

The goal of this project is to ensure the website’s functionalities are working as expected and to demonstrate testing skills for my SQA job applications.

Testing Process
The testing process is divided into two main parts:

1. Manual Testing
Manual testing involves executing test cases without automation tools. The main focus was to verify the functionality of the login, checkboxes, and dropdown features on the website.

Manual Test Scenarios:
Login Authentication Test:

Verify login with valid credentials.
Verify login with invalid credentials.
Check behavior when password is pasted into the input field.
Checkboxes Test:

Check both checkboxes.
Uncheck both checkboxes.
Check the first checkbox only.
Check the first checkbox while the second remains checked.
Dropdown Test:

Select "Option 1".
Select "Option 2".
Do not select any option (default state).
All test cases were documented in TestCases_Manual.xlsx, which contains detailed steps, expected results, and pass/fail status.

2. Automation Testing
Automation testing was implemented using Selenium in Python to execute the same test cases as manual testing, reducing execution time and increasing reliability.

Automation Test Scenarios:
Login Authentication Test:

Automated tests for valid and invalid login scenarios, including password paste behavior.
Checkboxes Test:

Automation for checking/unchecking boxes as per manual test cases.
Dropdown Test:

Automation for selecting dropdown options and verifying default behavior.
Tools Used:
Python 3.7
Selenium WebDriver for automation.
ChromeDriver to interface with Google Chrome.
Pytest (planned, but not implemented due to installation issues).
PyCharm for Python development.
