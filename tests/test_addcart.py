from pytest_playwright.pytest_playwright import page

from pages.Add_cartPage import Add_CartPage
from pages.Searchpage import SearchPage



def test_cart(logged_in_page):
    search = SearchPage(logged_in_page)
    search.search_amazon("Laptop")
    search.click_first_result()
    add_cart=Add_CartPage(logged_in_page)
    add_cart.click_add_cart()
    add_cart.verify_cart_count(1)

