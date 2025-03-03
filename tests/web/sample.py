import pytest  #  Python: Importing pytest for test setup and fixtures
from playwright.sync_api import sync_playwright  #  Playwright: Importing sync version of Playwright

with sync_playwright() as p:  #  Playwright: Starting Playwright context (internally runs `playwright install` if needed)
    browser = p.chromium.launch(headless=False, slow_mo=700)  #  Playwright: Launching a Chromium browser (headless=False means UI is visible)
    context = browser.new_context()  #  Playwright: Creating a new browser session (like a new Chrome profile)
    page = context.new_page()  #  Playwright: Opening a new tab in the browser
    page.goto("https://google.com")  #  Playwright: Navigating to the website
    page.locator("#APjFqb").fill("playwright")
