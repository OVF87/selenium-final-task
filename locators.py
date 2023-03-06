# Напишите здесь свой код :-)

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_IN_BASKET_LINK = (By.CSS_SELECTOR, "button[class*='add-to']")
    TOTAL_IN_BASKET = (By.CSS_SELECTOR, "div [class*='alertinner'] p strong")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p[class*='price']")
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div h1')
