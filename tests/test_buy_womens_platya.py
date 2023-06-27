import time

from selenium import webdriver

from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.map_page import MapPage
from pages.mens_collection_page import MansCollectionPage
from pages.mens_collection_rubashki import MansCollectionRubashki
from pages.womens_collection_page import WomensCollectionPage
from pages.womens_collection_platya import WomensCollectionPlatya


def test_buy_womens_platya():

    driver = webdriver.Chrome('C:\\Users\\MOGR\\PycharmProjects\\main_project_OODJI\\utilities\\chromedriver.exe')

    print("Start Test Buy Womens Platya")

    shop = MainPage(driver)
    shop.open_main_page()

    shop.open_womens_collection()

    platya = WomensCollectionPage(driver)
    platya.click_platya()
    platya.get_current_url()
    platya.assert_url('https://www.oodji.com/womens_collection/platya/')

    platye_1 = WomensCollectionPlatya(driver)
    platye_1.select_product()

    cart = CartPage(driver)
    cart.get_current_url()
    cart.assert_url('https://www.oodji.com/cart/')
    cart.click_basket_checkout_button()
    cart.get_screenshot()

    print("End Test Buy Womens Platya")