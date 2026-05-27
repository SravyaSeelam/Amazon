from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self,page: Page):
        self.page=page
        self.proceed_to_checkout=page.locator("#sc-buy-box-ptc-button-announce")

    def click_proceed_to_checkout(self):
        self.proceed_to_checkout.scroll_into_view_if_needed()
        self.proceed_to_checkout.dispatch_event("click")

    def verify_checkout_page(self):
        expect(self.page.locator("#nav-checkout-title-header")).to_be_visible()
