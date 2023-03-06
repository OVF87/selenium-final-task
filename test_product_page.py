# Напишите здесь свой код :-)
import pytest
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from pages.basket_page import BasketPage



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
    #проверка страницы продукта
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_product_in_basket()
    page.should_be_click_add_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_in_basket()
    page.should_be_price_product_equal_total()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #Проверяем, что нет сообщения об успехе not_element_present
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_be_basket_url()
    page.should_be_click_add_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    #Проверяем, что нет сообщения об успехе с помощью not_element_present
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_be_basket_url()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    #Проверяем, что нет сообщения об успехе с помощью is_disappeared
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_be_basket_url()
    page.should_be_click_add_basket()
    page.should_not_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    #проверка видимости ссылки на страницу входа
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-thestars_95/'
    page = ProductPage(browser,link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    #проверка перехода на страницу входа
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-thestars_95/'
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    #проверка в корзине нет товара
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser,link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page = BasketPage(browser, page)
    page.should_be_in_basket_not_product()
    page.should_be_guest_see_text_basket_empty()



