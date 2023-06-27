from selenium import webdriver

from pages.main_page import MainPage
from pages.map_page import MapPage


def test_looking_for_shops():

    driver = webdriver.Chrome('C:\\Users\\MOGR\\PycharmProjects\\main_project_OODJI\\utilities\\chromedriver.exe')

    print("Start Test Looking For Shops")

    shop = MainPage(driver)
    shop.open_main_page()
    shop.select_map()

    serch = MapPage(driver)
    serch.looking_for_shops()

    print("End Test Looking For Shops")