from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    # LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.XPATH, '//*[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//*[@id="register_form"]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="id_registration-email"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="id_registration-password1"]')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '//*[@id="id_registration-password2"]')
    REGISTER_BUTTON = (By.XPATH,'//*[@id="register_form"]/button')


class ProductPageLocators:
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRODUCT_PUT_BASKET = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    PRODUCT_MESSAGE_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_MESSAGE_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRODUCT_MESSAGE_SUCCESS = (By.XPATH, '//*[@id="messages"]/div[1]/div')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, 'p')
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket-items")

