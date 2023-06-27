import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MapPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    input_citi = "//input[@id='adr']"
    search_button = "//button[@id='search_google_map']"

    # Getters

    def get_input_citi(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_citi)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    # Actions

    def click_select_map(self,):
        self.get_input_citi().click()
        self.get_input_citi().clear()
        self.get_input_citi().send_keys('Воронеж')
        print("Input Citi")

    def click_search_button(self,):
        self.get_search_button().click()
        print("Click Search Button")

    # Methods

    def looking_for_shops(self):
        self.click_select_map()
        time.sleep(5)
        self.click_search_button()
        time.sleep(5)
        self.get_current_url()
        self.get_screenshot()

