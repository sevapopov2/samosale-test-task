"""Sign up page object model."""

from pages.base_page import BasePage


class SignUpPage(BasePage):
    """Sign up page object model class."""

    # constants
    BASE_URL = "https://dev.samosale.ru/auth/signup"
    # Search locators
    CHOOSE_MESSENGER_HEADING = "//h1[contains(text(), 'Выберите')]"

    def navigate_to_page(self):
        """Navigate to sign up page."""
        self.browser.get(self.BASE_URL)

    def find_choose_messenger_heading(self):
        """Find choose messenger heading."""
        heading = self.find_element_by_xpath(self.CHOOSE_MESSENGER_HEADING)
        return heading
