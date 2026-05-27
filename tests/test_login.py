import time
import os
import pytest

from playwright.sync_api import Page, expect
from pages.Loginpage import LoginPage
from dotenv import load_dotenv



@pytest.mark.skip(reason="login is tested via logged_in_page fixture")
def test_login(page: Page):
    # page.goto("https://www.amazon.com/")
    # email=os.getenv("AMAZON_EMAIL")
    # password = os.getenv("AMAZON_PASSWORD")
    # login_page = LoginPage(page)
    # login_page.login_to_amazon(email, password)
    # username = os.getenv("AMAZON_USERNAME")
    # expect(page.locator("#nav-link-accountList")).to_contain_text(f"Hello, {username}")

    page.goto("https://www.amazon.com/")
    page.locator("#nav-link-accountList").click()

    load_dotenv()
    login_page = LoginPage(page)
    email = os.getenv("AMAZON_EMAIL")
    password = os.getenv("AMAZON_PASSWORD")
    login_page.login_to_amazon(email, password)
    username = os.getenv("AMAZON_USERNAME")
    expect(page.locator("#nav-link-accountList")).to_contain_text(f"Hello, {username}")


