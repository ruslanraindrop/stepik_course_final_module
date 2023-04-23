from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, f"This url is not basket url: {self.browser.current_url}"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Success message is presented, but should not be"

    def should_be_shopping_text(self):
        assert self.is_element_present(*BasketPageLocators.SHOPPING_TEXT), "Shopping link is not presented"
