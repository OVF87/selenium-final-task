# Тест главной страницы
import pytest
from selenium.webdriver.common.by import By

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@pytest.mark.login_guest
class TestLoginFormMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # Проверка перехода на страницу вход\регистрация
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_be_login_page()


    def test_guest_should_see_login_link(self, browser):
        # Проверка наличия ссылки на страницу входа\регистрации
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.should_be_login_link()

@pytest.mark.need_review
def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Проверка в корзине нет товара
    link = 'http://selenium1py.pythonanywhere.com/'
    page = ProductPage(browser,link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page = BasketPage(browser, page)
    page.should_be_in_basket_not_product()
    page.should_be_guest_see_text_basket_empty()
