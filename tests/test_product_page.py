import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('offer_id', ["0", "1", "2", "3", "4", "5", "6",
                                      pytest.param("7", marks=pytest.mark.xfail),
                                      "8", "9"])
def test_guest_can_add_product_to_cart(browser, offer_id):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_id}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_added()
