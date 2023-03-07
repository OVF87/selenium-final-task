# Тестирование страницы товаров
import pytest
from selenium.webdriver.common.by import By
import time

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # Проверка страницы продукта
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_in_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Проверка, что нет сообщения об успехе not_element_present
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_be_basket_url()
    page.should_be_click_add_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # Проверка, что нет сообщения об успехе с помощью not_element_present
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_be_basket_url()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_should_see_login_link_on_product_page(browser):
    # Проверка видимости ссылки на страницу входа
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-thestars_95/'
    page = ProductPage(browser,link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # Проверка перехода на страницу входа
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-thestars_95/'
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Проверка в корзине нет товара
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser,link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page = BasketPage(browser, page)
    page.should_be_in_basket_not_product()
    page.should_be_guest_see_text_basket_empty()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Проверка, что нет сообщения об успехе с помощью is_disappeared
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_be_basket_url()
    page.should_be_click_add_basket()
    page.should_not_be_disappeared_success_message()


@pytest.mark.product
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        self.page = LoginPage(browser, self.link)
        self.page.open()
        self.email = str(time.time()) + "@fakemail.org"
        self.password = '!q1w2e3r4t5'
        self.page.register_new_user(self.email, self.password)
        self.page.should_be_authorized_user()


    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # Проверка страницы продукта
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.should_be_basket_url()
        self.page.should_be_click_add_basket()
        self.page.should_be_product_in_basket()
        self.page.should_be_price_product_equal_total()


    def test_user_cant_see_success_message(self, browser):
        # Проверка, что нет сообщения об успехе с помощью not_element_present
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
        self.page = ProductPage(browser, self.link, 0)
        self.page.open()
        self.page.should_be_basket_url()
        self.page.should_not_be_success_message()
