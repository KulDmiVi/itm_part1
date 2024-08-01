import unittest
from data_structures.part1 import *


class FiguresTests(unittest.TestCase):
    def test_square_perimetr(self):
        self.assertEqual(square_perimetr(4), 16)
        self.assertEqual(square_perimetr(5), 20)

    def test_square_area(self):
        self.assertEqual(square_area(4), 16)
        self.assertEqual(square_area(5), 25)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(4, 5), 20)
        self.assertEqual(rectangle_area(5, 6), 30)

    def test_rectangle_perimetr(self):
        self.assertEqual(rectangle_perimetr(4, 5), 18)
        self.assertEqual(rectangle_perimetr(5, 6), 22)

    def test_d_circumference(self):
        self.assertAlmostEqual(d_circumference(4), 12.56, places=2)
        self.assertAlmostEqual(d_circumference(5), 15.70, places=2)

    def test_cube_volume(self):
        self.assertEqual(cube_volume(4), 64)
        self.assertEqual(cube_volume(5), 125)

    def test_parallelepiped_volume(self):
        self.assertEqual(parallelepiped_volume(4, 5, 6), 120)
        self.assertEqual(parallelepiped_volume(5, 6, 7), 210)


class MathematicalOperationTests(unittest.TestCase):
    def test_arithmetic_mean(self):
        self.assertEqual(arithmetic_mean(4, 6), 5.0)

    def test_geometric_mean(self):
        self.assertEqual(geometric_mean(4, 9), 6.0)

    def test_sum_squares(self):
        self.assertEqual(sum_squares(3, 4), 25)

    def test_difference_squares(self):
        self.assertEqual(difference_squares(5, 2), 21)

    def test_multiplication_squares(self):
        self.assertEqual(multiplication_squares(4, 3), 144)

    def test_division_squares(self):
        self.assertEqual(division_squares(9, 3), 9.0)


if __name__ == '__main__':
    unittest.main()
