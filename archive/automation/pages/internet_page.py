class InternetPage:
    def __init__(self, page):
        self.page = page
        self.form_auth_link = page.locator("text=Form Authentication")
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_btn = page.locator("button[type='submit']")
        self.success_msg = page.locator(".flash.success")

    def load(self):
        self.page.goto("https://the-internet.herokuapp.com")

    def go_to_login(self):
        self.form_auth_link.click()

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()

    def get_success_message(self):
        return self.success_msg.inner_text()