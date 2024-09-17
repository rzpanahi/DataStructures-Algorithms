import unittest
from main import func


class MyTestCase(unittest.TestCase):
    def test_func(self):
        self.assertEqual(func())


if __name__ == '__main__':
    unittest.main()
