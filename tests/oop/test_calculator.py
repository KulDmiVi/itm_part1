from oop.calculator import Calculator, StrCalculator
import pytest


def test_calculate_sum_valid():
    assert Calculator.calculate_sum(2, 3) == 5


def test_calculate_sum_invalid():
    with pytest.raises(TypeError):
        Calculator.calculate_sum('a', 'b')


def test_str_calculate_sum_valid():
    assert StrCalculator.calculate_sum('hello', 'world') == 'helloworld'


def test_str_calculate_sum_invalid():
    with pytest.raises(TypeError):
        StrCalculator.calculate_sum(1, 2)
