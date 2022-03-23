import time
from .pages.product_page import ProductPage
from .pages.base_page import BasePage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.put_in_the_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.success_product_add()
    time.sleep(5)
