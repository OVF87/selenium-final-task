# Определение класса страницы корзины
from locators import BasketPageLocators
from pages.base_page import BasePage


class BasketPage(BasePage):
    def should_be_guest_see_text_basket_empty(self):
        # Проверка на текст, что корзина пуста
        assert self.get_text(*BasketPageLocators.BASKET_TEXT_IS_EMPTY).strip() == 'Your basket is empty. Continue shopping', 'Basket not is empty'


    def should_be_in_basket_not_product(self):
        # Проверка на отсутствие товара в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY), 'Basket not is empty'
