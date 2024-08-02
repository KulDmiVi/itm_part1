import builtins
from unittest import mock

import pytest

from exception_logging.quadratic_equation import *


def test_input_data():
    test_user_input = ["2", "3", "4"]
    with mock.patch.object(builtins, 'input', lambda _: test_user_input.pop(0)):
        assert input_data() == (2.0, 3.0, 4.0)


def test_input_failed():
    test_user_input1 = ["2", "oko", "4"]
    with mock.patch.object(builtins, 'input', lambda _: test_user_input1.pop(0)):
           assert input_data() == None




def test_get_discr():
    assert get_discr(2.0, 3.0, 4.0) == -23.0


def test_calc_roots_equation():
    assert calc_roots_equation(2.0, 3.0, -23) == 'Уравнение не имеет действительных корней'
