from page_object.main_page import MainPage


def test_login(main_page):
    login_page = main_page.open_login_page()
    login_page.try_to_login()
