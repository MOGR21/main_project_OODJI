import time

from selenium import webdriver

from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.map_page import MapPage
from pages.mens_collection_page import MansCollectionPage
from pages.mens_collection_rubashki import MansCollectionRubashki


def test_buy_mens_shirt():

    driver = webdriver.Chrome('C:\\Users\\MOGR\\PycharmProjects\\main_project_OODJI\\utilities\\chromedriver.exe')

    print("Start Test Buy Mens Shirt")

    shop = MainPage(driver)
    shop.open_main_page()

    shop.open_mens_collection()

    shirt = MansCollectionPage(driver)
    shirt.click_rubashki()
    shirt.get_current_url()
    shirt.assert_url('https://www.oodji.com/mens_collection/rubashki/')

    shirt_1 = MansCollectionRubashki(driver)
    shirt_1.select_product()

    cart = CartPage(driver)
    cart.get_current_url()
    cart.assert_url('https://www.oodji.com/cart/')
    cart.click_basket_checkout_button()
    cart.get_screenshot()

    print("End Test Looking For Shops")