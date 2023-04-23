from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, "basket")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    SHOPPING_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".items")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert:nth-child(1) > .alertinner > strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3) > .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(3) > .alertinner")
