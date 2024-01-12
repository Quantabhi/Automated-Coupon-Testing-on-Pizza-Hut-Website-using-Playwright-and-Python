# Automated-Coupon-Testing-on-Pizza-Hut-Website-using-Playwright-and-Python

This Python script utilizes Playwright to automate the testing of coupon codes on the Pizza Hut website. The script simulates user interactions, such as applying a coupon code, navigating through the website, and checking for any feedback messages.

## Dependencies

- **playwright**: A Python library for browser automation.
- **rich**: Used for enhanced console output.
- **time**: Standard Python library for time-related operations.
- **random**: Standard Python library for generating random numbers.

## Setup
pip install playwright rich

## Script Execution

The script launches a Chromium browser in non-headless mode for visibility during development.
It navigates to the Pizza Hut offers page and applies each coupon code in the list.
After applying a coupon, it performs various actions like selecting pickup, entering a search query, and clicking on checkout.
The script extracts and prints product details and any snackbar messages that may appear.

# Disclaimer

This script is for educational and demonstration purposes only. Ensure compliance with the terms of service of the targeted website. Use responsibly and consider the impact on the server load.
# Contributing
Feel free to contribute by opening issues or pull requests. Your feedback and enhancements are welcomed!
