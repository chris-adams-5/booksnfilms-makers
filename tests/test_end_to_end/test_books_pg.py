from playwright.sync_api import Page, expect
from data.books import books

def test_books_li_has(page: Page, db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    page.goto("http://localhost:5001/books")

    li_elements = page.locator("li")

    for i, li_element in enumerate(li_elements.all()):

        assert li_element.locator("h2").all_inner_texts()[0] == books[i]["title"]

        expect(li_element.locator("h2")).to_have_text(books[i]["title"])

        assert li_element.locator("p").all_inner_texts()[0] == f"by {books[i]["author"]}"

def test_books_form(page: Page):
    page.goto("http://localhost:5001/books")
    page.get_by_placeholder("Title").fill("The Hitchikers Guide to the Galaxy")
    page.get_by_placeholder("Author").fill("Douglas Adams")
    page.get_by_placeholder("Book Summary").fill("A story that begins with a man")
    page.get_by_placeholder("Image url").fill("https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1404613595i/13.jpg")
    page.get_by_role("button", name="Submit").click()

    li_elements = page.locator("li")

    books.append({
    "title": "The Hitchikers Guide to the Galaxy",
    "author": "Douglas Adams"
  })

    for i, li_element in enumerate(li_elements.all()):

        assert li_element.locator("h2").all_inner_texts()[0] == books[i]["title"]

        expect(li_element.locator("h2")).to_have_text(books[i]["title"])

        assert li_element.locator("p").all_inner_texts()[0] == f"by {books[i]["author"]}"
