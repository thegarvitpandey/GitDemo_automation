
import pytest

# here we define the setup name from the conftest fixture file
#note that we are using usefixtures instead of fixtures

@pytest.mark.usefixtures("setup")
class Test_example:

    def test_ficturedemo1(self):
        print(' this is fixture file 1 created initially')

    def test_ficturedemo2(self):
        print(' this is fixture file 2 created initially')

    def test_ficturedemo3(self):
        print(' this is fixture file 3 created initially')

# only when we pass the setup of fixtures, the methods are related to the fixture
# in pytest after if the code is written after "yield" keyword, then that part would be run after the entire script has run