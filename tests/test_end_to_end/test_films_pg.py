from playwright.sync_api import Page, expect
from data.films import films

# def test_films_list_has(page: Page, db_connection):

#     db_connection.seed("seeds/booksnfilms.pgsql")
#     page.goto("http://localhost:5001/books")

#     li_elements = page.locator("li")

#     for i, li_element in enumerate(li_elements.all()):

#         assert li_element.locator("h2").all_inner_texts()[0] == books[i]["title"]

#         expect(li_element.locator("h2")).to_have_text(books[i]["title"])

#         assert li_element.locator("p").all_inner_texts()[0] == f"by {books[i]["author"]}"

def test_films_form(page: Page, db_connection):

    db_connection.seed('seeds/booksnfilms.pgsql')

    page.goto("http://localhost:5001/films")
    page.get_by_placeholder("Title").fill("The Lost World")
    page.get_by_placeholder("Run Time Minutes").fill('129')
    page.get_by_placeholder("Director").fill("Steven Spielberg")
    page.get_by_placeholder("imdb").fill("https://www.imdb.com/title/tt0119567/")

    page.get_by_role("button", name="Submit").click()

    li_elements = page.locator("li")
    
    expected_films = films

    expected_films.append(      
        {
        "title":'The Lost World', 
        "run_time_minutes": 129, 
        "director": 'Steven Spielberg', 
        "imdb":'https://www.imdb.com/title/tt0119567/'
        },  
    )
 
    for i, li_element in enumerate(li_elements.all()):
            assert li_element.locator("h2").all_inner_texts()[0] == expected_films[i]["title"]
            assert li_element.locator("p").all_inner_texts()[0] == expected_films[i]["director"]

