# Напишите здесь свой код :-)
from pages.base_page import BasePage
from locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_in_basket_not_product(self):
        #проверка на отсутствие товара в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY), 'Basket not is empty'


    def should_be_guest_see_text_basket_empty(self):
        #проверка на текст корзина пуста
        assert self.get_text(*BasketPageLocators.BASKET_TEXT_IS_EMPTY).strip() == 'Your basket is empty. Continue shopping', 'Basket not is empty'
