from playwright.sync_api import Page, expect
from data.quotes import quotes

def test_books_li_has(page: Page):
    page.goto("http://3.8.19.234:5001/quotes")

    li_elements = page.locator("li")

    for i, li_element in enumerate(li_elements.all()):
        expect(li_element.locator("p")).to_have_text(quotes[i]["quote"])