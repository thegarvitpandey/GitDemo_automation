

# here we are learning about the data driven testing, we'll load data from conftest file

import pytest

@pytest.mark.usefixtures("dataLoad")
class Test_example2:

# if you see we are passing here "dataLoad" as parameter since we want return something from confest dataload fixture method
    def test_dataLoad(self, dataLoad):
        print('printing dataload of 0th index: ', dataLoad[0])
        print('printing dataload of 1st index: ', dataLoad[1])
        print('printing dataload of 2nd index: ', dataLoad[2])