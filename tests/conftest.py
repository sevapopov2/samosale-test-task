"""Setting up shared fixtures to start and quit Selenium driver."""

import pytest
from pytest_bdd import given, when
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage


@pytest.fixture
def browser():
    """Inicializing and closing webdriver instance."""
    # Inicialize WebDriver instance
    webbrowser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    # Maximize browser window
    webbrowser.maximize_window()
    # Set up calls to wait for 2 seconds
    webbrowser.implicitly_wait(2)
    # Return webdriver instance
    yield webbrowser
    # Quit the webdriver instance
    webbrowser.quit()

