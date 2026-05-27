from playwright.sync_api import Page


class LoginPage:
    def __init__(self,page: Page):
        self.page=page
        self.username=page.locator("#ap_email_login")
        self.continue_button=page.locator("#continue input[type='submit']")
        self.password=page.locator("#ap_password")
        self.signin_button=page.locator("#signInSubmit")

    def login_to_amazon(self,username,password):
        self.username.fill(username)
        self.continue_button.click()
        self.password.fill(password)
        self.signin_button.click()




