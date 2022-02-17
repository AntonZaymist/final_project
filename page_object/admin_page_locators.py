from selenium.webdriver.common.by import By


class AdminPageLocators:
    SITE_NAME = (By.XPATH, "//*[@id='site-name']/a")
    POSTS_BUTTON = (By.XPATH, "//*[@href='/admin/app/post/']")
    GROUPS_BUTTON = (By.XPATH, "//*[@href='/admin/auth/group/']")
    USERS_BUTTON = (By.XPATH, "//*[@href='/admin/auth/user/']")
    TEXT_ADD_GROUP_1 = (By.XPATH, "//*[@href='/admin/auth/group/1/change/']")
