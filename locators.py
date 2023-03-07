# Определение локаторов
from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "a[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_TEXT_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner h2')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input[name*='registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input[name*='password1']")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[name*='password2']")
    BTN_REGISTER = (By.CSS_SELECTOR, "button[name*='regist']")


class ProductPageLocators():
    ADD_IN_BASKET_LINK = (By.CSS_SELECTOR, "button[class*='add-to']")
    TOTAL_IN_BASKET = (By.CSS_SELECTOR, "div [class*='alertinner'] p strong")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p[class*='price']")
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner ')
