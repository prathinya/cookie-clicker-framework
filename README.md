# Cookie Clicker Automation Framework

## Project Overview

This project is a Selenium automation framework developed using Python and Pytest for automating the Cookie Clicker game.

The framework follows the Page Object Model (POM) design pattern and includes reusable components for scalability and maintainability.

---

## Technologies Used

- Python
- Selenium
- Pytest
- WebDriver Manager

---

## Project Structure

cookie_clicker_framework/

│

├── pages/

│   └── cookie_clicker_page.py

│

├── tests/

│   └── test_cookie_clicker.py

│

├── utils/

│   ├── driver_factory.py

│   └── logger.py

│

├── config/

│   └── settings.py

│

├── requirements.txt

├── README.md

└── pytest.ini

---

## Installation

Install all dependencies:

pip install -r requirements.txt

---

## Run the Test

Run using pytest:

pytest

---

## Features

- Page Object Model (POM)
- Reusable Driver Setup
- Explicit Waits
- Logging Support
- Pytest Framework Integration
- Clean and Maintainable Code Structure

---

## Generate HTML Report

pytest --html=report.html

---

## Future Improvements

- Headless Browser Support
- Screenshot Capture on Failure
- CI/CD Integration
- Environment Variable Support
- Parallel Test Execution

---

## Author

Automation Framework developed using Selenium and Python.# cookie-clicker-framework
