import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_empty(self):
        l = OrderedList()
        self.assertTrue(l.is_empty())

    def test_not_empty(self):
        l = OrderedList()
        l.add(5)
        l.add(10)
        self.assertFalse(l.is_empty())

    def test_add_unordered(self):
        l = OrderedList()
        l.add(20)
        l.add(10)
        l.add(5)
        l.add(30)
        l.add(20)
        l.add(20)
        l.add(1)
        l.add(15)
        l.add(40)

    def test_remove(self):
        l = OrderedList()
        l.add(10)
        l.add(50)
        l.add(5)
        l.add(20)
        self.assertTrue(l.remove(20))

    def test_remove_not_in_list(self):
        l = OrderedList()
        l.add(1)
        l.add(2)
        l.add(3)
        l.add(4)
        self.assertFalse(l.remove(5))

    def test_index(self):
        l = OrderedList()
        l.add(10)
        l.add(20)
        l.add(30)
        l.add(15)
        l.add(5)
        self.assertEqual(l.index(30), 4)

    def test_index_not_in_list(self):
        l = OrderedList()
        l.add(2)
        l.add(4)
        l.add(6)
        self.assertIsNone(l.index(3))

    def test_python_list(self):
        l = OrderedList()
        l.add(10)
        l.add(5)
        l.add(50)
        l.add(3.0)
        l.add(4.3)
        l.add(25)
        l.add(100)
        self.assertEqual(l.python_list(), [3.0, 4.3, 5, 10, 25, 50, 100])

    def test_pop(self):
        l = OrderedList()
        l.add(10)
        l.add(20)
        l.add(30)
        l.add(40)
        self.assertEqual(l.pop(1), 20)
        self.assertEqual(l.python_list(), [10, 30, 40])

    def test_search(self):
        l = OrderedList()
        l.add(10)
        l.add(20)
        l.add(30)
        l.add(40)
        self.assertTrue(l.search(20))
        self.assertFalse(l.search(50))

    def test_size(self):
        l = OrderedList()
        l.add(5)
        l.add(10)
        l.add(15)
        l.add(20)
        self.assertEqual(l.size(), 4)

    def test_reverse_python_list(self):
        l = OrderedList()
        l.add(10)
        l.add(20)
        l.add(30)
        self.assertEqual(l.python_list_reversed(), [30, 20, 10])

    def test_reverse_python_list_empty(self):
        l = OrderedList()
        self.assertEqual(l.python_list_reversed(), [])

    def test_string(self):
        l = OrderedList()
        l.add("hi")
        l.add('Hi')
        l.add('hello')
        self.assertEqual(l.python_list(), ['Hi', 'hello', 'hi'])

    def test_string_reverse(self):
        l = OrderedList()
        l.add("a")
        l.add("b")
        l.add("c")
        self.assertEqual(l.python_list_reversed(), ["c", "b", "a"])

    def test_duplicate_strings(self):
        l = OrderedList()
        l.add("apple")
        l.add("banana")
        l.add("carrot")
        l.add("carrot")
        self.assertEqual(l.python_list(), ["apple", "banana", "carrot"])

    def test_pop_negative_index(self):
        l = OrderedList()
        l.add(10)
        l.add(20)
        l.add(30)
        with self.assertRaises(IndexError):
            l.pop(-1)

    def test_search_empty_list(self):
        l = OrderedList()
        self.assertFalse(l.search(10))

    def test_pop_greater_than_size(self):
        l = OrderedList()
        l.add(10)
        l.add(20)
        l.add(30)
        with self.assertRaises(IndexError):
            l.pop(4)


if __name__ == '__main__': 
    unittest.main()
