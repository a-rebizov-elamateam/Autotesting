from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "BASKET_ITEMS is located"

    def should_be_text_the_basket_is_empty(self):
        assert 'Ваша корзина пуста' in self.browser.find_element(*BasketPageLocators.TEXT_BASKET_IS_EMPTY).text, \
            "TEXT_BASKET_IS_EMPTY is not located"
