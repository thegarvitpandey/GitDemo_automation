import pytest

@pytest.mark.xfail
def test_Prgm(setup):
    print('Running test_Prgm_3')

@pytest.mark.demo
def test_msg():
    msg = "Hello"
    assert msg == "Hello", "Test failed as condition didn't match"
