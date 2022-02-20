from page_object.base_page import BasePage
from page_object.group_page_locators import GroupPageLocators
from page_object.admin_page import AdminPage


class GroupPage(BasePage):
    def change_group_name(self):
        group_name = self.find_element(GroupPageLocators.NAME_GROUP_FIELD)
        group_name.clear()
        group_name.send_keys('new_name')
        save_button = self.find_element(GroupPageLocators.SAVE_BUTTON)
        save_button.click()
        return AdminPage(self.chrome_driver, self.chrome_driver.current_url)
