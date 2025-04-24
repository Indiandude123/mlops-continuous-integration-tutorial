import pytest

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5

# Testing square function
def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) == 9, "Test Failed: Square of 3 should be 9"
    
# Testing cube function
def test_cube():
    assert cube(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: Cube of 3 should be 27"
    
    
# Testing fifth_power function
def test_fifth_power():
    assert fifth_power(2) == 32, "Test Failed: fifth power of 2 should be 32"
    assert fifth_power(3) == 243, "Test Failed: fifth power of 3 should be 243"
    

# Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")