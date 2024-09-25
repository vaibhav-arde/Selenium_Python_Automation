import pytest

def test_firstProgram():
    print("Hello")
    
def test_secondProgram():
    msg = "hi"
    assert msg == "Hi", "Test failed because strings do not match"
    
@pytest.mark.smoke1
def test_markProgram():
    msg = "Hi"
    assert msg == "Hi", "Test failed because strings do not match"