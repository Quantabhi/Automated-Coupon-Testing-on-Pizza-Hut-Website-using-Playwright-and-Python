from playwright.sync_api import sync_playwright
from rich import print
import time
import random


COUPONS = ["HUT0001", "HUT002","HUT8008LSM","HUT002","HUT002"]  # Replace this list with your actual coupon codes

def test_coupon(coupon):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.pizzahut.com.au/offers", timeout=60000)
        # Wait is added for the development phase. You can remove it in production
        page.wait_for_timeout(5000)
        time.sleep(random.uniform(3, 7))

        page.locator('//input[@class="coupon-code-injector-input form-control"]').fill(coupon)
        page.wait_for_timeout(8000)
        time.sleep(random.uniform(3, 7))
        page.keyboard.press("Enter")
        page.wait_for_timeout(8000)
        time.sleep(random.uniform(2, 7))
        page.click('#pickupDispositionTab')
        page.wait_for_timeout(8000)
        page.locator('div.position-relative.search-query-input-wrapper #searchQuery').nth(1).fill('2020')
        time.sleep(random.uniform(1, 4))
        page.wait_for_timeout(8000)
        page.keyboard.press("Enter")
        page.wait_for_timeout(8000)
        page.locator('div.ml-auto.flex-shrink-0 button.btn.btn-primary').nth(0).click()
        page.wait_for_timeout(8000)
        senond = page.locator("//h1[contains(@class, 'product-header-title')]").all_text_contents()
        print(senond)
        main_divs = page.locator("//div[contains(@class, 'snackbar-content-wrapper')]").all_text_contents()
        print(main_divs)
        time.sleep(random.uniform(5, 9))
        page.wait_for_timeout(8000)
        # Close the browser
        browser.close()

def main():
    for coupon in COUPONS:
        print(f"Testing coupon: {coupon}")
        test_coupon(coupon)
        print("\n" + "=" * 40 + "\n")

if __name__ == "__main__":
    main()

