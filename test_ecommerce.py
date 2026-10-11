import json

import pytest
from selenium.common import TimeoutException
# in this file we are converting our current ecommerce file into framework file

from PageObjects.shopy import ShopPage
from PageObjects.login import LoginPage
from PageObjects.checking_out import PlacingOrder

# dynamically fethcing test_data from the test_commerce.json file under data directory

test_data_path = '../data/test_ecommerce.json'    # two dots are used to go back to previous folder from current folder path

with open(test_data_path) as f:
    test_data = json.load(f)     # here we converted the json into python object
    test_data_list = test_data['data']   # we are data items in a list format

# we'll have to use pytest parameterize fixture in order to pass the test data

@pytest.mark.parametrize("test_data_list_item", test_data_list)    # test_data_list_item indicates the index of the test_data_list
def test_ecommerce(invoking_browser, test_data_list_item):   # passing the argument inside the function call for to access the test data list items
    # the driver = webdriver.chrome() has been shifted to conftest under pytest fixture

    driver = invoking_browser
    driver.get('https://rahulshettyacademy.com/loginpagePractise/')

    #Logging to the page and then to the shop
    login1 = LoginPage(driver)
    print(login1.get_title())    # we go this get_title() method from the util class we defined
    '''
    another way to give XPATH locator for href links: //a[contains(@href, 'Shop')]  or in CSS way: a[href*='Shop']
    '''
    
    shop = login1.login(test_data_list_item["user_email"], test_data_list_item["password"])    # we are returning the shop object from login page, this is part of optimization
    shop.shop_page()
    print(shop.get_title())
    shop.current_cart_value()
    shop.product_add(test_data_list_item["item_name"])

    # user clicks the checkout button at cart review screen
    place_order = shop.checkout_button()
    print(place_order.get_title())
    place_order.review_card()
    place_order.delivery_country(test_data_list_item['country'])
    place_order.successful_checkout()

    # user is on last summary page

