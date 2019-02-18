
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.num_items = 0
        self.items = [None] * capacity
        self.front = 0
        self.back = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.size() == 0

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return self.num_items == self.capacity

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full():
            raise IndexError('Queue is full')
        else:
            self.items[self.back] = item
            self.back = (self.back + 1) % self.capacity  # finds first empty index in array
            self.num_items += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            val = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.num_items -= 1
            return val

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items

