from pages.basePage import BasePage, Locator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class StorefrontPage(BasePage):
    instance = None
    _CART_QUANTITY = Locator(By.CSS_SELECTOR, "div.cartDigit")
    _CHECKOUT_BUTTON = Locator(By.CSS_SELECTOR, "div.checkout-button > a")
    _CREATE_USER_LINK = Locator(By.CSS_SELECTOR, "div.buttonSection > div > button:nth-child(1)")
    _SIGN_IN_LINK = Locator(By.CSS_SELECTOR, "div.buttonSection > div > button:nth-child(2)")

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_quantity(self, search_term):
        cart_q = super().get_element(self._CART_QUANTITY)
        return int(cart_q.text)

    def get_tile_by_item_name(self, item_name):
        return super().get_element(Locator(By.XPATH, f"//div[@class='tileTitle'][text()='{item_name}']/ancestor::div[@class='tile']"))

    def add_to_cart_by_item_name(self, item_name, quantity=1):
        i = self.get_tile_by_item_name(item_name)

        for x in range(quantity):
            i.find_element(by=By.CSS_SELECTOR, value="div.tileAdd > button")\
                .click()

    def checkout_cart(self):
        self.get_element(self._CHECKOUT_BUTTON).click()

    def create_user_link(self):
        self.get_element(self._CREATE_USER_LINK).click()

    def sign_in_link(self):
        self.get_element(self._SIGN_IN_LINK).click()

