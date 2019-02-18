import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_simple2(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'a')
        bst.insert(5, 'b')
        bst.insert(15, 'c')
        bst.insert(20, 'd')
        self.assertFalse(bst.is_empty())
        self.assertEqual(bst.find_max(), (20, 'd'))
        self.assertEqual(bst.find_min(), (5, 'b'))
        self.assertTrue(bst.search(5))
        self.assertFalse(bst.search(30))
        self.assertEqual(bst.tree_height(), 2)

    def test_empty_tree(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertEqual(bst.find_max(), None)
        self.assertEqual(bst.find_min(), None)
        self.assertFalse(bst.search(10))
        self.assertEqual(bst.tree_height(), None)
        self.assertEqual(bst.inorder_list(), [])
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.level_order_list(), [])

    def test_inorder_traversal(self):
        bst = BinarySearchTree()
        bst.insert(10, 'hi')
        bst.insert(5, 'hi')
        bst.insert(15, 'hi')
        bst.insert(3, 'hi')
        bst.insert(7, 'hi')
        bst.insert(12, 'hi')
        bst.insert(18, 'hi')
        self.assertEqual(bst.inorder_list(), [3, 5, 7, 10, 12, 15, 18])

    def test_level_traversal(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(18)
        self.assertEqual(bst.level_order_list(), [10, 5, 15, 3, 7, 12, 18])

    def test_preorder_traverseal(self):
        bst = BinarySearchTree()
        bst.insert(10, 'hi')
        bst.insert(5, 'hi')
        bst.insert(15, 'hi')
        bst.insert(3, 'hi')
        bst.insert(7, 'hi')
        bst.insert(12, 'hi')
        bst.insert(18, 'hi')
        self.assertEqual(bst.preorder_list(), [10, 5, 3, 7, 15, 12, 18])

    def test_replace_node(self):
        bst = BinarySearchTree()
        bst.insert(10, 'hi')
        bst.insert(10, 'goodbye')
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.find_min(), (10, 'goodbye'))

if __name__ == '__main__': 
    unittest.main()
