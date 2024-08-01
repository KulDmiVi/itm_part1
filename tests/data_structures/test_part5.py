import unittest

from data_structures.part5 import *


class TestPeopleFunctions(unittest.TestCase):
    def setUp(self):
        self.test_people = {
        'name': 'Василий Василиевич',
        'age': 27,
        'sex': 'м',
        'height': 182,
        'weight': 115,
        'foot_size': 42,
    }

    def test_people_info(self):
        self.assertEqual(
            people_info(self.test_people),
    "name: Василий Василиевич age: 27 sex: м height: 182 weight: 115 foot_size: 42"
        )

    def test_del_key_age(self):
        del_key_age(self.test_people)
        self.assertNotIn('age', self.test_people)

    def test_modify_foot_size(self):
        foot_size = 39
        modify_foot_size(self.test_people, foot_size)
        self.assertEqual(self.test_people['foot_size'], foot_size)


if __name__ == '__main__':
    unittest.main()
