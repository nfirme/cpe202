import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_selection_empty(self):
        nums = []
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [])

    def test_selection_single(self):
        nums = [10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [10])

    def test_selection_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_selection_avg(self):
        nums = [16, 22, 5, 8, 2, 1, 100]
        comps = selection_sort(nums)
        self.assertEqual(comps, 21)
        self.assertEqual(nums, [1, 2, 5, 8, 16, 22, 100])

    def test_selection_best(self):
        nums = [1, 2, 3, 4, 5]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_selection_worst(self):
        nums = [5, 4, 3, 2, 1]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [1, 2, 3, 4, 5])


    def test_insertion_empty(self):
        nums = []
        comps = insertion_sort(nums)
        self.assertEqual(nums, [])

    def test_insertion_single(self):
        nums = [10]
        comps = insertion_sort(nums)
        self.assertEqual(nums, [10])

    def test_insertion_simple(self):
        nums = [40, 30]
        comps = insertion_sort(nums)
        self.assertEqual(nums, [30, 40])

    def test_insertion_avg(self):
        nums = [5, 7, 2, 4, 6, 3]
        comps = insertion_sort(nums)
        self.assertEqual(nums, [2, 3, 4, 5, 6, 7])

    def test_insertion_best(self):
        nums = [1, 2, 3, 4, 5]
        comps = insertion_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_insertion_worst(self):
        nums = [5, 4, 3, 2, 1]
        comps = insertion_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

if __name__ == '__main__': 
    unittest.main()
