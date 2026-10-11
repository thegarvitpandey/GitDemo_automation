# this is conftest file, it would have all the necessary configurations as needed
# just mention all the fixture and other dependencies here and the pytest would take care of rest
# on at other files you don't need to have dedicated pytest fixture tags and other things
import os

# now removing this fixture thing from files, they will still be able to use the setup defined here

#fixtures are used as setup and tear down methods for test cases

# conftest file is used to generalize the fixtures and make it available to all test cases

# it's better to use the class to run the fixture as it allows us to define the setup once and not everytime we write a test case / methods
# so here in the scope we'll have to mention that scope = 'class' so that the fixture only once before the class starts and once the
# once the class ends and not evertime to avoid redencency


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None # initializing the driver as none, since we are getting the driver from one function and want to use it in another


@pytest.fixture(scope='class')
def setup(request):
    print('this would be executed first')
    yield
    print('this would be executed after the fixture')

@pytest.fixture()
def dataLoad():
    print('this is to learn the data driven testing')
    return ('Garvit', 'Pandey', 123)

# on defining the fixture for a class, it runs once before class is initiated and once after the class is terminated
# here we are parameterizing the fixture and telling it to run 3 times on different browsers
# that means out fixture would run thrice: first for chrome, second for firefox and 3rd for safari
# this would be helpful if we want to run a fixture / feature which might behave variably over platforms

@pytest.fixture(params=[('chrome', 'Google'), 'firefox', ('safari', 'Apple')])
def crossBrowser_test(request):
    return request.param


# invoking the browser from here

# we have to predefine some of the browser options
# the following method is prefeined and is present on pytest documentation as to how to use --browser_name functionality
def pytest_addoption(parser):
        parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")


@pytest.fixture(scope='function')
def invoking_browser(request):
    global driver # by defining it as global we are informing that the driver we declared above is the same as we are
        # we are using here and calling and then once this driver is activated we are using it for capture_screnshot() function as well

    browser_name = request.config.getoption('browser_name') # this would help running the file and mentioning the intended browser at cmd only
    if browser_name == 'chrome':      # at cmd run like: python -m pytest test_file.py --browser_name chrome
        chrome_options = Options()

        # 1. Turn off Chrome Password Manager & Breach/Leak Warnings completely
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "safebrowsing.enabled": False
        })
        # 2. Disable the UI bubble notifications
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-features=PasswordLeakDetection,SafeBrowsing")
        driver=webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(5)

    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)

    yield driver


# generated HTML Reports
'''
to generate or run the command for the same give the command as: python -m pytest --html=report.html, 
a report.html file would be genarated.

to view the report, copy the path and paste it in browser
'''

# conftest.py
# here comes the def_pytest_runtest_markerport() code and it is template , thus it is to be copied either from RahulShetty's code or
# from online websites. We just need the capture_screenshot() function code and write it here


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)