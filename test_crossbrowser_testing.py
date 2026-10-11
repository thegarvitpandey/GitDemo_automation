

import pytest

def test_crossBrowser_testing(crossBrowser_test):
    print('browsers fetched: ', crossBrowser_test)
    print('second value of the tuple we passed in conftest: ', crossBrowser_test[1])

    # on indexing the response, we are fetching indexed value of the params we passed in the fixture tuple in conftest

# datadriven and paramaterization can be done with return statements in tuple format

