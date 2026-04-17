from archive.automation.pages.example_page import ExamplePage

def test_example_page(page):
    example = ExamplePage(page)

    example.load()

    assert "Example Domain" in page.title()

    assert example.get_heading() == "Example Domain"

    example.click_more_info()

    assert "iana" in example.get_url()
    page.wait_for_timeout(3000)
