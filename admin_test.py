from page_object.main_page import MainPage
import time


def test_admin_page(main_page):
    admin_page = main_page.open_admin_page()
    assert admin_page.site_text().text == 'Django administration'


def test_add_group(main_page):
    admin_page = main_page.open_admin_page()
    admin_page.open_groups()
    assert admin_page.open_groups.text == 'test_group'


