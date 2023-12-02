"""Login page."""

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object model."""

    # Constants
    BASE_URL = "https://dev.samosale.ru/auth/login"
    # Search locators
    LOGIN_HEADING = "//h1[contains(text(), 'Вход в')]"
    PHONE_FIELD = "//input[@placeholder='Номер телефона']"
    SIGN_IN_BUTTON = "//button[@type='submit']"
    ERROR_MESSAGE = "//div[@class='ant-form-explain']"

    def find_login_heading(self):
        """Find and return login heading."""
        heading = self.find_element_by_xpath(self.LOGIN_HEADING)
        return heading

    def find_phone_field(self):
        """Find and return phone field."""
        phone_field = self.find_element_by_xpath(self.PHONE_FIELD)
        return phone_field

    def write_phone_number(self, number):
        """Write the phone number in the field."""
        phone_field = self.find_element_by_xpath(self.PHONE_FIELD)
        phone_field.send_keys(number)
        return phone_field.get_attribute("value")

    def press_sign_in_button(self):
        """Press sign in button."""
        self.click_element_by_xpath(self.SIGN_IN_BUTTON)

    def find_error_message(self):
        """Find phone number error message."""
        return self.find_element_by_xpath(self.ERROR_MESSAGE)
