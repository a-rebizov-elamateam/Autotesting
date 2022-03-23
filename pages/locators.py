from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    # LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.XPATH, '//*[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//*[@id="register_form"]')


class ProductPageLocators:
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRODUCT_PUT_BASKET = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    PRODUCT_MESSAGE_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_MESSAGE_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRODUCT_MESSAGE_SUCCESS = (By.XPATH, '//*[@id="messages"]/div[1]/div')
