# all files of pytest must either start as "test_" or end with "_test"
# always write the code inside the functions /methods
# the pytest methods must always start with test_
import pytest
# to run the pytest file from terminal copy the path of the folder and cd /d and path of the file and then give cmd as "py.test" and it would
# all the files inside the folder
# to get more information about your tests, give the command as "py.test -v" v stands for verbose here which gives info
# about test results

# to print console logs i.e., the things which we want to print with print() function in the terminal too
# then give the command as py.test -v - s


# ------->    MODERN PYTEST USES python -m pytest -v -s command to run rather than py.test     <---------

# Additionally, in case the Venv is closed, then start it as:
# E:\Automation\Pycharm scripts\pytests_Demo_projects>.venv\Scripts\activate

# in case we have same methods, then pytest would override the previous method

# to run a specific file, give the file name in the command as python -m pytest file_name -v -s

# -k means method names execution, -s logs in output


# to run a specific test case (methods or functions), give the command as: python -m pytest -k text -v -s
# eg: python -m pytest -k Prgm -v -s

#to run grouped / tagged test case, commandd as: python -m pytest -m demo -v -s,   -m means marking so -m followed by your mark tag name here it is demo

# you can skip of the tests while running all the scripts, for that mark those test cases as: @python.mark.skip
# so skip is inbuit pytest tags

# in case you want to run a test case but it might fail and you don't want it in the output results, you can mark it as:
#   @pytest.mark.xfail

@pytest.mark.demo
def test_first_Program():
    print('Running first prgm running test')

@pytest.mark.skip
def test_second_Prgm():
    print('second prgm running test')