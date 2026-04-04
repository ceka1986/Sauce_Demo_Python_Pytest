# 🚀 SauceDemo Automation Framework

A professional end-to-end (E2E) automation framework built with **Python**, **Selenium**, and **Pytest**. This project demonstrates the implementation of the **Page Object Model (POM)** design pattern to test the [SauceDemo](https://www.saucedemo.com/) e-commerce platform.

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Automation:** Selenium WebDriver
- **Test Runner:** Pytest
- **Reporting:** Pytest-HTML
- **Design Pattern:** Page Object Model (POM)

## 📂 Project Structure

````text
SauceDemoPython/
├── pages/               # Page Object classes with locators and actions
├── tests/               # Test suites (Login, Inventory, Checkout)
├── utils/               # Centralized TestData (credentials, product info)
├── reports/             # Automatically generated HTML test reports
├── screenshots/         # Captured images for test verification and debugging
├── conftest.py          # Shared fixtures for WebDriver setup/teardown
├── pytest.ini           # Pytest configuration settings
└── requirements.txt     # List of project dependencies




# 🚀 SauceDemo Automation Framework

A professional end-to-end (E2E) automation framework built with **Python**, **Selenium**, and **Pytest**. This project demonstrates the implementation of the **Page Object Model (POM)** design pattern to test the [SauceDemo](https://www.saucedemo.com/) e-commerce platform.

## 🛠️ Tech Stack

* **Language:** Python 3.8+
* **Automation:** Selenium WebDriver
* **Test Runner:** Pytest
* **Reporting:** Pytest-HTML
* **Design Pattern:** Page Object Model (POM)

## 📂 Project Structure

```text
SauceDemoPython/
├── pages/               # Page Object classes with locators and actions
├── tests/               # Test suites (Login, Inventory, Checkout)
├── utils/               # Centralized TestData (credentials, product info)
├── reports/             # Automatically generated HTML test reports
├── screenshots/         # Captured images for test verification and debugging
├── conftest.py          # Shared fixtures for WebDriver setup/teardown
├── pytest.ini           # Pytest configuration settings
└── requirements.txt     # List of project dependencies

🧪 Test Coverage

Authentication (Login):

Happy Path: Verification of successful login with valid credentials.

Data-Driven Testing: 6 negative scenarios (invalid/locked-out users, empty fields) implemented using Pytest Parametrization.

Product Management (Inventory):

Sorting functionality (Name A-Z/Z-A, Price Low-High/High-Low).

Shopping cart interactions (Add/Remove items).

Checkout Workflow (E2E):

Full purchasing flow: from Login to Order Confirmation.

Modular step-by-step verification (Information entry, Overview, Final Success).


🚀 Getting Started

Install Dependencies:

Bash
pip install -r requirements.txt
Run All Tests:

Bash
pytest -v
Generate HTML Report:

Bash
pytest -v --html=reports/final_report.html --self-contained-html


✨ Key Framework Features

Scalability: Easy to add new pages and tests due to the POM architecture.

Maintainability: Centralized test data in utils/data.py ensures easy updates.

Reliability: Screenshots captured for visual proof of test execution.

Atomicity: Independent tests utilizing Pytest fixtures for clean setup/teardown.
````
