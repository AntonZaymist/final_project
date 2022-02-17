from page_object.base_page import BasePage
from page_object.admin_page_locators import AdminPageLocators
from page_object.login_page_locators import LoginPageLocators
from constants import ADMIN_LOGIN, ADMIN_PASSWORD


class AdminPage(BasePage):

    def site_text(self):
        return self.find_element(AdminPageLocators.SITE_NAME)

    def open_groups(self):
        groups_button = self.find_element(AdminPageLocators.GROUPS_BUTTON)
        groups_button.clcik()
        return self.find_element(AdminPageLocators.TEXT_ADD_GROUP_1)

    def admin_login(self):
        username = self.find_element(LoginPageLocators.USERNAME_INPUT_LOCATORS)
        username.send_keys(ADMIN_LOGIN)
        password = self.find_element(LoginPageLocators.PASSWORD_INPUT_LOCATORS)
        password.send_keys(ADMIN_PASSWORD)
        button = self.find_element(LoginPageLocators.LOG_IN_BUTTON)
        button.click()



