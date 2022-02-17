from page_object.main_page_locators import MainPageLocators
from page_object.base_page import BasePage
from page_object.login_page import LoginPage


class MainPage(BasePage):
    URL = 'http://localhost:8000/'

    def __init__(self, chrome_driver):
        super().__init__(chrome_driver, self.URL)

    def open_admin_page(self):
        admin_link = self.find_element(MainPageLocators.ADMIN_BUTTON_LOCATORS)
        admin_link.click()
        return LoginPage(self.chrome_driver, self.chrome_driver.current_url)
