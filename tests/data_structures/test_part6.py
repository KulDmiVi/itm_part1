import pytest
from data_structures.part6 import *


@pytest.mark.parametrize("input_list, expected_result", [
    ([4, 2, 1, 6, 3, 5], [1, 2, 3, 4, 5, 6]),
    (['s', 'b', 'e'], ['b', 'e', 's']),
])
def test_bubble_sort(input_list, expected_result):
    bubble_sort(input_list)
    assert input_list == expected_result


def test_binary_search_found():
    array = [1, 2, 3, 4, 5, 6]
    value = 4
    result = binary_search(array, value)
    assert result == 'ID = 3'


def test_binary_search_not_found():
    array = [1, 2, 3, 4, 5, 6]
    value = 7
    result = binary_search(array, value)
    assert result == 'No value'
