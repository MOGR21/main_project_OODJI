import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class WomensCollectionPlatya(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    check_box_ultra = "//a[@href='/womens_collection/platya/ultra/']"
    check_box_krasnyj = "//a[@href='/womens_collection/platya/krasnyj/']"
    check_box_size_hl_48 = "//a[@href='/womens_collection/platya/size_hl_48-l-w/']"
    check_box_sale = "//a[@href='/womens_collection/platya/sale/']"
    radio_size_48 = "//input[@data-id=408766]"
    cart_button = "//a[@data-ui='cart-button']"
    cart_icon = "//span[@class='cartIcon']"

    word_cart = "//h1[@class='lft-16']"

    platye_1 = "(//a[@href='/womens_collection/11725139-4500N/'])[3]"

    # Getters

    def get_check_box_ultra(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_ultra)))

    def get_check_box_krasnyj(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_krasnyj)))

    def get_check_box_size_hl_48(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_size_hl_48)))

    def get_check_box_sale(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_sale)))

    def get_platye_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.platye_1)))

    def get_radio_size_48(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.radio_size_48)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_icon)))

    def get_word_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_cart)))

    # Actions

    def click_check_box_ultra(self):
        self.get_check_box_ultra().click()
        print("Click Check Box Ultra")

    def click_check_box_krasnyj(self):
        self.get_check_box_krasnyj().click()
        print("Click Check Box Krasnyj")

    def click_check_box_size_hl_48(self):
        self.get_check_box_size_hl_48().click()
        print("Click Check Box Size Hl 48")

    def click_check_box_sale(self):
        self.get_check_box_sale().click()
        print("Click Check Box Sale")

    def click_platye_1(self):
        self.get_platye_1().click()
        print("Select Platye")

    def click_radio_size_48(self):
        self.get_radio_size_48().click()
        print("Click Shirt Size 48")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click Cart Button")

    def click_cart_icon(self):
        self.get_cart_icon().click()
        print("Click Cart Icon")

    # Methods

    def select_product(self):
        time.sleep(3)
        self.click_check_box_ultra()
        self.click_check_box_krasnyj()
        self.click_check_box_size_hl_48()
        self.click_check_box_sale()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.click_platye_1()
        self.get_current_url()
        self.click_radio_size_48()
        self.click_cart_button()
        time.sleep(3)
        self.click_cart_icon()
        self.assert_word(self.get_word_cart(), "ВАША КОРЗИНА")

