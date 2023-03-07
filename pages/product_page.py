# Определение класса страницы товара
from locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def should_be_add_product_in_basket(self):
        # Общая проверка страницы с промо
        self.should_be_promo()
        self.should_be_basket_url()
        self.should_be_click_add_basket()
        self.solve_quiz_and_get_code()
        self.should_be_product_in_basket()
        self.should_be_price_product_equal_total()


    def should_be_basket_url(self):
        # Проверка присутствия кнопки добавить в корзину
        assert self.is_element_present(*ProductPageLocators.ADD_IN_BASKET_LINK), \
        "Login form is not presented"


    def should_be_click_add_basket(self):
        # Нажимаем кнопку добавить в корзину
        self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET_LINK).click()


    def should_be_promo(self):
        # Проверка на промо в адресной ссылке
        assert "?promo=offer" in self.browser.current_url or "?promo=newYear" in self.browser.current_url


    def should_be_product_in_basket(self):
        # Проверка на правильный товар в корзине
        assert self.get_text(*ProductPageLocators.NAME_PRODUCT) == self.get_text(*ProductPageLocators.NAME_PRODUCT_IN_BASKET)


    def should_be_price_product_equal_total(self):
        # Проверка на совпадение цены товара и общей цены в корзине
        assert self.get_text(*ProductPageLocators.PRICE_PRODUCT) == self.get_text(*ProductPageLocators.TOTAL_IN_BASKET)


    def should_not_be_disappeared_success_message(self):
        # Проверка что сообщение о добавлении товара в корзину пропало
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should disappear"


    def should_not_be_success_message(self):
        # Проверка сообщения об успешном добавлении в корзину
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
