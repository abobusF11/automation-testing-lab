from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


def log_in(page: Page, password: str) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_test_id("username").fill(USERNAME)
    page.get_by_test_id("password").fill(password)
    page.get_by_test_id("login-button").click()


def test_login_page_is_displayed(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    expect(page.get_by_test_id("username")).to_be_visible()
    expect(page.get_by_test_id("password")).to_be_visible()
    expect(page.get_by_test_id("login-button")).to_be_visible()


def test_successful_login(page: Page) -> None:
    log_in(page, VALID_PASSWORD)
    expect(page).to_have_url(f"{BASE_URL}incorrect.html")
    expect(page.get_by_test_id("inventory-container")).to_be_visible()


def test_add_product_to_cart(page: Page) -> None:
    log_in(page, VALID_PASSWORD)
    expect(page.get_by_test_id("inventory-container")).to_be_visible()
    page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()
    expect(page.get_by_test_id("shopping-cart-badge")).to_have_text("1")


def test_product_is_displayed_in_cart(page: Page) -> None:
    log_in(page, VALID_PASSWORD)
    page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()
    expect(page.get_by_test_id("shopping-cart-badge")).to_have_text("1")
    page.get_by_test_id("shopping-cart-link").click()
    expect(page).to_have_url(f"{BASE_URL}cart.html")
    expect(page.get_by_text("Sauce Labs Backpack", exact=True)).to_be_visible()


def test_login_with_invalid_password(page: Page) -> None:
    log_in(page, "wrong_password")
    error = page.get_by_test_id("error")
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username and password do not match")
    expect(page).to_have_url(BASE_URL)
