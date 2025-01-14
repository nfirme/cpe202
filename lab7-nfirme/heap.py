
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heapList = [0]
        self.capacity = capacity
        self.size = 0

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
        if self.is_full():
            return False
        else:
            self.heapList.append(item)
            self.size += 1
            self.perc_up(self.size)
            return True

    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        if self.is_empty():
            return None
        else:
            return self.heapList[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty():
            return None
        else:
            max_val = self.heapList[1]
            self.heapList[1] = self.heapList[self.size]
            self.size -= 1
            self.heapList.pop()
            self.perc_down(1)
            return max_val

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        return self.heapList[1:]

    def build_heap(self, alist):
        """Builds a heap from the items in alist and builds a heap using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased"""
        if len(alist) > self.capacity:
            self.capacity = len(alist)
        i = len(alist) // 2
        self.size = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        return self.get_size() == 0

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        return self.get_size() == self.capacity
        
    def get_capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.capacity
    
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.size
        
    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while (i * 2) <= self.size:
            max = self.max_child(i)
            if self.heapList[i] < self.heapList[max]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[max]
                self.heapList[max] = tmp
            i = max

    def max_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order"""
        self.heapList = [0]
        self.size = [0]
        self.build_heap(alist)

        i = len(alist) - 1

        while i > 0:
            alist[i] = self.dequeue()
            i = i - 1








