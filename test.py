import pytest
from main import square_root

def test_perfect_square():
    assert square_root(4, 2) == 2.0
    assert square_root(9, 2) == 3.0

def test_non_perfect_square():
    assert square_root(2, 5) == pytest.approx(round(2 ** 0.5, 5), rel=1e-5)

def test_zero():
    assert square_root(0, 2) == 0.0  # Handle sqrt(0)

def test_one():
    assert square_root(1, 2) == 1.0

def test_negative_number():
    with pytest.raises(ValueError, match="Cannot calculate the square root of a negative number"):
        square_root(-4, 2)

def test_high_precision():
    assert square_root(2, 10) == round(2 ** 0.5, 10)  # Test high precision on √2
    assert square_root(100, 10) == round(10.0, 10)  # Test high precision on √100

def test_large_numbers():
    assert square_root(1000000, 5) == round(1000.0, 5)  # Test large numbers like √1000000
