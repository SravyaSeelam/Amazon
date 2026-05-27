from playwright.sync_api import Page


class SearchPage:
    def __init__(self,page: Page):
        self.page=page
        self.search_button=page.locator("#nav-search-submit-button")
        self.search_input=page.locator("#twotabsearchtextbox")
        self.search_description=page.locator("#searchDropdownBox")

    def search_amazon(self,search_term, department="All Departments"):
        self.search_description.select_option(label=department)
        self.search_input.fill(search_term)
        self.search_button.click()

    def click_first_result(self):
        self.page.locator("[data-component-type='s-search-result']").filter(
            has=self.page.locator("button[name='submit.addToCart']")
        ).first.locator("h2 span").click()