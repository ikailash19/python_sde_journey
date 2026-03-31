from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")

        # Check title contains 'Google'
        assert "Google" in page.title()

        browser.close()