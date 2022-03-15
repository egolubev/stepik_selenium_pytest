from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.check_empty_list_in_basket() # корзина пуста
        self.check_text_for_empty_basket() # сообщение о пустой корзине найдено

    def check_empty_list_in_basket(self):
	    assert self.is_not_element_present(*BasketPageLocators.LIST_ITEMS_IN_BASKET), "Basket is not empty"

    def check_text_for_empty_basket(self):
        assert self.get_text_for_empty_bakset_page() is not None, "Text for empty basket not found"

    def get_text_for_empty_bakset_page(self):
        return self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET).text