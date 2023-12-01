"""Sign up page step definitions for BDD tests."""

from pytest_bdd import given, scenarios, then, when

from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage

scenarios("../features/sign_up_page.feature")


@given("sign up page is opened")
def open_sign_up_page(browser):
    """Open sign up page."""
    SignUpPage(browser).navigate_to_page()


@then("user finds choose messenger heading")
def find_choose_messenger_heading(browser):
    """Find choose messenger heading."""
    sign_up_page = SignUpPage(browser)
    heading = sign_up_page.find_choose_messenger_heading()
    assert heading


@when("user presses login link")
def open_login_page(browser):
    """Open login page."""
    SignUpPage(browser).open_login_page()


@then("user finds sign in heading")
def find_sign_in_heading(browser):
    """Find sign in heading on a log in page."""
    LoginPage(browser).find_login_heading()
