from pages.Add_cartPage import Add_CartPage
from pages.Searchpage import SearchPage
from pages.checkoutpage import CheckoutPage


def test_checkout(logged_in_page):
    search = SearchPage(logged_in_page)
    search.search_amazon("Laptop")
    search.click_first_result()
    add_cart=Add_CartPage(logged_in_page)
    add_cart.click_add_cart()
    checkout=CheckoutPage(logged_in_page)
    checkout.click_proceed_to_checkout()
    checkout.verify_checkout_page()