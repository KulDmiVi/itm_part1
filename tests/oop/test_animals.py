import unittest
from unittest.mock import patch
from oop.animals import Cat


class TestCat(unittest.TestCase):
    def test_voice(self):
        with patch('builtins.print') as mocked_print:
            cat = Cat('Whiskers')
            cat.voice()
            mocked_print.assert_called_once_with('meow')


if __name__ == '__main__':
    unittest.main()
