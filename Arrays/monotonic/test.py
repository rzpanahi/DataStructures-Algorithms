import unittest
from main import isMonotonic


class TestMonotonicArray(unittest.TestCase):
    def test_empty_array(self):
        arr = []

        self.assertTrue(isMonotonic(arr))
    
    def test_single_element_array(self):
        arr = [5]

        self.assertTrue(isMonotonic(arr))
    
    def test_increasing_monotonic_array(self):
        arr = [-7, -3, 0, 2, 5, 9]

        self.assertTrue(isMonotonic(arr))
    
    def test_decreasing_monotonic_array(self):
        arr = [8, 5, 2, 0, -1, -4]

        self.assertTrue(isMonotonic(arr))


    def test_non_monotonic_array(self):
        arr = [2, 8, 10, -3]

        self.assertFalse(isMonotonic(arr))

    def test_all_same_value(self):
        arr = [2, 2, 2, 2]

        self.assertTrue(isMonotonic(arr))