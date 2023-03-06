# Напишите здесь свой код :-)

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

    #LOGIN_EMAIL_LINK = (By.CSS_SELECTOR, '#login_form input[type="email"]')
    #LOGIN_PASSWORD_LINK = (By.CS_SELECTOR, '#login_form input[type="passwors"]')
    #REGISTER_EMAIL_LINK = (By.CSS_SELECTOR, '#register_form input[type="email"]')
    #REGISTER_PASSWORD_LINK = (By.CSS_SELECTOR, '#register_form input[name*="password1"]')
    #REGISTER_CONFIRM_PASSWORD_LINK = (By.CSS_SELECTOR, '#register_form input[name*="password2"]')

class ProductPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "button[class*='add-to']")
