# Import necessary libraries
from playwright.sync_api import sync_playwright
from rich import print
import time
import random

# List of coupon codes to test
COUPONS = ["HUT0001", "HUT002", "HUT8008LSM", "HUT002", "HUT002"]

# Function to test a coupon code on the Pizza Hut website
def test_coupon(coupon):
    # Launch a Chromium browser in non-headless mode for visibility
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the Pizza Hut offers page
        page.goto("https://www.pizzahut.com.au/offers", timeout=60000)

        # Add a wait time for development purposes (can be removed in production)
        page.wait_for_timeout(5000)
        time.sleep(random.uniform(3, 7))

        # Fill the coupon code in the input field
        page.locator('//input[@class="coupon-code-injector-input form-control"]').fill(coupon)
        page.wait_for_timeout(8000)
        time.sleep(random.uniform(3, 7))

        # Simulate pressing Enter key to apply the coupon
        page.keyboard.press("Enter")
        page.wait_for_timeout(8000)
        time.sleep(random.uniform(2, 7))

        # Click on the pickup tab
        page.click('#pickupDispositionTab')
        page.wait_for_timeout(8000)

        # Fill the search query input with '2020' (example value)
        page.locator('div.position-relative.search-query-input-wrapper #searchQuery').nth(1).fill('2020')
        time.sleep(random.uniform(1, 4))
        page.wait_for_timeout(8000)

        # Simulate pressing Enter key to perform the search
        page.keyboard.press("Enter")
        page.wait_for_timeout(8000)

        # Click on the checkout button
        page.locator('div.ml-auto.flex-shrink-0 button.btn.btn-primary').nth(0).click()
        page.wait_for_timeout(8000)

        # Extract and print product details
        product_title = page.locator("//h1[contains(@class, 'product-header-title')]").all_text_contents()
        print(product_title)

        # Extract and print any snackbar messages
        snackbar_messages = page.locator("//div[contains(@class, 'snackbar-content-wrapper')]").all_text_contents()
        print(snackbar_messages)

        # Add a random wait time before closing the browser
        time.sleep(random.uniform(5, 9))
        page.wait_for_timeout(8000)

        # Close the browser
        browser.close()

# Main function to test each coupon code
def main():
    for coupon in COUPONS:
        print(f"Testing coupon: {coupon}")
        test_coupon(coupon)
        print("\n" + "=" * 40 + "\n")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
