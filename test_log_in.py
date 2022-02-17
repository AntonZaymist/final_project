from page_object.main_page import MainPage


def test_login(chrome_driver):
    page = MainPage(chrome_driver)
    page.open()
    login_page = page.open_admin_page()
    login_page.try_to_login()
