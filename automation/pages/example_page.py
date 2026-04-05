class ExamplePage:
    def __init__(self, page):
        self.page = page
        self.heading = page.locator("h1")
        self.more_info_link = page.locator("a")

    def load(self):
        self.page.goto("https://example.com")

    def get_heading(self):
        return self.heading.inner_text()

    def click_more_info(self):
        self.more_info_link.click()

    def get_url(self):
        return self.page.url