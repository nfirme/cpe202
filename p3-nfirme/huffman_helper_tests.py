import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):
    def test_comes_before(self):
        node1 = HuffmanNode(97, 2)
        node2 = HuffmanNode(98, 3)
        self.assertTrue(comes_before(node1, node2))
        self.assertFalse(comes_before(node2, node1))

    def test_comes_before_diff(self):
        node1 = HuffmanNode(97, 10)
        node2 = HuffmanNode(98, 10)
        self.assertTrue(comes_before(node1, node2))
        self.assertFalse(comes_before(node2, node1))

    def test_combine(self):
        a = HuffmanNode(100, 4)
        b = HuffmanNode(110, 9)
        self.assertEqual(combine(a, b).char, 100)
        self.assertEqual(combine(a, b).freq, 13)

    def test_code_helper(self):
        node = None
        code_list = [''] * 256
        code = ''
        self.assertEqual(code_helper(node, code, code_list), [])


