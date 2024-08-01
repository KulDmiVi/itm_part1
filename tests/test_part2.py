import unittest
from data_structures.part2 import *


class functionTest(unittest.TestCase):

    def test_centimeters_to_meters(self):
        self.assertEqual(centimeters_to_meters(150), 1)

    def test_kilograms_to_tons(self):
        self.assertEqual(kilograms_to_tons(2500), 2)

    def test_bytes_to_kbytes(self):
        self.assertEqual(bytes_to_kbytes(2048), 2)

    def test_segments_count(self):
        self.assertEqual(segments_count(20, 3), 6)

    def test_segment_free_part(self):
        self.assertEqual(segment_free_part(20, 3), 2)

    def test_left_right_part(self):
        self.assertEqual(left_right_part(45), None)  # Function prints the result

    def test_summ_digit(self):
        self.assertEqual(summ_digit(45), 9)

    def test_multiplication_digit(self):
        self.assertEqual(multiplication_digit(45), 20)

    def test_first_digit(self):
        self.assertEqual(first_digit(345), None)  # Function prints the result

    def test_last_second_digit(self):
        self.assertEqual(last_second_digit(345), None)  # Function prints the result


if __name__ == '__main__':
    unittest.main()
