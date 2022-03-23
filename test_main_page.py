import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()  # переход на страницу LoginPage
    time.sleep(5)
    # login_page = page.go_to_login_page() #  в переменную записываем возвращенный LoginPage из go_to_login_page(self)
    # login_page.should_be_login_page() #  проверяем все элементы страницы LoginPage
    login_page = LoginPage(browser, browser.current_url)  # в переменную записываем LoginPage
    login_page.should_be_login_page()  # проверяем все элементы страницы LoginPage


def test_guest_should_see_login_link(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
