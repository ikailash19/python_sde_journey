import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.skip
def test_google_title():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")

        # Check title contains 'Google'
        assert "Google" in page.title()

        browser.close()

def test_google_search():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")

        page.fill("textarea[name='q']", "Playwright Python")
        page.wait_for_timeout(3000)
        page.keyboard.press("Enter")

        page.wait_for_timeout(3000)

        assert "Playwright" in page.title()

        browser.close()

