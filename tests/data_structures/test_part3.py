

from data_structures.part3 import is_positive, is_odd, is_even, logic1, logic2, logic3, logic4, logic5, logic6, logic7


def test_is_positive_positive_number():
    assert is_positive(5) == True


def test_is_positive_null_number():
    assert is_positive(0) == False


def test_is_positive_negative_number():
    assert is_positive(-5) == False


def test_is_positive_zero():
    assert is_positive(0) == False


def test_is_odd_odd_number():
    assert is_odd(5) == True


def test_is_odd_even_number():
    assert is_odd(4) == False


def test_is_odd_zero():
    assert is_odd(0) == False


def test_is_even_even_number():
    assert is_even(4) == True


def test_is_even_odd_number():
    assert is_even(5) == False


def test_is_even_zero():
    assert is_even(0) == False


def test_logic1_true():
    assert logic1(3, 3) == True


def test_logic1_false():
    assert logic1(1, 4) == False


def test_logic2_true():
    assert logic2(1, -3) == True


def test_logic2_false():
    assert logic2(-1, -2) == False


def test_logic3_true():
    assert logic3(1, 2, 3) == True


def test_logic3_false():
    assert logic3(3, 2, 1) == False


def test_logic4_true():
    assert logic4(1, 2, 3) == True

def test_logic4_false():
    assert logic4(1, 1, 1) == True
def test_logic4_false():
    assert logic4(3, 2, 1) == True


def test_logic5_true():
    assert logic5(3, 5) == True


def test_logic5_false():
    assert logic5(2, 4) == False


def test_logic6_true():
    assert logic6(3, 4) == True


def test_logic6_false():
    assert logic6(2, 4) == False


def test_logic7_true():
    assert logic7(3, 4) == True


def test_logic7_false():
    assert logic7(2, 4) == False
