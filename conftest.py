import pytest
from selenium.webdriver import Chrome

from page_object.main_page import MainPage


@pytest.fixture(scope="session")
def chrome_driver():
    chrome_driver = Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope="module")
def main_page(chrome_driver):
    page = MainPage(chrome_driver)
    page.open()
    return page
