from page_object.base_page import BasePage
from page_object.admin_page_locators import AdminPageLocators


class AdminPage(BasePage):
    def site_text(self):
        return self.find_element(AdminPageLocators.SITE_NAME).text
