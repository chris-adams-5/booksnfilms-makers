from playwright.sync_api import Page, expect

def test_landing_has_title(page: Page):
    page.goto("http://3.8.19.234:5001")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Books and Films")