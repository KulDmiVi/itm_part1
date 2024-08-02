
from exception_logging.arithmetic_mean import calc_arithmetic_mean

import sys

def test_arithmetic():
    assert calc_arithmetic_mean((1, 2, 3)) == 2.0
    assert calc_arithmetic_mean((0, 0, 0, 0)) == 0.0
    assert calc_arithmetic_mean((10, 20, 30, 40, 50)) == 30.0
    print(sys.path)

