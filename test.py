import pytest
from io import StringIO
from main import get_input, calculate_square_root, display_output

# get_input
def test_get_input_positive_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('16\n3\n'))
    n, accuracy = get_input()
    assert n == 16
    assert accuracy == 3

def test_get_input_zero_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('0\n5\n'))
    n, accuracy = get_input()
    assert n == 0
    assert accuracy == 5

def test_get_input_negative_accuracy(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('25\n-2\n'))
    n, accuracy = get_input()
    assert n == 25
    assert accuracy == -2

def test_get_input_high_accuracy(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('81\n10\n'))
    n, accuracy = get_input()
    assert n == 81
    assert accuracy == 10

def test_get_input_float_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('5.76\n4\n'))
    n, accuracy = get_input()
    assert n == 5.76
    assert accuracy == 4

# calculate_square_root

def test_calculate_square_root_positive_number():
    result = calculate_square_root(16, 3)
    assert result == 4.0

def test_calculate_square_root_high_accuracy():
    result = calculate_square_root(2, 10)
    assert abs(result - 1.4142135624) < 1e-10  # Checking within 10 decimal places

def test_calculate_square_root_of_zero():
    result = calculate_square_root(0, 5)
    assert result == 0.0

def test_calculate_square_root_negative_number():
    with pytest.raises(ValueError):
        calculate_square_root(-4, 2)

def test_calculate_square_root_large_number():
    result = calculate_square_root(1e6, 2)
    assert result == 1000.0

# display_output

def test_display_output_positive_number(capsys):
    display_output(4.0)
    captured = capsys.readouterr()
    assert "The square root is approximately: 4.0" in captured.out

def test_display_output_high_precision(capsys):
    display_output(1.4142135624)
    captured = capsys.readouterr()
    assert "The square root is approximately: 1.4142135624" in captured.out

def test_display_output_zero(capsys):
    display_output(0.0)
    captured = capsys.readouterr()
    assert "The square root is approximately: 0.0" in captured.out

def test_display_output_rounding(capsys):
    display_output(3.142)
    captured = capsys.readouterr()
    assert "The square root is approximately: 3.142" in captured.out

def test_display_output_negative_result(capsys):
    display_output(-1)
    captured = capsys.readouterr()
    assert "The square root is approximately: -1" in captured.out

