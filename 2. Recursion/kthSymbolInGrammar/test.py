import unittest
from main import func


class MyTestCase(unittest.TestCase):
    def test_function(self):
        self.assertEqual(func(11, 5), 0)
        self.assertEqual(func(12, 5), 1)
        self.assertEqual(func(16, 5), 0)
        self.assertEqual(func(5, 5), 1)
        self.assertEqual(func(7, 4), 0)
        self.assertEqual(func(2, 4), 1)


if __name__ == '__main__':
    unittest.main()
