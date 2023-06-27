import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):

    url = "https://www.oodji.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    map = "(//a[@href='/map/'])[1]"
    cart = "//span[@class='cartIcon']"
    mens_collection = "//a[@href='/mens_collection/']"
    womens_collection = "//a[@href='/womens_collection/']"

    # Getters

    def get_select_map(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.map)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_mens_collection(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mens_collection)))

    def get_womens_collection(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.womens_collection)))

    # Actions

    def click_select_map(self,):
        self.get_select_map().click()
        print("Click Button Map")

    def click_cart(self,):
        self.get_cart().click()
        print("Click Cart")

    def click_mens_collection(self,):
        self.get_mens_collection().click()
        print("Click Mens Collection")

    def click_womens_collection(self, ):
        self.get_womens_collection().click()
        print("Click Womens Collection")

    # Methods

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()

    def select_map(self):
        self.get_current_url()
        self.click_select_map()

    def open_mens_collection(self):
        self.click_mens_collection()
        self.get_current_url()

    def open_womens_collection(self):
        self.click_womens_collection()
        self.get_current_url()

    def open_cart(self):
        self.click_cart()
        self.get_current_url()
