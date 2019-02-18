class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           Do not have an attribute to keep track of size'''
        self.head = Node("It's a secret to everybody")
        self.head.next = self.head
        self.head.prev = self.head

    def is_empty(self):
        '''Returns back True if OrderedList is empty
            MUST have O(1) performance'''
        if self.head.next == self.head:
            return True
        else:
            return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           If the item is already in the list, do not add it again 
           MUST have O(n) average-case performance'''
        new_node = Node(item)

        if self.is_empty():
            self.head.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            cur = self.head.next

            while cur != self.head:
                if item == cur.item:  # checks if item has duplicates in list
                    break
                elif item < cur.item: # for adding at beginning and inserting
                    new_node.next = cur
                    new_node.prev = cur.prev
                    cur.prev.next = new_node
                    cur.prev = new_node
                    break

                if cur.next == self.head and item > cur.item:  # for appending
                    new_node.next = self.head
                    new_node.prev = cur
                    self.head.prev = new_node
                    cur.next = new_node

                cur = cur.next

    def remove(self, item):
        '''Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''

        cur = self.head.next

        while cur != self.head:
            if item == cur.item:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            cur = cur.next
        return False

    def index(self, item):
        '''Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        cur = self.head.next
        index = 0

        while cur != self.head:
            if item == cur.item:
                return index
            else:
                cur = cur.next
                index += 1

        return None


    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0 or index > self.size():
            raise IndexError('Index must be greater than 0')

        cur = self.head.next

        for i in range(index):
            cur = cur.next

        cur.prev.next = cur.next
        cur.next.prev = cur.prev

        return cur.item

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        if self.is_empty():
            return False
        return self.search_helper(self.head.next, item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''

        p_list = []
        cur = self.head.next
        while cur != self.head:
            p_list.append(cur.item)
            cur = cur.next
        return p_list

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        r_list = []
        if self.is_empty():
            return r_list
        return self.reverse_helper(self.head.prev)


    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.head.next)

    def search_helper(self, node, item):
        if node == self.head:
            return False
        if node.item == item:
            return True
        return self.search_helper(node.next, item)

    def size_helper(self, node):
        if node == self.head:
            return 0
        return 1 + self.size_helper(node.next)

    def reverse_helper(self, node):
        rlist = []
        if node == self.head:
            return rlist
        return rlist + [node.item] + self.reverse_helper(node.prev)