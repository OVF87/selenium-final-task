# Определение класса страницы входа
from selenium.webdriver.common.by import By
import time

from .base_page import BasePage
from locators import BasePageLocators
from locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        # Общая проверка страницы входа
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_authorized_user(self):
        # Проверка, что пользователь зарегистрирован
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"


    def should_be_login_form(self):
        # Проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_login_url(self):
        # Проверка на корректный url адрес страницы входа
        assert 'login' in self.browser.current_url or '?promo=newYear' in self.browser.current_url


    def register_new_user(self, email, password):
        # Регистрация нового пользователя
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_REGISTER).click()


    def should_be_register_form(self):
        # Проверка, что есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
