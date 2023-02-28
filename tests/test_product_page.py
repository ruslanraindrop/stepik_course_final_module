import pytest
from pages.product_page import ProductPage
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.parametrize('offer_id', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                      "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                      "?promo=offer6",
                                      pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                      "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, offer_id):
    offer_link = f"{link}{offer_id}"
    page = ProductPage(browser, offer_link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_added()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_disappeared_success_message()
