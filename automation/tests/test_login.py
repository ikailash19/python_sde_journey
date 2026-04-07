from automation.pages.internet_page import InternetPage
from automation.utils.helpers import print_step

def test_login_success(page):
    print_step("Launching site")
    site = InternetPage(page)

    site.load()
    site.go_to_login()
    site.login("tomsmith", "SuperSecretPassword!")

    page.wait_for_timeout(2000)

    print("Message:", site.get_success_message())

    assert "You logged into a secure area!" in site.get_success_message()