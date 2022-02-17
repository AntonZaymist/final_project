from page_object.base_page import BasePage
from page_object.admin_page_locators import AdminPageLocators


class AdminPage(BasePage):

    def site_text(self):
        return self.find_element(AdminPageLocators.SITE_NAME)

    def open_groups(self):
        groups_button = self.find_element(AdminPageLocators.GROUPS_BUTTON)
        groups_button.clcik()
        return self.find_element(AdminPageLocators.TEXT_ADD_GROUP_1)



