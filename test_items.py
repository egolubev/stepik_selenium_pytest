link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button_add_basket(browser):
    browser.get(link)
    assert browser.find_elements_by_class_name("btn-add-to-basket"), 'basket button not found'