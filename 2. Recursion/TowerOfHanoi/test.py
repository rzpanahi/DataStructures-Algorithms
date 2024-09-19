import unittest
from main import tower_of_hanoi

class MyTestCase(unittest.TestCase):
    def test_tower_of_hanoi(self):

        self.assertEqual(tower_of_hanoi(5), 31)  # add assertion here
        self.assertEqual(tower_of_hanoi(6), 63)  # add assertion here
        self.assertEqual(tower_of_hanoi(12), 4095)  # add assertion here


if __name__ == '__main__':
    unittest.main()
