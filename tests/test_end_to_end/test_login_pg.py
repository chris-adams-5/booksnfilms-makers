from playwright.sync_api import Page, expect

def test_login_redirects_to_home(page:Page, db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    page.goto("http://localhost:5001/login_page")
    page.get_by_placeholder("User Name / Email").fill("user")
    page.get_by_placeholder("Password").fill("password")
    page.get_by_role("button", name="Login").click()
    h1 = page.locator("h1")
    expect(h1).to_have_text("Books and Films")

    assert page.url == "http://localhost:5001/"

def test_login_fails(page:Page, db_connection):
    db_connection.seed("seeds/booksnfilms.pgsql")
    page.goto("http://localhost:5001/login_page")
    page.get_by_placeholder("User Name / Email").fill("user")
    page.get_by_placeholder("Password").fill("wrong")
    page.get_by_role("button", name="Login").click()

    assert page.url == "http://localhost:5001/login_failed"