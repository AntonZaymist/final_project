from selenium.webdriver.common.by import By


class GroupPageLocators:
    NAME_GROUP_FIELD = (By.XPATH, "//*[@id='id_name']")
    SAVE_BUTTON = (By.XPATH, "//*[@value='Save']")
