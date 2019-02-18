import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([]), None) # list is empty
        self.assertEqual(max_list_iter([1, 2, 3, 4, 5]), 5) # list is sorted
        self.assertEqual(max_list_iter([17, 32, 8, 99, 0, 2]), 99) # list is unsorted
        self.assertEqual(max_list_iter([-2, -4, -6, -8, -10]), -2) # list is negative


    def test_reverse_rec(self):
        sList = None
        with self.assertRaises(ValueError):                 # checks ValueError if list is None
            reverse_rec(sList)
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1]) # sorted list
        self.assertEqual(reverse_rec([]), [])               # empty list
        self.assertEqual(reverse_rec([1]), [1])             # len(list) = 1
        self.assertEqual(reverse_rec([4, 10, 2, 16, 32, -1]), [-1, 32, 16, 2, 10, 4]) # unsorted list with negatives
        self.assertEqual(reverse_rec(['hi', 'bye', 'hola', 'adios']), ['adios', 'hola', 'bye', 'hi']) # lists of strings
        self.assertEqual(reverse_rec([1.2, 3.4, 10.6, 8.7]), [8.7, 10.6, 3.4, 1.2]) #lists of floats


    def test_bin_search(self):
        uList = None
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        list_single = [2]
        low = 0
        high = len(list_val) - 1
        with self.assertRaises(ValueError): # if list is None
            bin_search(100, low, high, uList)
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4) # target is mid
        self.assertEqual(bin_search(1, 0, len(list_val) - 1, list_val), 1) # target is less than mid
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8) # target is greater than mid
        self.assertEqual(bin_search(5, 0, len(list_val), list_val), None) # target is not found in list
        self.assertEqual(bin_search(2, 0, len(list_single) - 1, list_single), 0) # list is len = 1


if __name__ == "__main__":
    unittest.main()

