import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class WomensCollectionPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    platya = "(//a[@href='/womens_collection/platya/'])[2]"

    # Getters

    def get_platya(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.platya)))

    # Actions

    def click_platya(self,):
        self.get_platya().click()
        print("Click Platya")

    # Methods


