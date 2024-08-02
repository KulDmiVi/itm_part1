import unittest
from unittest.mock import patch
from conditions.conditions import *


class TestMainFunctions(unittest.TestCase):
    @patch('builtins.input', side_effect=["5", "0", "7"])
    def test_get_positive_count(self, mock_input):
        result = get_positive_count()
        self.assertEqual(result, "Количество положительных чисел: 2")

    @patch('builtins.input', side_effect=["8", "2"])
    def test_get_max_number(self, mock_input):
        result = get_max_number()
        self.assertEqual(result, "Большее число: 8.0")

    @patch('builtins.input', side_effect=["8", "2"])
    def test_get_min_max_number(self, mock_input):
        result = get_min_max_number()
        self.assertEqual(result, "Большее число: 8.0 \n Меньшее число: 2.0")

    @patch('builtins.input', side_effect=["1", "3", "2"])
    def test_get_min_number(self, mock_input):
        result = get_min_number()
        self.assertEqual(result, "Минимальное из чисел: 1.0")

    @patch('builtins.input', side_effect=["3", "4"])
    def test_get_quarter_number(self, mock_input):
        result = get_quarter_number()
        self.assertEqual(result, "Точка принадлежит 1-ой четверти")


if __name__ == '__main__':
    unittest.main()
