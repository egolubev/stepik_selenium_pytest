from .base_page import BasePage
from .locators import ProductPageLocators
import html
import time

class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        self.add_product_to_basket() # добавляем в корзину
        self.solve_quiz_and_get_code() # получаем код
        title_from_page = self.get_title_from_page() # получаем название со страницы
        price_from_page = self.get_price_from_page() # получаем стоимость со страницы
        self.check_title_and_price_book_after_add_to_basket(title_from_page, price_from_page) # проверяем заголовок и стоимость

    def add_product_to_basket(self):
        button_add_product = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_product.click()
		
    def check_title_and_price_book_after_add_to_basket(self, title_from_page, price_from_page):
        assert title_from_page == self.get_title_from_alert() and price_from_page == self.get_price_from_alert(), "Check title/price is failed"
		
    def get_price_from_page(self):
        price_book_from_description = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_FROM_DESCRIPTION)
        return html.unescape(price_book_from_description.text)
	
    def get_price_from_alert(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_BOOK_FROM_ALERT).text

    def get_title_from_page(self):
        title_book_from_description = self.browser.find_element(*ProductPageLocators.TITLE_BOOK_FROM_DESCRIPTION)
        return html.unescape(title_book_from_description.text)
		
    def get_title_from_alert(self):
        return self.browser.find_element(*ProductPageLocators.TITLE_BOOK_FROM_ALERT).text
		
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
		
    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should disappeared"