import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
#from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)

    def test_stack2(self):
        stack = Stack(0)
        with self.assertRaises(IndexError):
            stack.push(1)

    def test_stack3(self):
        stack = Stack(3)
        stack.push(0)
        stack.push(0)
        stack.push(0)
        self.assertTrue(stack.is_full())

    def test_stack4(self):
        stack = Stack(5)
        stack.push(0)
        stack.push(0)
        stack.push(0)
        stack.pop()
        self.assertEqual(stack.size(), 2)

    def test_stack5(self):
        stack = Stack(3)
        stack.push(None)
        stack.push(None)
        stack.push(None)
        self.assertTrue(stack.is_full())

    def test_stack6(self):
        stack = Stack(3)
        stack.push("hi")
        stack.push("hola")
        stack.push("bonjour")
        with self.assertRaises(IndexError):
            stack.push("yo")

    def test_stack7(self):
        stack = Stack(3)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_stack8(self):
        stack = Stack(3)
        with self.assertRaises(IndexError):
            stack.peek()

    def test_stack9(self):
        stack = Stack(3)
        self.assertTrue(stack.is_empty())

    def test_stack10(self):
        stack = Stack(5)
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.peek(), 30)
        stack.pop()
        self.assertEqual(stack.peek(), 20)





if __name__ == '__main__': 
    unittest.main()
