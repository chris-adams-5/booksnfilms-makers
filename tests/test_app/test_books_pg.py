from playwright.sync_api import Page, expect
from data.books import books

def test_books_li_has(page: Page):
    page.goto("http://3.8.19.234:5001/books")

    li_elements = page.locator("li")

    for i, li_element in enumerate(li_elements.all()):

        assert li_element.locator("h2").all_inner_texts()[0] == books[i]["title"]

        expect(li_element.locator("h2")).to_have_text(books[i]["title"])

        assert li_element.locator("p").all_inner_texts()[0] == f"by {books[i]["author"]}"
