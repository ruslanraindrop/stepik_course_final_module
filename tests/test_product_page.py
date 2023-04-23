import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.parametrize('offer_id', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                      "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                      "?promo=offer6",
                                      pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                      "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, offer_id):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    offer_link = f"{link}{offer_id}"
    page = ProductPage(browser, offer_link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_added()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
