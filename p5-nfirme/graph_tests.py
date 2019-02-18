import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())

    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_03(self):
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3']])
        self.assertFalse(g.is_bipartite())

    def test_vertex_functions(self):
        g = Graph('test1.txt')
        g.add_vertex('v0')
        self.assertEqual(g.get_vertices(), ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        g.add_edge('v0', 'v1')
        self.assertIsNone(g.get_vertex('u1'))


if __name__ == '__main__':
    unittest.main()
