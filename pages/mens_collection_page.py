import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MansCollectionPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    rubashki = "(//a[@href='/mens_collection/rubashki/'])[2]"

    # Getters

    def get_rubashki(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.rubashki)))

    # Actions

    def click_rubashki(self,):
        with allure.step("Click Rubashki"):
            self.get_rubashki().click()
            print("Click Rubashki")

    # Methods


