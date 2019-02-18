import unittest
#from queue_array import Queue
from queue_linked import Queue


class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_queue2(self):
        q = Queue(10)
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

    def test_queue3(self):
        q = Queue(3)
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        self.assertTrue(q.is_full())
        with self.assertRaises(IndexError):
            q.enqueue('d')

    def test_queue4(self):
        q = Queue(4)
        q.enqueue(10)
        q.enqueue(20)
        self.assertEqual(q.size(), 2)

    def test_queue5(self):
        q = Queue(5)
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        q.enqueue(40)
        q.enqueue(50)
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.size(), 3)

    def test_queue6(self):
        q = Queue(1)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_queue7(self):
        q = Queue(0)
        with self.assertRaises(IndexError):
            q.enqueue(10)

    def test_queue8(self):
        q = Queue(3)
        q.enqueue(1.1)
        q.enqueue(2.2)
        q.enqueue(3.3)
        self.assertTrue(q.is_full())

    def test_queue9(self):
        q = Queue(4)
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        q.enqueue(40)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_queue10(self):
        q = Queue(3)
        q.enqueue(None)
        self.assertFalse(q.is_full())
        self.assertFalse(q.is_empty())

    def test_queue11(self):
        q = Queue(3)
        q.enqueue(10)
        q.enqueue(20)
        self.assertEqual(q.dequeue(), 10)

if __name__ == '__main__': 
    unittest.main()
