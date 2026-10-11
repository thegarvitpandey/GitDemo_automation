from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

'''
running only tagged test cases: python -m pytest -m smoke
'''


@pytest.mark.smoke
def test_sorting_tables(invoking_browser):

    driver = invoking_browser
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')

    driver.implicitly_wait(5)

    try:
        # opening the entire table view default is 5 we are going to 20
        driver.find_element(By.XPATH, '//select[@id = "page-menu"]//option[3]').click()

        empty_list1 = []
        # grabbing the list
        veggie_list = driver.find_elements(By.XPATH, '//tr/td[1]')
        for item in veggie_list:
            empty_list1.append(item.text)

        print("Original list: ", empty_list1)

        # sorting the list
        sorted_list = []
        for item in sorted(veggie_list, key=lambda veggie: veggie.text):
            sorted_list.append(item.text)

        print("Python sorted list: ", sorted_list)

        # clicking the header to sort the list
        header = driver.find_element(By.XPATH, '//table/thead/tr/th[1]')  # or // //table/thead/tr/th[@tabindex ='0']
        print("Clicked", header.text)
        header.click()

        list3 = []
        # getting the list sorted by click option
        veggie_list2 = driver.find_elements(By.XPATH, '//tr/td[1]')
        for item in veggie_list2:
            list3.append(item.text)

        print("Sorted list after clicking the button: ", list3)

        assert list3 == sorted_list
        print('they are sorted')

    except Exception as e:
        print(e)