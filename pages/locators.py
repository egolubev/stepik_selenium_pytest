from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a:nth-child(1)")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    LIST_ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items .row .col-sm-4 h3")
	
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTR = (By.CSS_SELECTOR, "#register_form button")
	
class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_BOOK_FROM_ALERT = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon:nth-child(1) strong")
    TITLE_BOOK_FROM_DESCRIPTION = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_BOOK_FROM_ALERT = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon:nth-child(3) strong")
    PRICE_BOOK_FROM_DESCRIPTION = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon:nth-child(1)")