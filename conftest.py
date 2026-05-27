import pytest
import os
from dotenv import load_dotenv
from pages.Loginpage import LoginPage


@pytest.fixture(scope="function")
def browser_context(playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def page_context(browser_context,base_url):
    page=browser_context.new_page()
    page.goto(base_url)
    yield page
    page.close()



@pytest.fixture(scope="function")
def logged_in_page(page):
    load_dotenv()
    page.goto("https://www.amazon.com")
    page.locator("#nav-link-accountList").click()
    login = LoginPage(page)
    email = os.getenv("AMAZON_EMAIL")
    password = os.getenv("AMAZON_PASSWORD")
    login.login_to_amazon(email, password)
    yield page
