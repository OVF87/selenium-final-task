# Напишите здесь свой код :-)
from pages.base_page import BasePage
from locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_product_in_basket(self):
        self.should_be_promo()
        self.should_be_basket_url()
        self.should_be_click_add_basket()
        self.solve_quiz_and_get_code()


    def should_be_basket_url(self):
        #проверка присутствия кнопки добавить в корзину
        assert self.is_element_present(*ProductPageLocators.BASKET_LINK), "Login form is not presented"


    def should_be_click_add_basket(self):
        #нажимаем кнопку добавить в корзину
        self.browser.find_element(*ProductPageLocators.BASKET_LINK).click()


    def should_be_promo(self):
        assert "?promo=newYear" in self.browser.current_url



