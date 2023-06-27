import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MansCollectionRubashki(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    shirt_1 = "(//img[@alt='Рубашка из смесового льна с коротким рукавом'])[1]"
    radio_size_50 = "//input[@data-id='431802']"
    cart_button = "//a[@data-ui='cart-button']"
    cart_icon = "//span[@class='cartIcon']"

    # Getters

    def get_shirt_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shirt_1)))

    def get_radio_size_50(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radio_size_50)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_icon)))

    # Actions

    def click_shirt_1(self):
        self.get_shirt_1().click()
        print("Click Shirt 11725233-1000N")

    def click_radio_size_50(self):
        self.get_radio_size_50().click()
        print("Click Shirt Size 50")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click Cart Button")

    def click_cart_icon(self):
        self.get_cart_icon().click()
        print("Click Cart Icon")

    # Methods

    def select_product(self):
        time.sleep(5)
        self.click_shirt_1()
        self.get_current_url()
        self.click_radio_size_50()
        self.click_cart_button()
        self.click_cart_icon()

