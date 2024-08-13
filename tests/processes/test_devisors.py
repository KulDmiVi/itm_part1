import pytest
from multithreading.find_divisors import get_divisors, get_divisors_line

def test_get_divisors():
    assert get_divisors(12) == [1, 2, 3, 4, 6, 12]
    assert get_divisors(28) == [1, 2, 4, 7, 14, 28]
    assert get_divisors(1) == [1]
    assert get_divisors(0) == []
    assert get_divisors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
    assert get_divisors(13) == [1, 13]  #

def test_get_divisors_line():
    assert get_divisors_line(12) == [1, 2, 3, 4, 6, 12]
    assert get_divisors_line(28) == [1, 2, 4, 7, 14, 28]
    assert get_divisors_line(1) == [1]
    assert get_divisors_line(0) == []
    assert get_divisors_line(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
    assert get_divisors_line(13) == [1, 13]


if __name__ == "__main__":
    pytest.main()