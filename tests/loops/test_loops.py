import builtins

from loops.main import *
from unittest import mock


def test_average_positive_number_input():
    test_user_input = ["2", "3", "4", "0"]
    with mock.patch.object(builtins, 'input', lambda _: test_user_input.pop(0)):
        assert average() == "Среднее арифметическое: 3.0"


def test_average_negative_number_input():
    test_user_input = ["-5", "-10", "-15", "0"]
    with mock.patch.object(builtins, 'input', lambda _: test_user_input.pop(0)):
        assert average() == "Среднее арифметическое: -10.0"


def test_average_mixed_number_input():
    test_user_input = ["5", "-10", "15", "0"]
    with mock.patch.object(builtins, 'input', lambda _: test_user_input.pop(0)):
        assert average() == "Среднее арифметическое: 3.3333333333333335"


def test_average_non_numeric_input():
    test_user_input = ["a", "-10", "15", "0"]
    with mock.patch.object(builtins, 'input', lambda _: test_user_input.pop(0)):
        assert average() == "Введенное значение не корректно"


def test_output_range():
    assert output_range() == list(range(101))


def test_output_list_length():
    assert len(output_list()) == 10


def test_output_dict_length():
    assert len(output_dict()) == 10


def test_summ_100():
    assert summ_100() == 5050


def test_prime_numbers():
    assert prime_numbers() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def test_sqrt_sums():
    assert sqrt_sums() == 385


def test_get_factorial():
    assert get_factorial() == "1: 1 2: 2 3: 6 4: 24 5: 120"
