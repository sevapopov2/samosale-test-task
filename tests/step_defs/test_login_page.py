"""Step definitions for login page tests."""

from pytest_bdd import given, scenarios, then, when

from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage

scenarios("../features/login_page.feature")


@given("login page is opened")
def open_login_page(browser):
    """Open login page."""
    SignUpPage(browser).navigate_to_page()
    SignUpPage(browser).open_login_page()
    heading = LoginPage(browser).find_login_heading()
    assert heading


@when("user finds a phone field")
def find_phone_field(browser):
    """Find and check a phone field."""
    phone_field = LoginPage(browser).find_phone_field()
    assert phone_field


@then("user enters phone number")
def enter_correct_number(browser):
    """Enter correct phone number."""
    phone_field = LoginPage(browser).write_phone_number(9213312345)
    assert phone_field == "(921) 331-2345"


@then("user presses sign in button")
def press_sign_in_button(browser):
    """Press sign in button."""
    LoginPage(browser).press_sign_in_button()


@then("error message displays")
def check_error_message(browser):
    """Check that error message is displayed."""
    error_message = LoginPage(browser).find_error_message()
    assert error_message
