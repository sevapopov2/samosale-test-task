"""Login page."""

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object model."""

    # Constants
    BASE_URL = "https://dev.samosale.ru/auth/login"
    # Search locators
    LOGIN_HEADING = "//h1[contains(text(), 'Вход в')]"

    def find_login_heading(self):
        """Find and return login heading."""
        heading = self.find_element_by_xpath(self.LOGIN_HEADING)
        return heading
