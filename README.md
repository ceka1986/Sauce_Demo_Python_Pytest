# 🧪 SauceDemo Test Automation Framework

A scalable and maintainable UI test automation framework built for the SauceDemo application using **Python, Selenium, and Pytest**.

This project demonstrates real-world QA automation practices including **Page Object Model (POM)**, **component-based design**, **Dockerized execution**, and **CI/CD integration**.

---

## 🚀 Overview

The framework automates key user flows of an e-commerce application:

- Login functionality
- Product browsing and selection
- Cart operations
- Checkout process
- Order confirmation

The architecture is designed for **readability, reusability, and scalability**, making it suitable for real-world automation projects.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Automation Tool:** Selenium WebDriver
- **Testing Framework:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **Architecture:** Component-based structure
- **Containerization:** Docker & Docker Compose
- **CI/CD:** GitHub Actions

---

## 📂 Project Structure

```id="5k8r2c"
SauceDemoPython/
│
├── pages/                         # Page Object classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_step_one_page.py
│   ├── checkout_step_two_page.py
│   ├── checkout_complete_page.py
│   |── product_details_page.py
|   └──components/                    # Reusable UI components
│       └──sidebar.py
|
│
├── tests/                         # Test cases
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_checkout.py
│
├── utils/                         # Test data and helpers
│   └── data.py
│
├── reports/                       # HTML reports
│   └── report.html
│
├── screenshots/                   # Failure screenshots
│
├── .github/workflows/             # CI pipeline
│
├── conftest.py                    # Fixtures & driver setup
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Dependencies
├── Dockerfile                     # Test container
├── docker-compose.yml             # Selenium + tests setup
└── README.md
```

---

## ✨ Key Features

- ✅ Page Object Model (clean separation of logic)
- ✅ Component-based architecture (reusable UI elements)
- ✅ Centralized `base_page` for shared functionality
- ✅ Pytest fixtures for scalable test setup
- ✅ Multiple test suites (login, inventory, checkout)
- ✅ Automatic HTML reporting
- ✅ Screenshot capture on failure
- ✅ Dockerized execution with Selenium container
- ✅ CI/CD with GitHub Actions

---

## ⚙️ Installation

```id="q7xk1d"
git clone https://github.com/ceka1986/Sauce_Demo_Python_Pytest.git
cd Sauce_Demo_Python_Pytest
```

Create virtual environment:

```id="m8dj2s"
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

Install dependencies:

```id="h2p9zk"
pip install -r requirements.txt
```

---

## ▶️ Running Tests Locally

Run all tests:

```id="m9r1tx"
pytest
```

Run specific test file:

```id="j4k2wd"
pytest tests/test_checkout.py
```

---

## 📊 Test Reporting

After test execution, an HTML report is generated:

```id="p3x9lz"
reports/report.html
```

Includes:

- Test results
- Logs (print output)
- Execution details

---

## 🐳 Docker Support

The framework supports full containerized execution.

### Services:

- **chrome** → Selenium standalone browser
- **tests** → Pytest execution

### Run tests:

```id="v8c2np"
docker compose up --build
```

### Selenium available at:

```id="z1w8yr"
http://localhost:4444
```

---

## 🔄 CI/CD (GitHub Actions)

Tests are automatically executed on:

- Push
- Pull Request

Pipeline includes:

- Environment setup
- Dependency installation
- Test execution

---

## 🧪 Test Coverage

### ✔ Login Tests

- Valid login
- Invalid login
- Locked out user test

### ✔ Inventory Tests

- Product display
- Add to cart
- Remove from cart

### ✔ Checkout Tests

- Complete checkout flow
- Data validation

---

## 📸 Screenshots on Failure

Screenshots are automatically saved in:

```id="n2s8xa"
screenshots/
```

Useful for debugging failed test cases.

---

## 📈 Future Improvements

- Allure reporting integration
- Parallel execution
- Cross-browser support
- Test data parameterization
- Docker image optimization

---

## 👤 Author

**Milovan Cekić**

- GitHub: https://github.com/ceka1986

---

## 📄 License

MIT License
