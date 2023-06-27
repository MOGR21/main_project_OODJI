import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    basket_checkout_button = "//button[@data-entity='basket-checkout-button']"

    # Getters

    def get_basket_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket_checkout_button)))

    # Actions

    def click_basket_checkout_button(self,):
        self.get_basket_checkout_button().click()
        print("Click Basket Checkout Button")

    # Methods


