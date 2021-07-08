from pages.basePage import BasePage, Locator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    instance = None
    _CC_FNAME = Locator(By.NAME, "firstName")
    _CC_LNAME = Locator(By.NAME, "lastName")
    _CC_NUMBER = Locator(By.NAME, "cardNumber")
    _CC_CVV = Locator(By.NAME, "cvv")
    _CC_EXP_DATE = Locator(By.NAME, "expirationDate")
    _BILLING_COMPANY = Locator(By.NAME, "company")
    _BILLING_TITLE = Locator(By.NAME, "title")
    _BILLING_ADDR = Locator(By.NAME, "address")
    _BILLING_CITY = Locator(By.NAME, "city")
    _CONTINUE_SHOPPING_BUTTON = Locator(By.CSS_SELECTOR, "div.infoButton > a > div")
    _COMPLETE_ORDER_BUTTON = Locator(By.CSS_SELECTOR, "div.infoButton > button")
    _CART_PRODUCTS_SECTION = Locator(By.CSS_SELECTOR, "div.productSection")
    _CART_SUBTOTAL = Locator(By.CSS_SELECTOR, "div.totalDetails div:nth-child(1) > span:nth-child(2)")
    _CART_SHIPPING = Locator(By.CSS_SELECTOR, "div.totalDetails div:nth-child(2) > span:nth-child(2)")
    _CART_TAXES = Locator(By.CSS_SELECTOR, "div.totalDetails div:nth-child(3) > span:nth-child(2)")
    _CART_TOTAL = Locator(By.CSS_SELECTOR, "div.totalFinal > span:nth-child(2)")

    def __init__(self, driver):
        super().__init__(driver)

    def get_subtotal(self):
        cart_q = super().get_element(self._CART_SUBTOTAL)
        return float(cart_q.text.replace("$", ""))

    def get_total(self):
        cart_q = super().get_element(self._CART_TOTAL)
        return float(cart_q.text.replace("$", ""))

    def get_shipping(self):
        cart_q = super().get_element(self._CART_SHIPPING)
        return float(cart_q.text.replace("$", ""))

    def get_taxes(self):
        cart_q = super().get_element(self._CART_TAXES)
        return float(cart_q.text.replace("$", ""))

    def get_cart_items(self):
        r = []
        prod_items = super().get_element(self._CART_PRODUCTS_SECTION).find_elements(by=By.CSS_SELECTOR, value="div.productItem")

        for prod in prod_items:
            r.append((prod.find_element(by=By.CSS_SELECTOR, value="div.columnCenter > div").text, int(''.join(filter(str.isdigit, prod.find_element(by=By.CSS_SELECTOR, value="div.columnCenter > div:nth-child(2) > span:nth-child(1)").text)))))

        return dict(r)

    def continue_shopping(self):
        self.get_element(self._CONTINUE_SHOPPING_BUTTON).click()

    def complete_order(self):
        self.get_element(self._COMPLETE_ORDER_BUTTON).click()

