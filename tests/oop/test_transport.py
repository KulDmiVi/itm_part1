import unittest
from oop.transport import MeansOfTransport, Car, Moped


class TestTransport(unittest.TestCase):
    def setUp(self):
        self.car = Car('blue', 'volvo', 4)
        self.moped = Moped('green', 'karpatii')

    def test_show_color(self):
        self.assertEqual(self.car.show_color(), 'blue')
        self.assertEqual(self.moped.show_color(), 'green')

    def test_show_brand(self):
        self.assertEqual(self.car.show_brand(), 'volvo')
        self.assertEqual(self.moped.show_brand(), 'karpatii')

    def test_color_property(self):
        self.car.color = 'red'
        self.assertEqual(self.car.color, 'red')
        self.moped.color = 'yellow'
        self.assertEqual(self.moped.color, 'yellow')

    def test_brand_property(self):
        self.car.brand = 'ford'
        self.assertEqual(self.car.brand, 'ford')
        self.moped.brand = 'vespa'
        self.assertEqual(self.moped.brand, 'vespa')

    def test_min_arrival_time(self):
        self.assertEqual(Moped.min_arrival_time(50, 100), 2.0)
        self.assertEqual(Moped.min_arrival_time(30, 150), 5.0)

    def test_car_drive(self):
        self.assertEqual(self.car.car_drive, 4)


if __name__ == '__main__':
    unittest.main()
