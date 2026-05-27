from playwright.sync_api import Page, expect


class Add_CartPage:
    def __init__(self,page: Page):
        self.page=page
        self.add_cart_button=page.locator("#add-to-cart-button")
        self.buynow_button=page.locator("#buy-now-button")
        self.quantity_button=page.get_by_label("Quantity:")

    def select_quantity(self, quantity):
        self.quantity_button.select_option(str(quantity))

    def click_add_cart(self):
        self.add_cart_button.click()
        self.page.wait_for_timeout(2000)
        try:
            no_thanks = self.page.locator("#attachSiNoCoverage")
            if no_thanks.is_visible():
                no_thanks.click()
        except:
            pass

    def click_buynow(self):
        self.buynow_button.click()

    def verify_cart_count(self,quantity):
        cart_count = self.page.locator("#nav-cart-count")
        expect(cart_count).not_to_have_text("0")
        expect(cart_count).to_have_text(str(quantity))