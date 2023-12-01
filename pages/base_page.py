"""Base Page class."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base page class that defines all methods to work with page objects."""

    def __init__(self, browser):
        """Class constructor defining webdriver instance and wait function."""
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)

    def find_element_by_xpath(self, xpath):
        """Find element by xpath."""
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def click_element_by_xpath(self, xpath):
        """Click earlier found by expath method."""
        self.find_element_by_xpath(xpath).click()
